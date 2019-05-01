# SwSpotify

SwSpotify is a python library to get the song and artist of the currently playing song from the Spotify application faster and without using the API. It works on Windows, Linux and macOS.

The original repository was [spotilib](https://github.com/XanderMJ/spotilib) which worked just for Windows and hasn't been updated since a long while when it broke on account of Spotify updating their application.

## Installation

Requires Python3. Use pip or pip3 depending on your installation.
```
pip install SwSpotify
```

## Usage

Use it in your project by importing it as:
```python
from SwSpotify import spotify
```
Then you can access the song and artist as:
```python
>>> spotify.song()
>>> spotify.artist()
```

## Compiling SwSpotify for Development

- Clone the repo by `git clone https://github.com/SwagLyrics/SwSpotify.git` or use ssh.
- `cd` into the cloned repo.
- `pip install -e .` the -e flag installs it locally in editable mode.


## Contributing

Sure, improvements/fixes/issues everything is welcome :)
