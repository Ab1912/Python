# Student database
import sqlite3
con = sqlite3.connect("firstdb.db")

class student:
    def view(self):
        qry = "select * from studentdetails;"
        ex = con.execute(qry)
        for view in ex:
            print(view[0],end=".")
            print(view[1],end="|")
            print(view[2],end="|")
            print(view[3],end="|")
            print(view[4])


    def add(self,name,gender,age,place):
        qry = "insert into studentdetails(NAME,GENDER,AGE,PLACE) values (?,?,?,?);"
        con.execute(qry,(name,gender,age,place))
        con.commit()
        print("Student details Added")

    def update(self,name,gender,age,place,id):
        qry = "update studentdetails set NAME=?,GENDER=?,AGE=?,PLACE=? where id=?;"
        con.execute(qry,(name,gender,age,place,id))
        con.commit()
        print("Student details updated")

    def deletestu(self,id):
        qry = "delete from studentdetails where id=?"
        con.execute(qry,(id))
        con.commit()
        print("Student details deleted")

obj = student()
c = 1
while c==1:
    print('''
Student database:
1. View Student(s) details
2. Add Student details
3. Update Student details
4. Delete Student details
    ''')
    ch=int(input("Enter your Choice : "))
    if ch==1:
        print("\nStudents list : ")
        obj.view()
    elif ch==2:
        print("\nEnter Student details :")
        name=input("Name : ")
        name=name.title()
        gender=input("Gender : ")
        gender=gender.title()
        age=input("Age : ")
        place=input("Place : ")
        place=place.title()
        obj.add(name,gender,age,place)
    elif ch==3:
        print("\nUpdate Student details :")
        obj.view()
        id=input("\nEnter Student ID : ")
        name=input("Name : ")
        name=name.title()
        gender=input("Gender : ")
        gender=gender.title()
        age=input("Age : ")
        place=input("Place : ")
        place=place.title()
        obj.update(name,gender,age,place,id)
    elif ch==4:
        print("\nDelete Student details : ")
        obj.view()
        id=input("\nEnter Student ID : ")
        obj.deletestu(id)
    else:
        print("\nInvalid input!!!")
    c = int(input("\nPress 1 to continue or any other number to exit : "))
    print("Thank you!!!!")


        

        