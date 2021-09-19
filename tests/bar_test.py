import unittest
from classes.bar import Bar
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestBar(unittest.TestCase):
    
    def setUp(self):
        self.bar1 = Bar("CheekyTiki")
        self.room1 = Room("Sunset", 1, 10)
        self.room2 = Room("Sunrise", 2, 15)
        self.song2 = Song("Fast Car", "Tracy Chapman")
        self.song3 = Song("All Star", "Smash Mouth")
        self.guest1 = Guest("Joni", 15, self.song3)
        self.guest2 = Guest("Frank", 35, self.song2)

    def test_bar_has_name(self):
        self.assertEqual("CheekyTiki", self.bar1.name)

    def test_bar_has_takings(self):
        self.assertEqual(0, self.bar1.total_takings)

    def test_bar_has_room_inventory(self):
        self.bar1.room_inventory.append(self.room1)
        self.bar1.room_inventory.append(self.room2)
        self.assertEqual(2, len(self.bar1.room_inventory))

    def test_view_room_inventory(self):
        self.bar1.room_inventory.append(self.room1)
        self.bar1.room_inventory.append(self.room2)
        self.assertEqual(["Sunset", "Sunrise"], self.bar1.view_room_inventory())

    def test_combine_takings(self):
        self.bar1.add_room_to_inventory(self.room1)
        self.bar1.add_room_to_inventory(self.room2)
        self.room1.add_to_guest_list(self.guest1)
        self.room2.add_to_guest_list(self.guest2)
        self.assertEqual(10, self.room1.takings)
        self.assertEqual(15, self.room2.takings)
        self.assertEqual(25, self.bar1.combine_takings())
        