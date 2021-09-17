import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Iron Man", "Black Sabbath")
        self.song2 = Song("Fast Car", "Tracy Chapman")
        self.song3 = Song("All Star", "Smash Mouth")
    
    def test_song_has_title(self):
        self.assertEqual("Iron Man", self.song1.title)

    def test_song_has_artist(self):
        self.assertEqual("Black Sabbath", self.song1.artist)

