from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/api/employees', methods=['GET'])
def get_employees():
    employees = EmpModel.query.all()
    data = [{
        "id": 1,
        "name": "Abc"
    }] 
    # data = [
    # {
    #     "id" : emp.id,
    #     "name" : emp.name,
    #     "designation" : emp.designation, "gender" : emp.gender,
    #     "salary" : emp.salary,
    #     "joining__date" : emp. joining__date,
    # } for emp in employees]
    return jsonify({'employees': data})



if __name__ == '__main__':
    app.run(debug=True)