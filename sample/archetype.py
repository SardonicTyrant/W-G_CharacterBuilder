from archetype_benefits import Benefits
from archetype_prereqs import Prereqs

class Archetype:

    def __init__(self, name:str, prereqs:Prereqs, benefits:Benefits):
        self._name = name
        self._prereqs = prereqs
        self._benefits = benefits

    def get_name(self)->str:
        return self._name

    def get_prerequisites(self)->Prereqs:
        return self._prereqs

    def get_benefits(self)->Benefits:
        return self._benefits
