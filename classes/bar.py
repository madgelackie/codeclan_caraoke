class Bar:
    
    def __init__(self, inputName):
        self.name = inputName
        self.total_takings = 0
        self.drinks = []
        self.room_inventory = []

    def add_room_to_inventory(self, room):
        self.room_inventory.append(room)

    def view_room_inventory(self):
        room_list = []
        for room in self.room_inventory:
            room_list.append(room.room_name)
        return room_list

    def combine_takings(self):
        for room in self.room_inventory:
            self.total_takings += room.takings
        return self.total_takings

