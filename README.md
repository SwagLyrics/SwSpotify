# SwSpotify

[![Discord Server](https://badgen.net/badge/discord/join%20chat/7289DA?icon=discord)](https://discord.gg/DSUZGK4)
[![Test](https://github.com/SwagLyrics/SwSpotify/actions/workflows/tests.yml/badge.svg)](https://github.com/SwagLyrics/SwSpotify/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/SwagLyrics/SwSpotify/branch/master/graph/badge.svg)](https://codecov.io/gh/SwagLyrics/SwSpotify)
![PyPI](https://img.shields.io/pypi/v/swspotify.svg)
[![Downloads](https://pepy.tech/badge/swspotify)](https://pepy.tech/project/swspotify)

SwSpotify is a Python library to get the song and artist of the currently playing song from the Spotify application faster and without using the API. It works on Windows, Linux, macOS and even the Spotify Web Player! 🥳

In order to add support for the Spotify Web Player, the [SwagLyrics Chrome Extension](https://chrome.google.com/webstore/detail/swaglyrics-for-spotify/miopldoofdhmipepmnclnoangcdffmlk) needs to be installed. We have plans to extend this for other browsers as well.

If you're a developer using SwSpotify, you can direct your end users to install the extension to automatically make your application work with the Spotify Web Player. The source of the Chrome Extension is open sourced at https://github.com/SwagLyrics/SwagLyrics-Chrome-Extension.

The original repository was [spotilib](https://github.com/XanderMJ/spotilib) which worked just for Windows and hasn't been updated since a long while when it broke on account of Spotify updating their application.

Originally made for use in [SwagLyrics for Spotify](https://github.com/SwagLyrics/SwagLyrics-For-Spotify).

## Installation

Requires Python3. Use pip or pip3 depending on your installation. You might want to use the `--user` flag on Linux to
avoid using pip as root.

```shell
pip install SwSpotify
```

For linux you need `dbus` which is usually pre-installed.

## Usage

Use it in your project by importing it as:

```py
from SwSpotify import spotify
```

Then you can access the song and artist as:

```py
>>> spotify.song()
'Hello'
>>> spotify.artist()
'Adele'
```

Since mostly song and artist are used in conjunction, there is a `current()` method as well.

```py
>>> spotify.current()
('Hello', 'Adele')
```

This allows you to access song and artist by tuple unpacking as:

```py
>>> song, artist = spotify.current()
```

A `SpotifyNotRunning` Exception is raised if Spotify is closed or paused. `SpotifyClosed` and `SpotifyPaused` inherit from `SpotifyNotRunning`, meaning that you can catch both at the same time:

```py
try:
    title, artist = spotify.current()
except SpotifyNotRunning as e:
    print(e)
else:
    print(f"{title} - {artist}")
```

In case Spotify is closed or paused, that will automatically be reflected in the value of `e`.

For finer control you can catch `SpotifyClosed` and `SpotifyPaused` separately.

## Compiling SwSpotify for Development

- Clone the repo by `git clone https://github.com/SwagLyrics/SwSpotify.git` or use ssh.
- `cd` into the cloned repo.
- `pip install -e .` the -e flag installs it locally in editable mode.

## Contributing

Sure, improvements/fixes/issues everything is welcome :)
