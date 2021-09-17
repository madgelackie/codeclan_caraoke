import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Sunset", 5)
        self.room2 = Room("Sunrise", 6)
        self.song3 = Song("All Star", "Smash Mouth")

    def test_room_has_name(self):
        self.assertEqual("Sunset", self.room1.room_name)

    def test_room_has_capcity(self):
        self.assertEqual(5, self.room1.capacity)

    def test_room_has_empty_guest_list(self):
        self.assertEqual(0, len(self.room1.guest_list))

    def test_room_has_empty_playlist(self):
        self.assertEqual(0, len(self.room1.playlist))

    def test_add_song_to_playlist(self):
        self.room1.add_to_playlist(self.song3)
        self.assertEqual(1, len(self.room1.playlist))

    # def test_check_playlist_by_title(self):
    #     self.room1.add_to_playlist(self.song3)
    #     self.assertEqual("All Star", self.room1.playlist.title)        


