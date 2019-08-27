name = 'SwSpotify'
__version__ = '1.0.0'


class SpotifyNotRunning(Exception):
    """Exception raised if Spotify is not running or is paused.

        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
        """

    def __init__(self, message="Spotify doesn't appear to be playing at the moment."):
        super().__init__(message)
