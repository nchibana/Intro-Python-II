# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room:
    def __init__(self, name, description, items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    def __str__(self):
        output = f"Current room: {self.name}\n" + \
                 f"Description: {textwrap.fill(self.description, 50)}\n" + \
                 f"Items in room:"

        for i in self.items:
            output += f"\n\tItem: {i.name}\n\tDescription: {i.description}"

        return output
                 
                
