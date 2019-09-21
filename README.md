# SwSpotify

[![Build Status](https://travis-ci.com/SwagLyrics/SwSpotify.svg?branch=master)](https://travis-ci.com/SwagLyrics/SwSpotify)
[![Build status](https://ci.appveyor.com/api/projects/status/c8heviwe9q2m8lb0?svg=true)](https://ci.appveyor.com/project/TheClashster/swspotify)
[![codecov](https://codecov.io/gh/SwagLyrics/SwSpotify/branch/master/graph/badge.svg)](https://codecov.io/gh/SwagLyrics/SwSpotify)
![PyPI](https://img.shields.io/pypi/v/swspotify.svg)
[![Downloads](https://pepy.tech/badge/swspotify)](https://pepy.tech/project/swspotify)

SwSpotify is a python library to get the song and artist of the currently playing song from the Spotify application faster and without using the API. It works on Windows, Linux and macOS. 

The original repository was [spotilib](https://github.com/XanderMJ/spotilib) which worked just for Windows and hasn't been updated since a long while when it broke on account of Spotify updating their application.

Originally made for use in [SwagLyrics for Spotify](https://github.com/SwagLyrics/SwagLyrics-For-Spotify).

## Installation

Requires Python3. Use pip or pip3 depending on your installation.
```
pip install SwSpotify
```

## Usage

Use it in your project by importing it as:
```pydocstring
from SwSpotify import spotify
```
Then you can access the song and artist as:
```pydocstring
>>> spotify.song()
'Hello'
>>> spotify.artist()
'Adele'
>>> spotify.is_playing()
True
```
Since mostly song and artist are used in conjunction, there is a `current()` method as well.
```pydocstring
>>> spotify.current()
('Hello', 'Adele')
```
or you can pass `return_status=True` to also get whether it's playing or not.
```pydocstring
>>> spotify.current(return_status=True)
('Hello', 'Adele', True)
```
This allows you to access song and artist by tuple unpacking as:
```pydocstring
>>> song, artist = spotify.current()
>>> song, artist, is_playing = spotify.current(return_status=True)
```

If Spotify is not running or is paused, a `SpotifyNotRunning` Exception is raised.
## Compiling SwSpotify for Development

- Clone the repo by `git clone https://github.com/SwagLyrics/SwSpotify.git` or use ssh.
- `cd` into the cloned repo.
- `pip install -e .` the -e flag installs it locally in editable mode.


## Contributing

Sure, improvements/fixes/issues everything is welcome :)
