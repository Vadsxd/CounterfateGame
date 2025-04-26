import config


class Hole:
    def __init__(self):
        self.radius = config.HOLE_RADIUS
        self.x = config.HOLE_X
        self.y = config.HOLE_Y
        self.name = "Hole"

    def distance_to_object(self, obj) -> float:
        return ((self.x + self.radius // 2 - obj.x) ** 2 + (self.y + self.radius // 2 - obj.y) ** 2) ** 0.5
