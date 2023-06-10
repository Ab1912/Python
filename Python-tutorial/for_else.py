# for else loop

x = 1
for x in range(0,11,2):
    print(x,end=",")
else:
    print("End")

y = 1
for y in range(3,22,3):
    if y == 18:
        break
    print(y)
else:
    print("End")