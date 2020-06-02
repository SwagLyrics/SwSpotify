name = 'SwSpotify'
__version__ = '1.2.0'


class WebData:
    track = None
    artist = None
    playState = None

    @staticmethod
    def set_song(data):
        try:
            WebData.track = data['title']
            WebData.artist = data['artist']
            WebData.playState = data['playState']
        except KeyError:
            WebData.track = None
            WebData.artist = None
            WebData.playState = None


class SpotifyNotRunning(Exception):
    """
    Base exception raised if Spotify is not running i.e. is closed or paused.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, message="Spotify appears to be paused or closed at the moment."):
        super().__init__(message)


class SpotifyPaused(SpotifyNotRunning):

    def __init__(self, message="Spotify appears to be paused at the moment."):
        super().__init__(message)


class SpotifyClosed(SpotifyNotRunning):

    def __init__(self, message="Spotify appears to be closed at the moment."):
        super().__init__(message)
