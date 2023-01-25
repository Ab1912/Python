#list example
para = ['abi','deva','kavi']
print('Normal para',para)
print('Para using join function')
print('|'.join(para))

#Multiline input in loop
para1 = []
print('Enter the data')
while True:
    line = input()
    if line:
        para1.append(line)
    else:
        break
print(para1)
print('Para using join function')
output = ('\n'.join(para1))
print(output)