# Property decorators

class user:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    @property
    def msg(self):
        return self.name + " is " + str (self.age) + " Old"
        

obj = user("Abi",36)
print(obj.name)
print(obj.age)
print(obj.msg)
obj.age = 26
print(obj.msg)