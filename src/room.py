# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __getitem__(self, index):
        return getattr(self,index)

    def __str__(self):
        return str(self.name, self.description)
