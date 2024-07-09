import json


class SongInfo:
    def __init__(self, title: str, artist: str, album: str) -> None:
        self.title = title
        self.artist = artist
        self.album = album


def song_info_from_json(json: dict) -> SongInfo:
    return SongInfo(json["title"], json["artist"], json["album"])