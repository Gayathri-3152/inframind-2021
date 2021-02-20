from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee_details"

)



@app.route('/')
def page():
    return render_template("form.html")

database={"username123":"abc","userabc":"abc"}

@app.route('/', methods=['POST'])
def page1():
    username=request.form['username']
    password=request.form['password']
    if username not in database:
        return render_template("form.html",info='"INVALID USERNAME"')
    elif database[username]!=password:
        return render_template("form.html",info='"INVALID PASSWORD"')
    else:
        cursor = mydb.cursor()
        query = "select * from info"
        cursor.execute(query)
        record = cursor.fetchall()
        return render_template("table.html",record=record)
        cursor.close()
        mydb.close()



if __name__== "__main__":
    app.run(host='localhost', port=5001, debug=True)


