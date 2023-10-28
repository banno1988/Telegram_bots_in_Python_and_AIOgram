from dataclasses import dataclass, field
@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = 0

    def __post_init__(self):
        if self.x==0 or self.y==0:
            self.quadrant = 0
        elif self.x>0 and self.y>0:
            self.quadrant=1
        elif self.x<0 and self.y>0:
            self.quadrant=2
        elif self.x<0 and self.y<0:
            self.quadrant=3
        elif self.x>0 and self.y<0:
            self.quadrant=4

    def symmetric_x(self):
        return Point(self.x, -self.y)

    def symmetric_y(self):
        return Point(-self.x, self.y)