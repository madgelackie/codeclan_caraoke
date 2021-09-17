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

    def guest_list_length(self):
        return len(self.guest_list)

    def check_before_add_to_guest_list(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)
            return "Welcome to the karaoke room"
        if len(self.guest_list) >= self.capacity:
            return "Sorry, room is currently full"












