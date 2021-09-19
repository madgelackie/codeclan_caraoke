class Song:

    def __init__ (self, input_title, input_artist):
        self.title = input_title
        self.artist = input_artist

class Room:

    def __init__(self, input_room_name, input_capacity, input_fee):
        self.room_name = input_room_name
        self.capacity = input_capacity
        self.guest_list = []
        self.playlist = []
        self.fee = input_fee
        self.takings = 0


    def check_before_add_to_guest_list(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)
            return "Welcome to the karaoke room"
        if len(self.guest_list) >= self.capacity:
            return "Sorry, room is currently full"

# # song1 = Song("Iron Man", "Black Sabbath")
# song2 = Song("Fast Car", "Tracy Chapman")
song3 = Song("All Star", "Smash Mouth")
# guest1 = Guest("Joni", 32, song3)
# guest2 = Guest("Frank", 35, song2)
# guest3 = Guest("Gem", 50, song3)
# room1 = Room("Sunset", 1, 10)
# room2 = Room("Sunrise", 2, 15)

class Guest:

    def __init__ (self, input_name, input_wallet, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

# test = Guest("gemma", 50, song1)
# print(test.favourite_song.title)


    def pay_for_room(self, room):
        if room.check_before_add_to_guest_list(self) == "Welcome to the karaoke room":
            if self.wallet >= room.fee:
                self.wallet -= room.fee
                return "Payment successful"
        else:
            if room.check_before_add_to_guest_list(self) == "Sorry, room is currently full":
                return "Payment not taken, room full"
        return "Sorry, unable to take payment"

testGuest = Guest("Joni", 7, song3)
testRoom = Room("Sunset", 2, 10)

# print(len(testRoom.guest_list))

print(testGuest.pay_for_room(testRoom))
# print (len(testRoom.guest_list))

# testGuest2 = Guest("Grunk", 40, song3)

# print(testGuest2.pay_for_room(testRoom))
# print(len(testRoom.guest_list))