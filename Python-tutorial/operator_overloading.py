# Operator overloading

class maths():
  def __init__(self,a):
    self.a = a
    
  def __add__(self,obj1,obj2):
    return obj1.a + obj2.a

  def __sub__(self,obj1,obj2):
    return obj1.a - obj2.a

  def __mul__(self,obj1,obj2):
    return obj1.a + obj2.a

  def __truediv__(self,obj1,obj2):
    return obj1.a + obj2.a

obj1 = maths(20)
obj2 = maths(10)

print("Addition : ", (obj1.a + obj2.a))
print("Subtraction : ", (obj1.a - obj2.a))
print("Multiplication : ", (obj1.a * obj2.a))
print("Division : ", (obj1.a / obj2.a))

"""
Operator	Magic Method
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
 
Comparison Operators :
Operator	Magic Method
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
 
Assignment Operators :
Operator	Magic Method
-=	__ISUB__(SELF, OTHER)
+=	__IADD__(SELF, OTHER)
*=	__IMUL__(SELF, OTHER)
/=	__IDIV__(SELF, OTHER)
//=	__IFLOORDIV__(SELF, OTHER)
%=	__IMOD__(SELF, OTHER)
**=	__IPOW__(SELF, OTHER)
>>=	__IRSHIFT__(SELF, OTHER)
<<=	__ILSHIFT__(SELF, OTHER)
&=	__IAND__(SELF, OTHER)
|=	__IOR__(SELF, OTHER)
^=	__IXOR__(SELF, OTHER)
 
Unary Operators :
Operator	Magic Method
-	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
 
"""