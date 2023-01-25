# Multilevel Inheritance

class Grandfather:
    def house(self):
        print("Grandfather's house")

class Father(Grandfather):
    def car(self):
        print("Father's car")

class Son(Father):
    def boat(self):
        print("Son's boat")

obj = Son()
obj.house()
obj.car()
obj.boat()
        