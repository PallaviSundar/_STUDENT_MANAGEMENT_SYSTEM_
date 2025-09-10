from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# ===================== DATABASE CONFIG =====================
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "students.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print("Script started")

# ===================== DATABASE MODEL =====================
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    marks = db.Column(db.Integer, nullable=False)  # Updated from grade to marks

    def __repr__(self):
        return f"<Student {self.name}>"

# Create database tables
with app.app_context():
    db.create_all()

# ===================== ROUTES =====================
# Home page: list all students
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Add new student
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    marks = request.form['marks']
    new_student = Student(name=name, age=age, marks=marks)
    db.session.add(new_student)
    db.session.commit()
    return redirect(url_for('index'))

# Edit student
@app.route('/edit/<int:id>', methods=['POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    student.name = request.form['name']
    student.age = request.form['age']
    student.marks = request.form['marks']
    db.session.commit()
    return redirect(url_for('index'))

# Delete student
@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
