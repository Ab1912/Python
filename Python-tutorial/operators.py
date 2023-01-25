 #Arithmetic operators
print('Arithematic operators : \n')
"""
    +     Addition
    -     Subtraction
    *     Multiplication
    /     Division
    %     Modulus(to find reminder of division)
    **    Exponentiation
    //    floor division(division without reminder
    """
a = 11
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# Assignment operators
print('\n Assignment operators : \n')
"""
    +=     Addition
    -=     Subtraction
    *=     Multiplication
    /=     Division
    %=    Modulus(to find reminder of division)
    **=    Exponentiation
    //=    floor division(division without reminder
"""
b = 135
print(b)
b += 10
print(b)
b -= 10
print(b)
b *= 10
print(b)
b /= 10
print(b)
b %= 10
print(b)
b **= 10
print(b)
b //= 10
print(b)

# Comparison or Relational operators
print('\n  Comparison or Relational operators : \n')
"""
    ==  Equal to
    !=  Not Equal to
    >   Greater than
    <   Less than
    >=  Greater or Equal to
    <=  Less than or Equal to  
"""
a = 15
b = 20

print('A Equal to B : ', a == b)
print('A Not Equal to B : ', a != b)
print('A Greater than B : ', a > b)
print('A Lesser than B : ', a < b)
print('A Greater or Equal to B : ', a >= b)
print('A Lesser or Equal to B : ', a <= b)

# Logical Operators
print('\n  Logical operators : \n')

"""
    and
    or
    not
"""
a = 25
print(a >= 10 and a <= 20)
print(a >= 10 or a <= 20)
print(not(a >= 10 and a <= 20))  # inverts the result

#Bitwise operators

"""
&   AND
|   OR
^   XOR
~   NOT
<<  ZERO FILL LEFT SHIFT
>>  SIGNED RIGHT SHIFT
"""

a = 25
b = 45
print('AND operator : ',a&b)
print('OR operator : ',a|b)
print('XOR operator : ',a^b)
print('NOT operator : ',~a)
print('ZERO FILL LEFT SHIFT operator : ',a<<2)
print('SIGNED RIGHT SHIFT operator : ',a>>2)
