from item import LightSource

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
            message = available[0].on_take()
            if message:
                print(message)
            return f'{item_name} successfully taken!\n'

    def drop_item(self, item_name):
        available = [x for x in self.inventory if x.name == item_name]
        if not available:
            return "You don't have one of those!\n"
        else:
            self.room.add_item(available[0])

            message = available[0].on_drop()
            if message:
                print(message)

            for i in range(len(self.inventory)):
                if self.inventory[i].name == item_name:
                    self.inventory.pop(i)
                    break

            return "Done.\n"

    def display_items(self):
        if len(self.inventory) == 0:
            return "Items: none\n"
        else:
            item_names = [x.name for x in self.inventory]
            str_form = ", ".join(item_names)
            return f'Items: {str_form}'

    def can_see(self):
        if self.room.is_light:
            return True
        # for i in self.inventory if isinstance(i, LightSource):
        for i in self.inventory:
            if isinstance(i, LightSource):
                return True
        return False
    