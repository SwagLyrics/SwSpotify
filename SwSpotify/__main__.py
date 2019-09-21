from . import spotify


def main():
    title, artist, is_playing = spotify.current(return_status=True)
    if is_playing:
        print(f"{title} - {artist}")
    else:
        print("Spotify is paused")


if __name__ == '__main__':
    main()
