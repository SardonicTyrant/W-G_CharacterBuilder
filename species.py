
class Species():
    _build_points = 0
    _tier = 1
    _speed = 6
    def __init__(self):
        pass

    def get_build_points(self) -> int:
        return self._build_points

    def get_tier(self) -> int:
        return self._tier

    def get_speed(self) -> int:
        return self._speed
