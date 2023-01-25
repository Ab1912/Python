from flask import Flask,render_template,url_for,request,redirect,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
#MYSQL CONNECTION
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="mysql"
app.config["MYSQL_DB"]="python_db"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

#Loading Home Page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)

#New User
@app.route("/add_users",methods=['GET','POST'])
def add_users():
    if request.method=='POST':
          name=request.form['name']
          age=request.form['age']
          city=request.form['city']
          con=mysql.connection.cursor()
          sql="insert into users(NAME,AGE,CITY) values (%s,%s,%s)"
          con.execute(sql,[name,age,city])
          mysql.connection.commit()
          con.close()
          flash('User Details Added')
          return redirect(url_for("home"))
    return render_template("add_users.html")

#Update User
@app.route("/edit_users/<string:id>",methods=['GET','POST'])
def edit_users(id):
    con=mysql.connection.cursor()
    if request.method=="POST":
        name=request.form["name"]
        city=request.form["age"]
        age=request.form["city"]
        sql="update users set NAME=%s,CITY=%s,AGE=%s where ID=%s"
        con.execute(sql,[name,age,city,id])
        mysql.connection.commit()
        con.close()
        flash('User Details Updated')
        return redirect(url_for("home"))
        con=mysql.connection.cursor()
        
    sql="select * from users where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("edit_users.html",datas=res)

#Delete User
@app.route("/delete_users/<string:id>",methods=['GET','POST'])
def delete_users(id):
    con=mysql.connection.cursor()
    sql="delete from users where ID=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    flash('User Detail Deleted')
    return redirect(url_for("home"))


if(__name__=='__main__'):
    app.secret_key="abc123"
    app.run(debug=True)
