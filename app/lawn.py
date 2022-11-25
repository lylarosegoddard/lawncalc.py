class Lawn:
    PI = 3.14
    def __init__(self, width, length, radius):
        self.width = width
        self.length = length
        self.radius = radius

    def area(self):
      return round(self._areaSquare() - self._areaCircle(), 2)
 
    def _areaSquare(self):
        return self.width * self.length
      
    def _areaCircle(self):
        return self.radius * self.radius * Lawn.PI
    