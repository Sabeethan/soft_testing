def add(a,b):
    """Simple Add function"""
    return a + b

def divide(numerator, denominator):
    """Divide function with zero error exception"""
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return numerator / denominator

def subtract(a, b):
    return a - b

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calculate_area(self):
        a = ((self.p1.x * (self.p2.y - self.p3.y)) +
            (self.p2.x * (self.p3.y - self.p1.y)) +
            (self.p3.x * (self.p1.y - self.p2.y))) / 2
        return abs(a)
