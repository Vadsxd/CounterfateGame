import config


class Hole:
    def __init__(self):
        self.radius = config.HOLE_RADIUS
        self.x = config.HOLE_X
        self.y = config.HOLE_Y
        self.name = "Hole"

    def distance_to_object(self, obj) -> float:
        if hasattr(obj, "size"):
            obj_center_x = obj.x + obj.size / 2
            obj_center_y = obj.y + obj.size / 2
            return ((self.x - obj_center_x) ** 2 + (self.y - obj_center_y) ** 2) ** 0.5
        else:
            distance = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
            return distance - obj.radius
