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

```python
from SwSpotify import spotify
song = spotify.current_playing_song()
print(song.artist)
print(song.title)
```

If Spotify is not running, the SpotifyNotRunning exception is raised.

## Compiling SwSpotify for Development

- Clone the repo by `git clone https://github.com/SwagLyrics/SwSpotify.git` or use ssh.
- `cd` into the cloned repo.
- `pip install -e .` the -e flag installs it locally in editable mode.


## Contributing

Sure, improvements/fixes/issues everything is welcome :)
