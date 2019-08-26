import platform


def get_info_windows():
    import win32gui

    # Older Spotify versions - simply FindWindow for "SpotifyMainWindow"
    windows = [win32gui.GetWindowText(win32gui.FindWindow("SpotifyMainWindow", None))]

    # Newer Spotify versions - create an EnumHandler for EnumWindows and flood the list with Chrome_WidgetWin_0s
    def find_spotify_uwp(hwnd, windows):
        text = win32gui.GetWindowText(hwnd)
        if win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and len(text) > 0:
            windows.append(text)

    win32gui.EnumWindows(find_spotify_uwp, windows)

    while windows.count != 0:
        try:
            text = windows.pop()
        except:
            return None, None
        try:
            artist, track = text.split(" - ", 1)
            return track, artist
        except:
            pass


def get_info_linux():
    import dbus

    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    spotify_properties = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")
    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    track = str(metadata['xesam:title'])
    artist = str(metadata['xesam:artist'][0])
    return track, artist


def get_info_mac():
    from Foundation import NSAppleScript
    apple_script_code = """
    getCurrentlyPlayingTrack()
    on getCurrentlyPlayingTrack()
        tell application "Spotify"
            set currentArtist to artist of current track as string
            set currentTrack to name of current track as string
            return {currentArtist, currentTrack}
        end tell
    end getCurrentlyPlayingTrack
    """
    s = NSAppleScript.alloc().initWithSource_(apple_script_code)
    x = s.executeAndReturnError_(None)
    a = str(x[0]).split('"')
    return a[3], a[1]


def current():
    if platform.system() == "Windows":
        try:
            return get_info_windows()
        except:
            return None, None
    elif platform.system() == "Darwin":
        try:
            return get_info_mac()
        except:
            return None, None
    else:
        try:
            return get_info_linux()
        except:
            return None, None


def artist():
    return current()[1]


def song():
    return current()[0]
