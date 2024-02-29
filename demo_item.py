class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.location = None
    
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    
    def get_description(self):
        return self.description
    def set_description(self, new_description):
        self.description = new_description

    def get_details(self):
        print(self.name)
        print('---------------------')
        print(self.description)
        print(self.location)

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

class Key(Item):
    def __init__ (self, item_name):
        super(). __init__(item_name)

class Sword(Item):
    def __init__ (self, item_name):
        super(). __init__ (item_name)