try:
    f = open("test.txt")
    print(f.readline())
    print(f.readline(3))

except FileNotFoundError:
    print("file not found")

else:
    f.close()