# Multiple Inheritance (Inheriting properties more than one class)

class Father:
    def fishing(self):
        print("Fishing in river")

    def chess(self):
        print("Playing chess often")

class Mother:
    def cooking(self):
        print("Cooking in the kitchen")

    def chess(self):
        print("Playing chess rarely")

class Son(Father,Mother):
    def cycle(self):
        print("Riding bicycle")

obj = Son()
obj.cycle()
obj.fishing()
obj.cooking()
obj.chess()
