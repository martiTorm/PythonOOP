from random import randint
from geometry_game_classes import Point, Rectangle
   
        
rectangle = Rectangle(
    Point(randint(0, 9), randint(0, 9)),
    Point(randint(10, 19), randint(10, 19))
)

print(f"Rectangle Coordinates: "
      f"(x)={rectangle.point1.x}, (y)={rectangle.point1.y} and "
      f"(x)={rectangle.point2.x}, (y)={rectangle.point2.y}")

user_point = Point(float(input("Guess X Coordinate: ")),
                   float(input("Guess Y Coordinate: ")))

user_area = float(input("Guess rectangle area: "))

if user_point.falls_in_rectangle(rectangle) is True:
    print("Your point was inside the rectangle.")
else:
    print("Your point was outside the rectangle.")

print(f"Your guessed area is: {user_area}")
print(f"The actual area is: {rectangle.area()}")