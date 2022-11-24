
from app.lawn import Lawn

area = 0
anotherarea = 0
overallTurfNeeded = 0
radiusG = float(input("What is the radius of the flower bed? "))
widthG = float(input("What is the width of the lawn? "))
lengthG = float(input("What is the length of the lawn? "))

overallTurfNeeded = Lawn(widthG, lengthG, radiusG)
print('You need ')
print(overallTurfNeeded.area(), 'm2 of turf')