# Abstract Base class

from abc import ABC,abstractmethod

class College(ABC):

    @abstractmethod
    def education(self): pass

    def sports(self): pass

    def culturals(self): pass

class MCC(College):
    def education(self):
        print("MCC college provides education")

    def sports(self):
        print("MCC college provides sports")

    def culturals(self):
        print("MCC college provides culturals")

    def ecr(self):
        print("MCC college provides Extra curricular activities")

obj = MCC()
obj.education()
obj.sports()
obj.culturals()
obj.ecr()
