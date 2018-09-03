
class Benefits:

    def __init__(self, keywords:set, influence:int, abilities: set, wargear: set):
        self._keywords = _keywords
        self._influence = influence
        self._abilities = abilities
        self._wargear = wargear

    def get_keywords(self):
        return self._keywords

    def get_influence(self):
        return self._influence

    def get_abilities(self):
        return self._abilities

    def get_wargear(self):
        return self._wargear
