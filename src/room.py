import textwrap

# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, char_line_limit):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.wrapper = textwrap.TextWrapper(char_line_limit)

    def __str__(self):
        wrapped = self.wrapper.fill(text=self.description)
        return f'{self.name}:\n{"-" * (len(self.name) + 1)}\n{wrapped}'

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        if len(self.items) == 0:
            return "Items: none"
        else:
            item_names = [x.name for x in self.items]
            str_form = ", ".join(item_names)
            wrapped = self.wrapper.fill(text=f'Items: {str_form}')
            return wrapped