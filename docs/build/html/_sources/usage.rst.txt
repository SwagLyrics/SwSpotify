.. _usage:

Usage
=====

Use it in your project by importing it as:

    from SwSpotify import spotify

Then you can access the song and artist as:

    >>> spotify.song()
    'Hello'
    >>> spotify.artist()
    'Adele'

Since mostly song and artist are used in conjunction, there is a current() method as well.

    >>> spotify.current()
    ('Hello', 'Adele')

This allows you to access song and artist by tuple unpacking as:

    >>> song, artist = spotify.current()

A SpotifyNotRunning Exception is raised if Spotify is closed or paused. SpotifyClosed and SpotifyPaused inherit from SpotifyNotRunning, meaning that you can catch both at the same time:

    try:
        title, artist = spotify.current()
    except SpotifyNotRunning as e:
        print(e)
    else:
        print(f"{title} - {artist}")

In case Spotify is closed or paused, that will automatically be reflected in the value of e.

For finer control you can catch SpotifyClosed and SpotifyPaused separately.


