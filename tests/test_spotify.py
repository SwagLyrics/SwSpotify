"""
Contains unit tests for spotify.py
"""
import platform
import unittest

from mock import patch

from SwSpotify import SpotifyNotRunning, SpotifyPaused, SpotifyClosed
from SwSpotify.spotify import song, artist, get_info_windows, get_info_web
from SwSpotify.spotify_web import run as server_run


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
    @patch('SwSpotify.spotify.sys')
    @patch('SwSpotify.spotify.get_info_linux', **{'return_value.raiseError.side_effect': SpotifyNotRunning})
    def test_that_artist_function_calls_get_info(self, mock, mock_sys, mock_no_native_spotify):
        """
        test that artist function calls get_info_web when native is not running.

        This works by mocking the get_info_linux which is called since we mock the platform as linux. NOTE that this
        would work on any platform I just mocked the platform to save mocking every get_info function with the
        SpotifyNotRunning error.

        This should cause the 'current' function to now run get_info_web due to the exception thrown.
        """
        mock_sys.platform = "Linux"
        artist()
        self.assertTrue(mock.called)

    @patch('SwSpotify.spotify.get_info_web')
    @patch('SwSpotify.spotify.sys')
    @patch('SwSpotify.spotify.get_info_linux', **{'return_value.raiseError.side_effect': SpotifyNotRunning})
    def test_that_song_function_calls_get_info(self, mock, mock_sys, mock_no_native_spotify):
        """
        test that artist function calls get_info_web when native is not running.

        This works by mocking the get_info_linux which is called since we mock the platform as linux. NOTE that this
        would work on any platform I just mocked the platform to save mocking every get_info function with the
        SpotifyNotRunning error.

        This should cause the 'current' function to now run get_info_web due to the exception thrown.
        """
        mock_sys.platform = "Linux"
        song()
        self.assertTrue(mock.called)

    @patch('SwSpotify.spotify_web.run', return_value=None)
    def test_get_info_web_returns_error_when_none(self, mock):
        """
        test that get_info_web raises SpotifyClosed when spotify_web.run returns None
        """
        self.assertRaises(SpotifyClosed, get_info_web)

    @patch('SwSpotify.spotify_web.run', return_value={"title": "Darkside", "artist": "Alan Walker"})
    def test_get_info_web_parse(self, mock):
        """
        test that get_info_web parses the dictionary correctly
        """
        x = get_info_web()
        self.assertEqual(x, ("Darkside", "Alan Walker"))

    @patch('SwSpotify.spotify.get_info_web')
    @patch('SwSpotify.spotify.get_info_linux', return_value=("some song", "some artist"))
    @patch('SwSpotify.spotify.get_info_windows', return_value=("some song", "some artist"))
    @patch('SwSpotify.spotify.get_info_mac', return_value=("some song", "some artist"))
    def test_get_info_web_not_called_if_native(self, mock, mock_sys, *mock_native_detected):
        """
        test that get_info_web is not called when there is a native alternative available.
        We mock the all the native get_info functions to return without raising a SpotifyNotRunning error and returning
        a supported value.
        """
        song()
        self.assertFalse(mock.called)

    @patch('SwSpotify.spotify_web.server')
    def test_run_function_calls_server(self, mock):
        """
        test that the server function is called by run
        """
        server_run()
        self.assertTrue(mock.called)

    @patch('SwSpotify.spotify_web.Server')
    def test_server_returns_null_if_no_data(self, mock_server):
        mock_server.data = {}
        result = server_run()
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
