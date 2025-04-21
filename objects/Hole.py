class Hole:
    def __init__(self, radius: float, x: int, y: int):
        self.radius = radius
        self.x = x
        self.y = y

    def distance_to_object(self, obj) -> float:
        return ((self.x + self.radius // 2 - obj.x) ** 2 + (self.y + self.radius // 2 - obj.y) ** 2) ** 0.5
