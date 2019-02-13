# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, start_room):
        self.room = start_room
        self.inventory = []