class WebData:
    track = ""
    artist = ""
    playState = ""

    @staticmethod
    def set_song(data):
        WebData.track = data['title']
        WebData.artist = data['artist']
        WebData.playState = data['playState']
