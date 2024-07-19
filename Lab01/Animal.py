class Animal:
    def __init__(self, species = None, weight = None, age = None, name = None):
        self.species = species.upper() if species else None
        self.weight = weight
        self.age = age
        self.name = name.upper() if name else None
        
    def setSpecies(self, species):
        self.species = species.upper() if species else None
    
    def setWeight(self, weight):
        self.weight = weight
    
    def setAge(self, age):
        self.age = age
        
    def setName(self, name):
        self.name = name.upper() if name else None
        
    def toString(self):
        return f"Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}"

