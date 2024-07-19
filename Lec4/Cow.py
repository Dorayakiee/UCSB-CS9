# Cow.py

from Animal import Animal

class Cow(Animal):
    
    def __init__(self, species=None, name=None, sound=None):
        super().__init__(species, name)
        #Animal.__init__(self, species, name) # also works
        self.sound = sound
    
    def setSound(self, sound):
        self.sound = sound

    #def getSound(self):
    #    return f"{self.sound}!!"

    def getSound(self):
        s = "Using Super class getSound method!\n"
        s += Animal.getSound(self)
        s += "\n"
        s += "Extending it with our own getSound functionality\n"
        s += f"{self.sound}!!"
        return s