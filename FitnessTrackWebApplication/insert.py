import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee_details"

)

response = requests.get('http://localhost:5000/api/data')
data = response.json()
cursor=mydb.cursor()
for i in range(10):
    user=data[i]["username"]
    bp=str(data[i]["systolic blood pressure"])+"/"+str(data[i]["diastolic blood pressure"])
    bt=data[i]["body temperature"]
    os=data[i]["oxygen saturation"]
    rr=data[i]["respiration rate"]
    hr=data[i]["heart rate"]
    bg=data[i]["blood glucose"]

    query="INSERT INTO detail(user_name,BloodPressure,BodyTemp,Oxygensat ,ResperationRate ,HeartRate ,BloodGlucose) values('{}','{}',{},{},{},{},{})".format(user,bp,bt,os,rr,hr,bg)

    cursor.execute(query)
    mydb.commit()


