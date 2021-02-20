from flask import Flask, jsonify
import random

app = Flask(__name__)

def details(i):
    user = ['snega', 'madhu', 'laxmi', 'aswin', 'vishnu', 'barkavi', 'barathi', 'divya', 'kavya', 'aswathi']
    username=user[i]
    bloodPressure1 = random.randint(80, 180)
    bloodPressuer2 = bloodPressure1 - random.randint(40, 50)
    bodyTemp = random.randint(90, 107)
    oxySat = random.randint(92, 98)
    respireRate = random.randint(10, 30)
    heartRate = random.randint(40, 125)
    bloodGlucose = random.randint(120, 220)

    result ={
            "username":username,
            "systolic blood pressure": bloodPressure1,
            "diastolic blood pressure": bloodPressuer2,
            "body temperature": bodyTemp,
            "oxygen saturation": oxySat,
            "respiration rate": respireRate,
            "heart rate": heartRate,
            "blood glucose": bloodGlucose,
        }
    return result


@app.route('/api/data')
def api():
    i=list(map (lambda x:x,range(10)))
    result=list(map(details,i))

    return jsonify(result)




if __name__ == "__main__":
    app.run(debug=True)

