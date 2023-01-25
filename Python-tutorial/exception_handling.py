# try_block

# 1. ZeroDivisionError 
try:
    a = 10/0
except ZeroDivisionError:
    print("Denominator can't be zero")
else:
    print(a)

try:
    a = 10/2
except ZeroDivisionError:
    print("Denominator can't be zero")
else:
    print(a)

# 2. ValueError
try:
    a = int("abi")
except ValueError:
    print("Value only can be number")
else:
    print(a)

# 3. IndexError
try:
    a = [12,45,64,32]
    print(a[8])
except IndexError as e:
    print(e)

# 4. FileNotFoundError
try:
    f = open("test.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found")

# 5. Multiple Exceptions 
try:
    a = 10/4
    print(a)
    b = [12,45,64,78]
    print(b[10])
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
