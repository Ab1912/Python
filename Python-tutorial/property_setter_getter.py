#property setter_getter

class student:
  def __init__(self,total):
    self._total = total
  @property
  def avg(self):
    return self._total/5

  #getter
  @property
  def get_total(self):
    return self._total

  #setter
  @get_total.setter
  def get_total(self,t):
    if t < 0 or t > 500:
      print("Invalid input")
    else:
      self._total = t

obj = student (500)
print("Total : ",obj.get_total)
print("Average : ",obj.avg)
obj.total = 770
print("Total : ",obj.get_total)
print("Average : ",obj.avg)
