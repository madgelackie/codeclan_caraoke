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

    def remove_from_guest_list(self, guest):
        self.guest_list.remove(guest)

    # def view_guest_list(self):
    #     guest_inventory = []
    #     for guest in self.guest_list:
    #         guest_inventory.append(guest.name)
    #     return guest_inventory

 







