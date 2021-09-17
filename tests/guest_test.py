import unittest
from classes.guest import Guest
from classes.song import Song


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Iron Man", "Black Sabbath")
        self.guest1 = Guest("Frank", 35, self.song1)
        self.guest2 = Guest("Joni", 15, self.song1)

    def test_guest_has_name(self):
        self.assertEqual("Joni", self.guest2.name)

    def test_guest_has_wallet(self):
        self.assertEqual(15, self.guest2.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Iron Man", self.guest2.favourite_song.title)
    