from SwSpotify import spotify, SpotifyNotRunning


def main():
    try:
        title, artist = spotify.current()
    except SpotifyNotRunning as e:
        print(e)
    else:
        print(f"{title} - {artist}")


if __name__ == '__main__':
    main()
