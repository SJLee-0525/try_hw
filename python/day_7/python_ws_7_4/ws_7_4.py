# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.width * self.height}')
        print(f'Perimeter: {(self.width * 2) + (self.height * 2)}')

shape1 = Shape(5, 3)
shape1.print_info()
