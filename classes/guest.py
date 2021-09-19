class Guest:

    def __init__ (self, input_name, input_wallet, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def check_for_fav_song(self, room):
        for song in room.playlist:
            if self.favourite_song == song:
                return "Whoo, my favourite song!"




