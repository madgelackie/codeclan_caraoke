# from song import Song

# song1 = Song("Iron Man", "Black Sabbath", 3)

class Room:

    def __init__(self, input_room_name, input_capacity):
        self.room_name = input_room_name
        self.capacity = input_capacity
        self.guest_list = []
        self.playlist = []

    def add_to_playlist(self, song):
        self.playlist.append(song)

    # def check_playlist_by_title(self):
    #     list_by_title = []
    #     for song in playlist:
    #         list_by_title.append(song.title)
    #     return list_by_title

# set_up = Room("Sunset", 5)
# set_up.add_to_playlist(song1)
# check = set_up.check_playlist_by_title
# print(check)



