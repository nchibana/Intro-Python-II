# Implement a class to hold item information.
# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.
import textwrap

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")

    def __str__(self):
       output = f"Item: {self.name}\n" + \
                 f"Description: {textwrap.fill(self.description, 50)}\n"

       return output