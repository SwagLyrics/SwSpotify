import sys
from SwSpotify import SpotifyClosed, SpotifyPaused, SpotifyNotRunning


def get_info_windows():
    """
    Reads the window titles to get the data.

    Older Spotify versions simply use FindWindow for "SpotifyMainWindow",
    the newer ones create an EnumHandler and flood the list with
    Chrome_WidgetWin_0s
    """

    import win32gui

    windows = []

    old_window = win32gui.FindWindow("SpotifyMainWindow", None)
    old = win32gui.GetWindowText(old_window)

    def find_spotify_uwp(hwnd, windows):
        text = win32gui.GetWindowText(hwnd)
        classname = win32gui.GetClassName(hwnd)
        if classname == "Chrome_WidgetWin_0" and len(text) > 0:
            windows.append(text)

    if old:
        windows.append(old)
    else:
        win32gui.EnumWindows(find_spotify_uwp, windows)

    # If Spotify isn't running the list will be empty
    if len(windows) == 0:
        raise SpotifyClosed

    # Local songs may only have a title field
    try:
        artist, track = windows[0].split(" - ", 1)
    except ValueError:
        artist = ''
        track = windows[0]

    # The window title is the default one when paused
    if windows[0].startswith('Spotify'):
        raise SpotifyPaused

    return track, artist


def get_info_linux():
    """
    Uses the dbus API to get the data.
    """

    import dbus
    if not hasattr(get_info_linux, 'session_bus'):
        get_info_linux.session_bus = dbus.SessionBus()
    try:
        spotify_bus = get_info_linux.session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        spotify_properties = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")
        metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    except dbus.exceptions.DBusException:
        raise SpotifyClosed

    track = str(metadata['xesam:title'])
    # When this function is called and Spotify hasn't finished setting up the dbus properties, the artist field
    # is empty. This counts as if it weren't open because no data is loaded.
    try:
        artist = str(metadata['xesam:artist'][0])
    except IndexError:
        raise SpotifyClosed from None
    status = str(spotify_properties.Get("org.mpris.MediaPlayer2.Player", "PlaybackStatus"))
    if status.lower() != 'playing':
        raise SpotifyPaused

    return track, artist


def get_info_mac():
    """
    Runs an AppleScript script to get the data.

    Exceptions aren't thrown inside get_info_mac because it automatically
    opens Spotify if it's closed.
    """

    from Foundation import NSAppleScript

    apple_script_code = """
    getCurrentlyPlayingTrack()

    on getCurrentlyPlayingTrack()
        tell application "Spotify"
            set isPlaying to player state as string
            set currentArtist to artist of current track as string
            set currentTrack to name of current track as string
            return {currentArtist, currentTrack, isPlaying}
        end tell
    end getCurrentlyPlayingTrack
    """

    try:
        s = NSAppleScript.alloc().initWithSource_(apple_script_code)
        x = s.executeAndReturnError_(None)
        a = str(x[0]).split('"')
        if a[5].lower() != 'playing':
            raise SpotifyPaused
    except IndexError:
        raise SpotifyClosed from None

    return a[3], a[1]


def get_info_web():
    import SwSpotify.web_server
    import os
    import contextlib
    from SwSpotify import WebData
    with open(os.devnull, 'w') as f, contextlib.redirect_stdout(f):
        SwSpotify.web_server.run()
    if not WebData.track:
        raise SpotifyClosed
    elif WebData.playState == "Play":
        raise SpotifyPaused
    else:
        return WebData.track, WebData.artist


def current():
    try:
        if sys.platform.startswith("win"):
            return get_info_windows()
        elif sys.platform.startswith("darwin"):
            return get_info_mac()
        else:
            return get_info_linux()
    except SpotifyNotRunning as e:
        try:
            return get_info_web()
        except SpotifyClosed:
            raise e


def artist():
    return current()[1]


def song():
    return current()[0]
