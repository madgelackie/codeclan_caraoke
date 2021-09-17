
class Song:

    def __init__ (self, input_title, input_artist):
        self.title = input_title
        self.artist = input_artist

class Guest:

    def __init__ (self, input_name, input_wallet, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song        


song2 = Song("Fast Car", "Tracy Chapman")
song3 = Song("All Star", "Smash Mouth")
guest1 = Guest("Joni", 32, song3)
guest2 = Guest("Frank", 35, song2)
guest3 = Guest("Gem", 50, song3)

song1 = Song("Iron Man", "Black Sabbath")


class Room:

    def __init__(self, input_room_name, input_capacity):
        self.room_name = input_room_name
        self.capacity = input_capacity
        self.guest_list = []
        self.playlist = []

    def add_to_playlist(self, song):
        self.playlist.append(song)

    def add_to_guest_list(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)
            return "Welcome to the karaoke room"
        if len(self.guest_list) >= self.capacity:
            return "Sorry, room is currently full"

    def view_guest_list(self):
        guest_inventory = []
        for guest in self.guest_list:
            guest_inventory.append(guest.name)
        return guest_inventory

    def can_add_guest(self):
        if len(self.guest_list) < self.capacity:
            return True
        return False

    # def updated_add_to_room(self, guest):
    #     if self.can_add_guest() == True:
    #         self.guest_list.append(guest)
    #         return len(self.guest_list)
    #     return "sorry, room full at the moment"

party_room = Room("Sunset", 2)
party_room.add_to_guest_list(guest1)
party_room.add_to_guest_list(guest2)
print(party_room.add_to_guest_list(guest3))

# print(len(party_room.guest_list))


# # One guest already added to list, is there space to add another?
# party_room.add_to_guest_list(guest2)
# print(party_room.updated_add_to_room(guest3))



# set_up = Room("Sunset", 5)
# print (set_up.room_name)

# set_up.add_to_playlist(song1)
# print(len(set_up.playlist))

# set_up.add_to_guest_list(guest1)
# print(len(set_up.guest_list))

# print(set_up.view_guest_list())

 # def view_guest_list(self):
    #     guest_inventory = []
    #     for guest in self.guest_list:
    #         guest_inventory.append(guest.name)
    #     return guest_inventory   

    # def check_if_guest_in_room(self, guest):
    #     for guest in self.guest_list:
    #         if guest.name == guest:
    #             return True
    #         return False

    # def check_if_guest_in_room(self, guest):
    #     guest_list_names = []
    #     for guest in self.guest_list:
    #         guest_list_names.append(guest.name)
    #     return guest_list_names

#     def check_playlist_by_title(self):
#         list_by_title = []
#         for song in playlist:
#             list_by_title.append(song.title)
#         return list_by_title

    # def test_see_who_is_in_room(self):
    #     self.room1.add_to_guest_list(self.guest1)
    #     self.assertEqual(["Joni"], self.room1.check_if_guest_in_room("Joni"))

    # def test_check_playlist_by_title(self):
    #     self.room1.add_to_playlist(self.song3)
    #     self.assertEqual("All Star", self.room1.playlist.title)        




