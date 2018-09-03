
class Species:

    def __init__(self, name:str="N/A", build_point:int=0, tier:int=1, speed:int=6, attr:dict={}, other:list=[]):
        self._name = name
        self._build_point = build_point
        self._tier = tier
        self._speed = speed
        self._attr_mod = attr
        self._other = other
    def get_name(self)->str:
        return self._name

    def get_build_point(self)->int:
        return self._build_point

    def get_tier(self)->int:
        return self._tier

    def get_speed(self)->int:
        return self._speed

    def get_attribute_modifications(self)->dict:
        return self._attr_mod

    def get_other_abilities(self)->list:
        return self._other
