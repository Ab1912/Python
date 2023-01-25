# Mysql user database
import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",username="root",password="mysql",database="python_db")

class user:
    def insertuser(self,name,age,city):
        res=con.cursor()
        sql="insert into users(NAME,AGE,CITY) values (%s,%s,%s)"
        res.execute(sql,(name,age,city))
        con.commit()
        print("Data Added")

    def updateuser(self,name,age,city,id):
        res=con.cursor()
        sql="update users set NAME=%s,AGE=%s,CITY=%s where id=%s"
        user=(name,age,city,id)
        res.execute(sql,user)
        con.commit()
        print("Data updated")

    def selectuser(self):
        res=con.cursor()
        sql="select ID,NAME,AGE,CITY from users"
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

    def deleteuser(self,id):
        res=con.cursor()
        sql="delete from users where id=%s"
        res.execute(sql,(id))
        con.commit()
        print("Data deleted")

obj=user()

while True:
    print('''
1. Insert users
2. Update users
3. Select users
4. Delete users
5. Exit''')

    choice=int(input("Enter your choice : "))
    if choice==1: #Insert user
        name=input("Enter Name : ")
        name=name.title()
        age=input("Enter Age : ")
        city=input("Enter City : ")
        city=city.title()
        obj.insertuser(name,age,city)
    elif choice==2: #Update user
        id=input("Enter iD : ")
        name=input("Enter Name : ")
        name=name.title()
        age=input("Enter Age : ")
        city=input("Enter City : ")
        city=city.title()
        obj.updateuser(name,age,city,id)
    elif choice==3:
        obj.selectuser()
    elif choice==4:
        id=input("Enter ID : ")
        obj.deleteuser(id)
    elif choice==5:
        print("Thank you!!!!")
        quit()
    else:
        print("Invalid choice, try again!!!")