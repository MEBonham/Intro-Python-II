# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, start_room):
        self.room = start_room
        self.inventory = []

    def take_item(self, item_name):
        available = [x for x in self.room.items if x.name == item_name]
        if not available:
            return "That item is not available to take.\n"
        else:
            self.inventory.append(available[0])
            self.room.remove_item(item_name)
            return f'{item_name} successfully taken!\n'