from flask import Flask, jsonify,request

app= Flask (__name__)
empDB=[
    {
        'id': '101',
        'name': 'Dory Blitz',
        'title': 'Technical Leader'
    },
    {
        'id': '102',
        'name': 'Barbie Gurl',
        'title': 'Software Engineer'
    }
]
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/empdb/employee/",methods=['GET'])
def getAllEmp():
    return jsonify({'emp':empDB})
@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    user=[emp for emp in empDB if (emp['id']==empId)]
    return  jsonify({'emp': user})

if __name__=='__main__':
    app.run()