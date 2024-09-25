from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__, static_url_path='', static_folder='.')


students = []
students_file_path = 'students.json'
if os.path.exists(students_file_path):
    with open(students_file_path) as f:
        students = json.load(f)
else:
    print(f"Error: '{students_file_path}' not found or cannot be loaded.")


statements = []
statements_file_path = 'actiontype_statements.json'
if os.path.exists(statements_file_path):
    with open(statements_file_path) as f:
        statements = json.load(f)
else:
    print(f"Error: '{statements_file_path}' not found or cannot be loaded.")

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_student', methods=['POST'])
def login_student():
    username = request.form['username']
    password = request.form['password']
    

    for student in students:
        if student['student_name'] == username and str(student['student_number']) == password:
            return redirect(url_for('statements'))  
    
    return redirect(url_for('login'))

@app.route('/statements')
def statements():
    return render_template('statements.html', statements=statements)

@app.route('/update_result', methods=['POST'])
def update_result():

    result = request.form['result']
    
    return {'result': 'Success'}

if __name__ == '__main__':
    app.run(debug=True)
