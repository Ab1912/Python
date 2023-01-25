# Class Methods

class Voter():
  name = "Abishek"
  age = 36

  def details():
    print("Name : ", Voter.name)
    print("Age : ", Voter.age)


Voter.details()
print(Voter.__dict__)

getattr(Voter, "details")()
Voter.__dict__["details"]