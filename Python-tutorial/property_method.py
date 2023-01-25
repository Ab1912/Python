# Property Method

class student:
    def __init__(self,total) -> None:
        self._total = total

    def average(self):
        return self._total/5

    #getter
    def getter(self):
        return self._total

    #setter
    def setter(self,t):
        if t > 0 and t < 500:
            self._total = t
        else:
            print("Invalid input")

    total = property(getter,setter) 

obj = student(500)
print("Total ",obj._total)
print("Average : ",obj.average())
obj.total = 300
print("Total ",obj._total)
print("Average : ",obj.average())
