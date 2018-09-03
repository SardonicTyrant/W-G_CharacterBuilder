from archetype import Archetype
from species import Species

class Character:

    def __init__ (self, name:str="", species:Species=None, archetype:Archetype=None):
        self._name = name
        self._species = species
        self._archetype = archetype

        def get_name(self)->str:
            return self._names
