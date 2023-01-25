# opening a file
import 
print("Opening a file : \n")
try:

    f = open("test.txt","r")
    print(f.read())

except FileNotFoundError:
    print("file not found")

else:
    f.close()

try:

    f = open("tst.txt","r")
    print(f.read())

except FileNotFoundError:
    print("file not found")

else:
    f.close()
print("--------------")

# Readline in file
print("Readline in file : \n")
try:
    f = open("test.txt","r")
    print(f.readline())
    print(f.readline(3))
    print("--------------")
except FileNotFoundError as e:
    print(e)

# Loop in file
print("Loop in file : \n")
try:
    f = open("test.txt","r")
    for line in f:
        print(line)
except FileNotFoundError as e:
    print(e)
else:
    f.close()
print("--------------")

# Overwriting in file

try:
    f = open("test.txt","w")
    f.write("This is Abishek\nLearning python")
    f.close()

    f = open("test.txt","r")

    for line in f:
        print(line)

except FileNotFoundError as e:
    print(e)
else:
    f.close()
print("--------------")

# Appending a file
print("Appending a file : \n")
try:
    f = open("test.txt","a")
    f.write("\nfrom youtube")
    f.close()

    f = open("test.txt","r")
    print(f.read())
except FileNotFoundError as e:
    print(e)
else:
    f.close()
print("--------------")

# Delete a file
print("Delete a file :")

import os

if os.path.exists("test2.txt"):
    os.remove("test2.txt")
    print("Test2 file deleted")
    #os.rmdir("folder name") - for deleting a folder

else:
    print("File not found")
    