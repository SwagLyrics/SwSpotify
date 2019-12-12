"""
Contains unit tests for spotify.py
"""
import platform
import unittest

from mock import patch

from SwSpotify import SpotifyNotRunning, SpotifyPaused
from SwSpotify.spotify import song, artist, get_info_windows, get_info_web


class LinuxTests(unittest.TestCase):
    """
    Unit tests for Linux
    """

    def setup(self):
        pass

    @patch('SwSpotify.spotify.get_info_linux')
    def test_that_artist_function_calls_get_info(self, mock):
        """
        test that test artist function calls get_info_linux function
        """
        x = artist()
        self.assertTrue(mock.called)

    @patch('SwSpotify.spotify.get_info_linux')
    def test_that_song_function_calls_get_info(self, mock):
        """
        test that test song function calls get_info_linux function
        """
        x = song()
        self.assertTrue(mock.called)

    @patch('dbus.SessionBus')
    @patch('dbus.Interface')
    def test_that_artist_function_returns_None_when_error(self, mock, mock_bus):
        """
        test that test artist function raises SpotifyNotRunning when the get_info_linux function will return an error
        """
        from dbus.exceptions import DBusException
        mock.side_effect = DBusException
        x = artist
        self.assertRaises(SpotifyNotRunning, x)

    @patch('dbus.SessionBus')
    @patch('dbus.Interface')
    def test_that_song_function_returns_None_when_error(self, mock, mock_bus):
        """
        test that test song function raises SpotifyNotRunning when the get_info_linux function will return an error
        """
        from dbus.exceptions import DBusException
        mock.side_effect = DBusException
        x = song
        self.assertRaises(SpotifyNotRunning, x)


class WindowsTests(unittest.TestCase):
    """
    Unit tests for Windows
    """

    def setup(self):
        pass

    if platform.system() == "Windows":
        pass

    @patch('win32gui.GetWindowText', return_value='Alan Walker - Darkside')
    @patch('win32gui.EnumWindows', return_value=None)
    def test_get_info_windows(self, mock_win32gui_1, mock_win32gui_2):
        """
        test that get_info_windows works
        """
        x = get_info_windows()
        self.assertEqual(x, ("Darkside", "Alan Walker"))

    @patch('SwSpotify.spotify.get_info_windows')
    def test_that_artist_function_calls_get_info(self, mock):
        """
        test that test artist function calls get_info_windows function
        """
        x = artist()
        self.assertTrue(mock.called)

    @patch('SwSpotify.spotify.get_info_windows')
    def test_that_song_function_calls_get_info(self, mock):
        """
        test that test song function calls get_info_windows function
        """
        x = song()
        self.assertTrue(mock.called)

    # @patch('SwSpotify.spotify.get_info_windows', side_effect=ValueError)
    # def test_that_artist_function_returns_None_when_error(self, mock):
    #     """
    #     test that test artist function returns None when the get_info_windows function will return an error
    #     """
    #     self.assertRaises(SpotifyNotRunning, artist)

    @patch('win32gui.GetWindowText', return_value='Spotify Free')
    def test_that_artist_function_raises_exception_when_spotify_paused(self, mock_window):
        """
        test that artist raise SpotifyPaused
        """
        self.assertRaises(SpotifyNotRunning, artist)

    # @patch('SwSpotify.spotify.get_info_windows', side_effect=ValueError)
    # def test_that_song_function_returns_None_when_error(self, mock):
    #     """
    #     test that test song function returns None when the get_info_windows function will return an error
    #     """
    #     self.assertRaises(SpotifyNotRunning, song)

    @patch('win32gui.GetWindowText', return_value='Spotify Free')
    def test_that_song_function_raises_exception_when_spotify_paused(self, mock_window):
        """
        test that song can raise SpotifyPaused
        """
        self.assertRaises(SpotifyPaused, song)

    @patch('win32gui.GetWindowText', return_value='Shawn Mendes - Youth (feat. Khalid)')
    def test_that_get_info_windows_works_for_old_spotify(self, mock_window):
        """
        test that get_info_windows parses song, artist correctly from the Spotify window
        """
        song, artist = get_info_windows()
        self.assertEqual(song, 'Youth (feat. Khalid)')
        self.assertEqual(artist, 'Shawn Mendes')

    @patch('win32gui.GetWindowText')
    @patch('win32gui.GetClassName', return_value="Chrome_WidgetWin_0")
    def test_that_get_info_windows_works_for_new_spotify(self, mock_window_class, mock_window_text):
        """
        test that get_info_windows parses song, artist correctly from the Spotify window
        """
        def w_text():
            yield ''
            while True:
                yield 'Adele - Hello'
        window_text = w_text()
        mock_window_text.side_effect = window_text

        song, artist = get_info_windows()
        self.assertEqual(song, 'Hello')
        self.assertEqual(artist, 'Adele')


class DarwinTests(unittest.TestCase):
    """
    Unit tests for macOS
    """

    def setup(self):
        pass

    @patch('SwSpotify.spotify.get_info_mac')
    def test_that_artist_function_calls_get_info(self, mock):
        """
        test that test artist function calls get_info_mac function
        """
        x = artist()
        self.assertTrue(mock.called)

    @patch('SwSpotify.spotify.get_info_mac')
    def test_that_song_function_calls_get_info(self, mock):
        """
        test that test song function calls get_info_mac function
        """
        x = song()
        self.assertTrue(mock.called)

    def test_that_artist_function_returns_None_when_error(self):
        """
        test that test artist function returns None when the get_info_mac function will return an error
        """
        x = artist
        self.assertRaises(SpotifyNotRunning, x)

    def test_that_song_function_returns_None_when_error(self):
        """
        test that test song function returns None when the get_info_mac function will return an error
        """
        x = song
        self.assertRaises(SpotifyNotRunning, x)


class WebTests(unittest.TestCase):
    """
    Unit tests for Chrome (with extension) for spotify web player
    """

    def setup(self):
        pass

    @patch('SwSpotify.spotify.get_info_web')
    def test_that_artist_function_calls_get_info(self, mock):
        """
        test that test artist function calls get_info_chrome function
        """
        x = artist()
        self.assertTrue(mock.called)

    @patch('SwSpotify.spotify.get_info_web')
    def test_that_song_function_calls_get_info(self, mock):
        """
        test that test song function calls get_info_web function
        """
        x = song()
        self.assertTrue(mock.called)

    def test_that_song_function_returns_None_when_error(self):
        """
        test that test song function returns None when the get_info_web function will return an error
        """
        x = song
        self.assertRaises(SpotifyNotRunning, x)

    @patch('spotify_web.run', return_value={"title": "Darkside", "artist": "Alan Walker"})
    def test_get_info_web(self, mock_spotify_web):
        """
        test that get_info_web works
        """
        x = get_info_web()
        self.assertEqual(x, ("Darkside", "Alan Walker"))


if __name__ == '__main__':
    unittest.main()
