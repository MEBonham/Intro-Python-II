
class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def on_take(self):
        pass

    def on_drop(self):
        pass


class LightSource(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, value)

    def on_drop(self):
        return "It's not wise to drop your source of light!"