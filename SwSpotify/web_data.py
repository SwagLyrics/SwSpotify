class WebData:
    track = None
    artist = None
    playState = None

    @staticmethod
    def set_song(data):
        WebData.track = data['title']
        WebData.artist = data['artist']
        WebData.playState = data['playState']
