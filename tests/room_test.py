import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Sunset", 1, 10)
        self.room2 = Room("Sunrise", 2, 15)
        self.song2 = Song("Fast Car", "Tracy Chapman")
        self.song3 = Song("All Star", "Smash Mouth")
        self.guest1 = Guest("Joni", 15, self.song3)
        self.guest2 = Guest("Frank", 35, self.song2)
        self.guest3 = Guest("Gem", 50, self.song3)

    def test_room_has_name(self):
        self.assertEqual("Sunset", self.room1.room_name)

    def test_room_has_capcity(self):
        self.assertEqual(1, self.room1.capacity)

    def test_room_has_empty_guest_list(self):
        self.assertEqual(0, len(self.room1.guest_list))

    def test_room_has_empty_playlist(self):
        self.assertEqual(0, len(self.room1.playlist))

    def test_add_song_to_playlist(self):
        self.room1.add_to_playlist(self.song3)
        self.assertEqual(1, len(self.room1.playlist))

    def test_can_add_guest_and_take_payment(self):
        self.assertEqual("Payment successful. Welcome to the karaoke room", self.room2.add_to_guest_list(self.guest1))

    def test_not_added_to_guest_list(self):
        self.room2.add_to_guest_list(self.guest1)
        self.room2.add_to_guest_list(self.guest2)
        self.assertEqual("Sorry, room is currently full", self.room2.add_to_guest_list(self.guest3))
        self.assertEqual(2, len(self.room2.guest_list))

    def test_payment_not_accepted(self):
        self.guest2.wallet = 5
        self.assertEqual("Unable to take payment", self.room2.add_to_guest_list(self.guest2))

    def test_remove_person_from_room(self):
        self.room1.add_to_guest_list(self.guest1)
        self.room1.remove_from_guest_list(self.guest1)
        self.assertEqual(0, len(self.room1.guest_list))








