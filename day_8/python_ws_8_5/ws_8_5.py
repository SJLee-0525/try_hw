# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
        pass

class Dog(Animal):  
    def __init__(self):
        super().__init__()
        self.sound = '멍멍'

    def bark(self):
        print('멍멍 !')

class Cat(Animal):
    sound = '야옹'
    def __init__(self):
        super().__init__()
        self.sound = '야옹'

    def meow(self):
        print(f'야옹 !')

class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
        
    def play(self):
        print('애완동물과 놀기')

print(Pet())