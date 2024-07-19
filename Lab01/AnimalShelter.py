from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.shelter = {}

    def addAnimal(self, animal):
        species = animal.species
        if species not in self.shelter:
            self.shelter[species] = []
        self.shelter[species].append(animal)

    def removeAnimal(self, animal):
        species = animal.species
        if species in self.shelter:
            for i, a in enumerate(self.shelter[species]):
                if (a.species == animal.species and a.name == animal.name and 
                    a.age == animal.age and a.weight == animal.weight):
                    del self.shelter[species][i]
                    if not self.shelter[species]: 
                        del self.shelter[species]
                    return True
        return False

    def removeSpecies(self, species):
        species = species.upper()
        if species in self.shelter:
            del self.shelter[species]

    def getAnimalsBySpecies(self, species):
        species = species.upper()
        if species in self.shelter:
            return "\n".join(animal.toString() for animal in self.shelter[species])
        return ""

    def doesAnimalExist(self, animal):
        species = animal.species
        if species in self.shelter:
            for a in self.shelter[species]:
                if (a.species == animal.species and a.name == animal.name and 
                    a.age == animal.age and a.weight == animal.weight):
                    return True
        return False




