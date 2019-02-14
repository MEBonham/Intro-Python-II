# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, naturally_lit):
        self.name = name
        self.description = description
        self.is_light = naturally_lit
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f'{self.name}:\n{"-" * (len(self.name) + 1)}\n{self.description}'

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items.reverse()   # All the reverses are just to make it so you'll take the last item if there are duplicates
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                self.items.pop(i)
                break
        self.items.reverse()

    def display_items(self):
        if len(self.items) == 0:
            return "Items: none"
        else:
            item_names = [x.name for x in self.items]
            str_form = ", ".join(item_names)
            return f'Items: {str_form}'


class Store(Room):
    def __init__(self, name, description, naturally_lit):
        super().__init__(name, description, naturally_lit)
        
