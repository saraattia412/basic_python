from abc import ABC
class Shape(ABC):
    def calculate_area(self):
        pass
class Rectangle(Shape):
  length = 2
  width = 3
  def calculate_area(self):
      return self.length * self.width
class Triangle(Shape):
  length = 2
  width = 3
  def calculate_area(self):
      return (self.width * self.length) / 2
rect_1 = Rectangle()
tri_1 =Triangle()
print("Area of a rectangle= ", rect_1.calculate_area())
print("Area of a Triangle= ", tri_1.calculate_area())
