import sys
from SwSpotify import SpotifyNotRunning


def get_info_windows(return_status=False):
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
        raise SpotifyNotRunning

    # Local songs may only have a title field
    try:
        artist, track = windows[0].split(" - ", 1)
    except ValueError:
        artist = ''
        track = windows[0]

    # The window title is the default one when paused
    if windows[0] in ('Spotify Premium', 'Spotify Free'):
        is_playing = False
        artist = ''
        track = ''
    else:
        is_playing = True

    if return_status:
        return track, artist, is_playing
    else:
        return track, artist


def get_info_linux(return_status=False):
    """
    Uses the dbus API to get the data.
    """

    import dbus

    session_bus = dbus.SessionBus()
    try:
        spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                             "/org/mpris/MediaPlayer2")
    except dbus.exceptions.DBusException:
        raise SpotifyNotRunning
    spotify_properties = dbus.Interface(spotify_bus,
                                        "org.freedesktop.DBus.Properties")

    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player",
                                      "Metadata")
    track = str(metadata['xesam:title'])
    artist = str(metadata['xesam:artist'][0])
    if return_status:
        status = str(spotify_properties.Get("org.mpris.MediaPlayer2.Player",
                                            "PlaybackStatus"))
        is_playing = True if status.lower() == 'playing' else False
        return track, artist, is_playing
    else:
        return track, artist


def get_info_mac(return_status=False):
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

    s = NSAppleScript.alloc().initWithSource_(apple_script_code)
    x = s.executeAndReturnError_(None)
    a = str(x[0]).split('"')
    is_playing = True if a[5].lower() == 'playing' else False

    if return_status:
        return a[3], a[1], is_playing
    else:
        return a[3], a[1]


def current(return_status=False):
    if sys.platform.startswith("win"):
        return get_info_windows(return_status)
    elif sys.platform.startswith("darwin"):
        return get_info_mac(return_status)
    else:
        return get_info_linux(return_status)


def artist():
    return current()[1]


def song():
    return current()[0]


def is_playing():
    return current(return_status=True)[2]
