from song import Song
from guest import Guest

song1 = Song("Iron Man", "Black Sabbath")
guest1 = Guest("Joni", 15, song1)

class Room:

    def __init__(self, input_room_name, input_capacity):
        self.room_name = input_room_name
        self.capacity = input_capacity
        self.guest_list = []
        self.playlist = []

    def add_to_playlist(self, song):
        self.playlist.append(song)

    def add_to_guest_list(self, guest):
        self.guest_list.append(guest)

    def view_guest_list(self):
        guest_inventory = []
        for guest in self.guest_list:
            guest_inventory.append(guest.name)
        return guest_inventory

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

set_up = Room("Sunset", 5)
print (set_up.room_name)

set_up.add_to_playlist(song1)
print(len(set_up.playlist))

set_up.add_to_guest_list(guest1)
print(len(set_up.guest_list))

print(set_up.view_guest_list())







