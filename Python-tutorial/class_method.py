# Class Method

class student:
    count = 0

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        student.count += 1

    def pout(self):
        print("Name : ",self.name,"Age : ",self.age)

    @classmethod
    def total(cls):
        return cls.count

obj = student("Kumar", 23)
obj.pout()
obj = student("Sathish", 21)
obj.pout()
print("Total number of admission : ",student.total())
