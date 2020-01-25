# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap

class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def get_name(self):
        return self.name
    
    def get_current_room(self):
        return self.current_room

    def __str__(self):
        output = f"Player's items:"

        if len(self.items) > 0:
            for i in self.items:
                output += f"\n\t{i}"
        else:
            output = "You have no items."

        return output
