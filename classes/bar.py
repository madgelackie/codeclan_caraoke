# from room import *
# from guest import *
# from song import *

# room1 = Room("Sunset", 1, 10)
# room2 = Room("Sunrise", 2, 15)
# song2 = Song("Fast Car", "Tracy Chapman")
# song3 = Song("All Star", "Smash Mouth")
# guest1 = Guest("Joni", 32, song3)
# guest2 = Guest("Frank", 35, song2)
# guest3 = Guest("Gem", 50, song3)

class Bar:
    
    def __init__(self, inputName):
        self.name = inputName
        self.total_takings = 0
        self.drinks = []
        self.room_inventory = []

    def add_room_to_inventory(self, room):
        self.room_inventory.append(room)

    def view_room_inventory(self):
        room_list = []
        for room in self.room_inventory:
            room_list.append(room.room_name)
        return room_list

    def combine_takings(self):
        for room in self.room_inventory:
            self.total_takings += room.takings
        return self.total_takings

# bar1 = Bar("CheekyTiki")
# # print(bar1.name)

# # print(room1.room_name)

# bar1.add_room_to_inventory(room1)
# bar1.add_room_to_inventory(room2)

# room1.add_to_guest_list(guest1)
# print(room1.takings)

# room2.add_to_guest_list(guest2)
# print(room2.takings)

# print(bar1.view_room_inventory())
# print(bar1.combine_takings())