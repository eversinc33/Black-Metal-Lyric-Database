from typing import List
from classes.album import Album

class Artist(object):
    def __init__(self):
        self.name: str = ""
        self.country: str = "Unknown"
        self.releases: List[Album] = []
        self.current_label: str = ""
