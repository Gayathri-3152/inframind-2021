import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee_details"

)
cursor=mydb.cursor()

cursor.execute("CREATE TABLE detail(id INT AUTO_INCREMENT PRIMARY KEY,user_name VARCHAR(255),BloodPressure VARCHAR(255),BodyTemp VARCHAR(255),Oxygensat VARCHAR(255),ResperationRate VARCHAR(255),HeartRate VARCHAR(255),BloodGlucose VARCHAR(255))")

cursor.execute("SHOW TABLES")

