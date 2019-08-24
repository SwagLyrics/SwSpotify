import sys
from collections import namedtuple

if sys.platform == "win32":
    import win32gui
elif sys.platform == "linux":
    import pydbus
elif sys.platform == "darwin":
    from Foundation import NSAppleScript

Song = namedtuple('Song', ['artist', 'title'])


class SpotifyNotRunning(Exception):
    __module__ = Exception.__module__

    def __init__(self, message=None):
        super(SpotifyNotRunning, self).__init__(message)


def get_info_windows():
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
        except IndexError:
            raise SpotifyNotRunning('Spotify is not running')
        try:
            artist, track = text.split(" - ", 1)
            return Song(artist, track)
        except:
            pass


def get_info_linux():
    bus = pydbus.SessionBus()
    player = bus.get('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
    track = str(player.Metadata['xesam:title'])
    artist = str(player.Metadata['xesam:artist'][0])
    return Song(artist, track)


def get_info_mac():
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
    return Song(a[1], a[3])


def current_playing_song():
    if sys.platform == "win32":
        return get_info_windows()
    elif sys.platform == "darwin":
        try:
            return get_info_mac()
        except:
            raise SpotifyNotRunning('Spotify is not running')
    else:
        try:
            return get_info_linux()
        except:
            raise SpotifyNotRunning('Spotify is not running')
