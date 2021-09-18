class Guest:

    def __init__ (self, input_name, input_wallet, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

    def pay_for_room(self, room):
        if self.wallet >= room.fee:
            self.wallet -= room.fee
        return "Sorry, unable to take payment"


