class Room:

    def __init__(self, input_room_name, input_capacity, input_fee):
        self.room_name = input_room_name
        self.capacity = input_capacity
        self.guest_list = []
        self.playlist = []
        self.fee = input_fee
        self.takings = 0

    def add_to_playlist(self, song):
        self.playlist.append(song)

    def add_to_guest_list(self, guest):
        if len(self.guest_list) < self.capacity and guest.wallet >= self.fee:
            guest.reduce_wallet(self.fee)
            self.guest_list.append(guest)
            self.takings += self.fee
            return "Payment successful. Welcome to the karaoke room"
        if len(self.guest_list) >= self.capacity:
                return "Sorry, room is currently full"
        return "Unable to take payment"

    def remove_from_guest_list(self, guest):
        self.guest_list.remove(guest)

    def guest_list_length(self):
        return len(self.guest_list)

    # def take_payment(self, guest):
    #     # guest.pay_for_room(self, room)
    #     self.takings += self.fee
# how to charge customer, increase takings, ?need to include reduce customer wallet

 # guest.pay_for_room(self, room)











