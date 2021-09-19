import unittest
from classes.guest import Guest
from classes.song import Song
from classes.room import Room


class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Iron Man", "Black Sabbath")
        self.song2 = Song("Fast Car", "Tracy Chapman")
        self.guest1 = Guest("Frank", 35, self.song2)
        self.guest2 = Guest("Joni", 15, self.song1)
        self.room1 = Room("Sunset", 1, 10)
        self.room2 = Room("Sunrise", 2, 15)

    def test_guest_has_name(self):
        self.assertEqual("Joni", self.guest2.name)

    def test_guest_has_wallet(self):
        self.assertEqual(15, self.guest2.wallet)

    def test_reduce_wallet(self):
        self.room2.add_to_guest_list(self.guest2)
        self.assertEqual(0, self.guest2.wallet)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Iron Man", self.guest2.favourite_song.title)

    def test_guest_favourite_song_in_room(self):
        self.room1.add_to_playlist(self.song1)
        self.room1.add_to_playlist(self.song2)
        self.room1.add_to_guest_list(self.guest1)
        self.assertEqual("Whoo, my favourite song!", self.guest2.check_for_fav_song(self.room1))

    

   
    