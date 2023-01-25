# Single Inheritance (Inheriting properties from base to derived class)

class motorola:
    company = "Motorola india"
    website = "www.motorola.in"

    def address(self):
        print("Address : Chennai, India")

class motog(motorola):
    def __init__(self) -> None:
        self.model = "MotoG"
        self.year = 2014

    def pout(self):
        print("Company : ",self.company)
        print("Website : ",self.website)
        print("Model : ",self.model)
        print("Year : ",self.year)

obj = motog()
obj.pout()
obj.address()