from random import randint
from item import LightSource
from room import Store

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, start_room):
        self.room = start_room
        self.inventory = []
        self.wealth = 2

    def try_take_item(self, item_name):
        if not self.can_see():
            return "Good luck finding that in the dark!\n"
        else:
            available = [x for x in self.room.items if x.name == item_name]
            if not available:
                return "That item is not available to take.\n"
            elif isinstance(self.room, Store):
                return "Stealing isn't THAT easy.\n"
            else:
                return self.take_item(item_name, available[0])

    def take_item(self, item_name, item):
        self.inventory.append(item)
        self.room.remove_item(item_name)
        message = item.on_take()
        if message:
            print(message)
        return f'{item_name} successfully taken!\n'

    def try_buy_item(self, item_name):
        if not self.can_see():
            return "Good luck finding that in the dark!\n"
        elif not isinstance(self.room, Store):
            return "You can't buy stuff here!\n"
        else:
            available = [x for x in self.room.items if x.name == item_name]
            if not available:
                return "The store doesn't have that.\n"
            else:
                


    def try_drop_item(self, item_name):
        available = [x for x in self.inventory if x.name == item_name]
        if not available:
            return "You don't have one of those!\n"
        elif isinstance(self.room, Store):
            return "You can't just leave that here, but you can try to sell it.\n"
        else:
            return self.drop_item(item_name, available[0])

    def drop_item(self, item_name, item):
        self.room.add_item(item)

        message = item.on_drop()
        if message:
            print(message)

        for i in range(len(self.inventory)):
            if self.inventory[i].name == item_name:
                self.inventory.pop(i)
                break

        return "Done.\n"

    def try_sell_item(self, item_name):
        available = [x for x in self.inventory if x.name == item_name]
        if not available:
            return "You don't have one of those!\n"
        elif not isinstance(self.room, Store):
            return "You can't sell that here!\n"
        else:
            self.boost_wealth(available[0].value)
            self.drop_item(item_name, available[0])
            return "Thank you for your business!\n"

    def display_items(self):
        if len(self.inventory) == 0:
            return f"Wealth: {self.wealth}\nItems: none"
        else:
            item_names = [x.name for x in self.inventory]
            str_form = ", ".join(item_names)
            return f'Wealth: {self.wealth}\nItems: {str_form}'

    def can_see(self):
        if self.room.is_light:
            return True
        for i in self.inventory:
            if isinstance(i, LightSource):
                return True
        return False
    
    def boost_wealth(self, value):
        rolled_total = 0
        for i in range(self.wealth):
            if randint(1, 6) > 4:
                rolled_total += 1
        if value > rolled_total:
            self.wealth += (value - rolled_total)