import unittest
from src.songs import Songs


class TestSongs(unittest.TestCase):
    def setUp(self):
        self.songs = Songs("I Will Survive", "Gloria Gaynor")
    
    def test_songs_has_a_title(self):
        self.assertEqual("I Will Survive", self.songs.title)

    def test_songs_has_a_artist(self):
        self.assertEqual("Gloria Gaynor", self.songs.artist)