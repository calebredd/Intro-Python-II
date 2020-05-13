# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    def __getitem__(self, index):
        return getattr(self,index)
    def __setitem__(self, index, newValue):
        if(index == 'room'):
            self.room = newValue
    def __str__(self):
        return str(self.name, self.room)
    def move(self, newRoom):
        self.__setitem__("room", newRoom)
