import sqlite3
con = sqlite3.connect("firstdb.db")

class data:

    def viewuser(self):
        qry = "select * from users;"
        details = con.execute(qry)
        for view in details:
            print(view)
    
    def insertuser(self,name,age,city):
        qry = "insert into users(NAME,AGE,CITY) values (?,?,?)";
        con.execute(qry,(name,age,city))
        con.commit()
        print("\nAdded new user details \n")

    def updateuser(self,name,age,city,id):
        qry = "update users set NAME=?,AGE=?,CITY=? where id=?";
        con.execute(qry,(name,age,city,id))
        con.commit()
        print("User details Updated")

    def deleteuser(id):
        qry = "delete from users where id=?";
        con.execute(qry,(id))

obj = data()
c=1
while c==1:
    print('''
User Data :
1. View user(s)
2. Add a user 
3. Update a user
4. Delete a user\n
''')

    ch = int(input("Enter youe choice : "))
    if ch==1:
        print("\nUser(s) Details :")
        obj.viewuser()
    elif ch==2:
        print("Enter New user details : ")
        name = input("Name : ")
        name = name.title()
        age = input("Enter Age : ")
        city = input ("City name : ")
        city = city.title()
        obj.insertuser(name,age,city)
    elif ch==3:
        print("Update user details : ")
        obj.viewuser()
        id = input(("Enter ID : "))
        name = input("Name : ")
        name = name.title()
        age = input("Enter Age : ")
        city = input ("City name : ")
        city = city.title()
        obj.updateuser(name,age,city,id)
    elif ch==4:
        print("Delete user details")
        id = input("Enter ID : ")
        obj.deleteuser(id)
    else :
        print("Invalid input")   

    c = int(input("\nPress 1 to continue or any other number to exit : "))
    print("Thank you!!!!")

    