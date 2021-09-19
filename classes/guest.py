class Guest:

    def __init__ (self, input_name, input_wallet, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

    def pay_for_room(self, room):
        if room.check_before_add_to_guest_list(self) == "Welcome to the karaoke room":
            if self.wallet >= room.fee:
                self.wallet -= room.fee
                return "Payment successful"
        else:
            if room.check_before_add_to_guest_list(self) == "Sorry, room is currently full":
                return "Payment not taken, room full"
        return "Sorry, unable to take payment"


