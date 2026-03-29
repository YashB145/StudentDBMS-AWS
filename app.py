from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# AWS RDS Configuration
app.config['MYSQL_HOST'] = 'student-dbms.cpemike2wz3f.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'YAsh1248'  # change this
app.config['MYSQL_DB'] = 'student_dbms'

mysql = MySQL(app)

# Home
@app.route('/')
def index():
    return render_template('index.html')

# View all students
@app.route('/students')
def students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    return render_template('students.html', students=data)

# Add student
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        roll = request.form['roll_number']
        first = request.form['first_name']
        last = request.form['last_name']
        email = request.form['email']
        dob = request.form['date_of_birth']
        gender = request.form['gender']
        dept = request.form['department']
        year = request.form['admission_year']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (roll_number, first_name, last_name, email, date_of_birth, gender, department, admission_year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                    (roll, first, last, email, dob, gender, dept, year))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('students'))
    return render_template('add_student.html')

# View grades and CGPA
@app.route('/grades')
def grades():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT s.roll_number, CONCAT(s.first_name,' ',s.last_name) AS name,
        c.course_code, c.course_name,
        g.internal_marks, g.external_marks, g.total_marks,
        g.grade_letter, g.grade_points
        FROM students s
        JOIN enrollments e ON s.student_id = e.student_id
        JOIN courses c ON e.course_id = c.course_id
        JOIN grades g ON e.enrollment_id = g.enrollment_id
    """)
    data = cur.fetchall()
    cur.close()
    return render_template('grades.html', grades=data)

# Enroll student
@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    cur = mysql.connection.cursor()
    cur.execute("SELECT student_id, roll_number, first_name FROM students")
    students = cur.fetchall()
    cur.execute("SELECT course_id, course_code, course_name FROM courses")
    courses = cur.fetchall()
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        academic_year = request.form['academic_year']
        semester = request.form['semester']
        enrolled_on = request.form['enrolled_on']
        cur.execute("INSERT INTO enrollments (student_id, course_id, academic_year, semester, enrolled_on) VALUES (%s,%s,%s,%s,%s)",
                    (student_id, course_id, academic_year, semester, enrolled_on))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('students'))
    cur.close()
    return render_template('enroll.html', students=students, courses=courses)

if __name__ == '__main__':
    app.run(debug=True)