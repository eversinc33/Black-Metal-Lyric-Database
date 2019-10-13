from typing import List
from classes.song import Song

class Album(object):
    def __init__(self):
        self.name: str = ""
        self.released_by: str = ""
        self.release_year: str = ""
        self.songs: List[Song] = []
