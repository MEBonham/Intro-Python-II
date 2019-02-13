
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        pass

    def on_drop(self):
        pass


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        return "It's not wise to drop your source of light!"