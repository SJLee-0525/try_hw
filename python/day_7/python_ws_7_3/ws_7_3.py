# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        result = (self.width * 2) + (self.height * 2)
        return result

shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
