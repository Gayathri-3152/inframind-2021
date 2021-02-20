import smtplib, ssl
import schedule
import time
import requests
from threading import Timer



def health():
    msg = "You may have these following issues, so take care of your health, proper medication is needed\n"
    response = requests.get('http://localhost:5000/api/data')
    dataGotFromApi = response.json()

    bp = str(dataGotFromApi[0]["systolic blood pressure"])
    bp1 = str(dataGotFromApi[0]["diastolic blood pressure"])
    btemp = str(dataGotFromApi[0]["body temperature"])
    oxysat = str(dataGotFromApi[0]["oxygen saturation"])
    resrate = str(dataGotFromApi[0]["respiration rate"])
    heartrate = str(dataGotFromApi[0]["heart rate"])
    glucose = str(dataGotFromApi[0]["blood glucose"])

    if (int(glucose) >= 140 and int(glucose) < 200):
        msg = msg+"prediabetes\n"
    elif (int(glucose) >= 200):
        msg = msg + "Diabetes\n"

    if (int(btemp) > 100 and int(resrate) >= 24):
        msg=msg + "Bronchitis\n"

    if (int(oxysat) < 96):
        msg=msg+ "Hypoxemia\n"

    if ((int(oxysat) >= 92 and int(oxysat) <= 95) and int(heartrate) >= 100 and int(resrate) >= 20):
        msg=msg + "Asthma\n"

    if ((int(bp) < 90 or int(bp1) < 60)):
        msg=msg + "Low Blood Pressure\n"
    elif ((int(bp) >= 180 or int(bp1) >= 120)):
        msg=msg + "Severe Blood Pressure\n"
    elif ((int(bp) >= 140 or int(bp1) >= 90)):
        msg = msg + "High Blood Pressure\n"

    if ((int(bp) >= 140 or int(bp1) >= 90) and int(heartrate) >= 100):
        msg = msg + "you are Stressed \n"

    if (msg == "You may have these following issues, so take care of your health, proper medication is needed\n"):
        msg = "You are doing great, keep maintaining your health\n"

    msg = msg+"\nblood pressure  : "+str(dataGotFromApi[0]["systolic blood pressure"]) +"/"+str(dataGotFromApi[0]["diastolic blood pressure"])
    msg = msg+"\nbody temperature  : "+str(dataGotFromApi[0]["body temperature"])+"F"
    msg = msg + "\noxygen saturation  : " + str(dataGotFromApi[0]["oxygen saturation"])+"%"
    msg = msg + "\nrespiration rate  : " + str(dataGotFromApi[0]["respiration rate"])+"/min"
    msg = msg + "\nheart rate  : " + str(dataGotFromApi[0]["heart rate"])+"/min"
    msg = msg + "\nblood glucose  : " + str(dataGotFromApi[0]["blood glucose"])+"mg/dL"

    return msg

def send():
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.starttls(context=ssl.create_default_context())
    sender = "sample33022@gmail.com"
    password = "sample2233"
    rec = "chandranpattu1976@gmail.com"
    msg = health()

    mail.login(sender, password)
    mail.sendmail(sender, rec, msg)
    print("mail send successfully")
    mail.quit()




schedule.every().day.at("00:06").do(send)

while 1:
    schedule.run_pending()
    time.sleep(1)
