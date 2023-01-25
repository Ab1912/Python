#STRING FUNCTIONS
a = "abi practice123"
print(a)
print(type(a))
print('String Functions')
print('Upper case : ', a.upper())
print('Lower case : ', a.lower())
print('Capitalize first letter : ', a.capitalize())
print('Title : ', a.title())
print('Count of a letter', a.count("a", 0, 14))  #indexing

#conditional functions
print('Starts with : ', a.startswith("ab"))
print('Starts with : ', a.endswith("34"))
print('Find : ', a.find("a", 2, 14))  # indexing
print('Replace', a.replace("a", "A"))

#Boolean functions
b = "abi"
print("Uppercase : ", b.isupper())
print("Lowercase : ", b.islower())
print("Alphabet : ", b.isalpha())
print("Numeric : ", b.isnumeric())
print("Alphanumeric :", b.isalnum())

#Split Function
s = 'my\nname\nis\nabishek'
print(s)
print(s.splitlines())
print(s.splitlines(True))
c = "I,am,a,karate,teacher"
print(c.split(","))
print('\n')
#Strip function
print('Strip Function\n')
d = "    abi    great   "
print(d,'\n',len(d))

print(d.strip(),'\n',len(d.strip())) # normal strip

print(d.lstrip(),'\n',len(d.lstrip())) # left side strip

print(d.rstrip(),'\n',len(d.rstrip())) # right side strip

# Partition

e = '12-10-1986'
print(e.partition('-'))
