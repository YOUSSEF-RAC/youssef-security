from flask import Flask, render_template, request, redirect, url_for
import json
import os
import werkzeug.security

app = Flask(__name__, static_url_path='', static_folder='.')

students = []
students_file_path = 'students.json'
if os.path.exists(students_file_path):
    with open(students_file_path) as f:
        students = json.load(f)
else:
    print(f"Error: '{students_file_path}' not found or cannot be loaded.")

teachers = []  
teachers_file_path = 'teachers.json'  
if os.path.exists(teachers_file_path):
    with open(teachers_file_path) as f:
        teachers = json.load(f)
else:
    print(f"Error: '{teachers_file_path}' not found or cannot be loaded.")

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
        if student['student_name'] == username:
            if 'salt' not in student or 'password' not in student:
                salt = os.urandom(16).hex()
                hashed_password = werkzeug.security.generate_password_hash(password + salt)

                student['salt'] = salt
                student['password'] = hashed_password

                print(f"Nieuwe salt: {salt}, Nieuwe hashed_password: {hashed_password}")  

                with open(students_file_path, 'w') as f:
                    json.dump(students, f)

            salt = student['salt']
            if werkzeug.security.check_password_hash(student['password'], password + salt):
                return redirect(url_for('statements'))

    return redirect(url_for('login'))

@app.route('/login_teacher', methods=['POST'])
def login_teacher():
    username = request.form['username']
    password = request.form['password']

    for teacher in teachers:
        if teacher['teacher_name'] == username:
            if 'salt' not in teacher or 'password' not in teacher:
                salt = os.urandom(16).hex()
                hashed_password = werkzeug.security.generate_password_hash(password + salt)


                teacher['salt'] = salt
                teacher['password'] = hashed_password
                
                print(f"Nieuwe salt: {salt}, Nieuwe hashed_password: {hashed_password}")  

                with open(teachers_file_path, 'w') as f:
                    json.dump(teachers, f)

            salt = teacher['salt']
            if werkzeug.security.check_password_hash(teacher['password'], password + salt):
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
