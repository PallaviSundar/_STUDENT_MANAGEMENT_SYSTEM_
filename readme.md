# 🎓 Student Management System

A **web-based Student Management System** built using **Flask (Python), SQLAlchemy, and SQLite** for the backend, and **HTML, CSS, and JavaScript** for the frontend.  
This project demonstrates **CRUD operations** (Create, Read, Update, Delete) along with search, filter, sorting, statistics, and data export features.

---

## 🚀 Features
- ✅ **Add Students** – Save name, age, and marks in the database.  
- ✅ **View Students** – Display all student records in a table.  
- ✅ **Edit Students** – Update student details easily.  
- ✅ **Delete Students** – Remove student records from the database.  
- ✅ **Search & Filter** – Search by name or filter students by marks.  
- ✅ **Sort Records** – Sort students by ID, Name, Age, or Marks.  
- ✅ **Statistics Dashboard** – View total students, average, highest, and lowest marks dynamically.  
- ✅ **Export Data** – Export student records into **CSV** or **Excel** format.  

---

## 🛠️ Tech Stack
- **Backend**: Flask (Python), SQLAlchemy (ORM)  
- **Database**: SQLite  
- **Frontend**: HTML, CSS, JavaScript  
- **Template Engine**: Jinja2 (Flask default)  

---

## 📂 Project Structure
student-management-system/
│
├── app.py # Main Flask application
├── students.db # SQLite database (auto-created)
├── templates/
│ └── index.html # Frontend (HTML + CSS + JS)
├── static/ # (Optional) for custom CSS/JS if separated
└── README.md # Documentation



---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system

## 2.Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


## 3. Install dependencies
pip install flask flask_sqlalchemy

## 4. Run the app
python app.py

## 5.Open in browser
http://127.0.0.1:5000/

📌 Example Input & Output
🔹 Example 1: Adding a Student

Input (via Add Student form):

Name: Rahul Sharma

Age: 20

Marks: 85

| ID | Name         | Age | Marks | Actions     |
| -- | ------------ | --- | ----- | ----------- |
| 1  | Rahul Sharma | 20  | 85    | Edit/Delete |

🔹 Example 2: Adding Multiple Students

Input:

Name: Ananya Gupta, Age: 19, Marks: 92

Name: Amit Verma, Age: 21, Marks: 67

Name: Priya Nair, Age: 20, Marks: 45

| ID | Name         | Age | Marks | Actions     |
| -- | ------------ | --- | ----- | ----------- |
| 1  | Rahul Sharma | 20  | 85    | Edit/Delete |
| 2  | Ananya Gupta | 19  | 92    | Edit/Delete |
| 3  | Amit Verma   | 21  | 67    | Edit/Delete |
| 4  | Priya Nair   | 20  | 45    | Edit/Delete |

🔹 Statistics Panel (Auto-calculated)

For the above students:

Total Students → 4

Average Marks → (85+92+67+45)/4 = 72.25

Highest Marks → 92

Lowest Marks → 45

🔹 Example 3: Search & Filter

If you search "Ananya", only Ananya’s row will be shown.

If you filter "Above 75", only Rahul (85) and Ananya (92) will be shown.