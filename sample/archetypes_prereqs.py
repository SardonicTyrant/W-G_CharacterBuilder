from constants import attributes

#Prerequisites needed to take an archetype
# Params:   Tier - minimum tier required
#           Species- species which can take this archetype
#           Attribute - a dictionary of the minimum required attributes
#           Skill - a dictionary of the minimum required skills
#           Other - a list of other required prereqs
class prereqs:


    def __int__(self, tier:int, species:str):
        self._tier = tier
        self._species = species

    def get_tier(self):
        return _tier

    def get_species(self):
        return _species

print(attributes.STRENGTH)
