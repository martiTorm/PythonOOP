# Development Steps
"""
# 1. Writing down the objects on paper
# 2. Writing a class for each object
# 3. Writing methods for each class
# 4. Calling the classes and their methods
"""

# What is a class?
"""
# A class is like a blueprint for creating objects. Imagine you want to make many points on a map.
# Instead of writing code for each point, you make a "Point" class, and then you can create as many points as you want.
"""

# What is 'self'?
"""
# 'self' is a way for the class to refer to itself. When you create a point, 'self' means "this point".
# For example, if you have two points, 'self.x' and 'self.y' will be different for each point.
"""

# What is __init__?
"""
# '__init__' is a special method that runs when you create a new object from the class.
# It sets up the object with the values you give it.
# Normal methods (like falls_in_rectangle) are functions you can use after the object is created.
# Methods could be considered as functions that belong to the class.
"""

# IMPORTANT to consider about classes:
"""
# According to one of the software design principles, a class should have only one responsibility. In other words, we should avoid writing classes that do a lot of work.
"""

# Example:
"""
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# Here, p1.x is 1, p2.x is 3. 'self.x' inside the class refers to the x value of the specific point.
"""
class Point:
    """
    The Point class represents a point with x and y coordinates.
    You can use it to create points on a map, check if a point is inside a rectangle,
    and calculate the distance between two points.
    """
    
    def __init__(self, x, y):
        self.x = x  # Store the x coordinate for this point
        self.y = y  # Store the y coordinate for this point

    def falls_in_rectangle(self, lowerleft, upperright):
        # Check if this point is inside the rectangle defined by lowerleft and upperright corners
        if lowerleft[0] < self.x < upperright[0] \
            and lowerleft[1] < self.y < upperright[1]:
            return True
        else:
            return False

    def distance_from_point(self, other_point):
        # Calculate the straight-line distance to another point using Pythagoras' theorem
        distance_x = self.x - other_point.x
        distance_y = self.y - other_point.y
        return (distance_x**2 + distance_y**2)**0.5

# Create two points
point1 = Point(1, 2)
point2 = Point(3, 4)

# Find the distance between point1 and point2
print(point1.distance_from_point(point2))