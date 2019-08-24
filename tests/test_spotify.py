"""
Contains unit tests for spotify.py for linux
"""
import unittest
from collections import namedtuple
from SwSpotify.spotify import get_info_windows, current_playing_song, SpotifyNotRunning
from mock import mock, patch, Mock
import platform

Song = namedtuple('Song', ['title', 'artist'])


class LinuxTests(unittest.TestCase):
    """
    Unit tests for Linux
    """

    def setup(self):
        pass

    @patch('SwSpotify.spotify.get_info_linux')
    def test_that_current_playing_song_function_calls_get_info(self, mock):
        """
        test that test current_playing_song function calls get_info_linux function
        """
        x = current_playing_song()
        self.assertTrue(mock.called)

    @patch('SwSpotify.spotify.get_info_linux', side_effect=SpotifyNotRunning)
    def test_that_current_playing_song_function_raise_exception(self, mock):
        """
        test that test current_playing_song function raise SpotifyNotRunning when spotify is not running
        """
        self.assertRaises(SpotifyNotRunning, current_playing_song)


class WindowsTests(unittest.TestCase):
    """
    Unit tests for Windows
    """

    def setup(self):
        pass

    if platform.system() == "Windows":
        import win32gui

    @mock.patch('win32gui.GetWindowText', return_value='Alan Walker - Darkside')
    @mock.patch('win32gui.EnumWindows', return_value=None)
    def test_get_info_windows(self, mock_win32gui_1, mock_win32gui_2):
        """
        test that get_info_windows works
        """
        x = get_info_windows()
        self.assertEqual(x.artist, "Alan Walker")
        self.assertEqual(x.title, "Darkside")

    @patch('SwSpotify.spotify.get_info_windows')
    def test_that_current_playing_song_function_calls_get_info(self, mock):
        """
        test that test current_playing_song function calls get_info_windows function
        """
        x = current_playing_song()
        self.assertTrue(mock.called)

    @patch('SwSpotify.spotify.get_info_windows', side_effect=SpotifyNotRunning)
    def test_that_current_playing_song_function_raise_exception(self, mock):
        """
        test that test current_playing_song function raise SpotifyNotRunning when spotify is not running
        """
        self.assertRaises(SpotifyNotRunning, current_playing_song)


@mock.patch('platform.system', return_value='Darwin')
class DarwinTests(unittest.TestCase):
    """
    Unit tests for macOS
    """

    def setup(self, mock_os):
        pass

    @patch('SwSpotify.spotify.get_info_mac', side_effect=SpotifyNotRunning)
    def test_that_current_playing_song_function_raise_exception(self, mock, mock_os):
        """
        test that test current_playing_song function raise SpotifyNotRunning when spotify is not running
        """
        self.assertRaises(SpotifyNotRunning, current_playing_song)


if __name__ == '__main__':
    unittest.main()