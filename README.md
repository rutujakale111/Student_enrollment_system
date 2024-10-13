Student Enrollment System

Overview :
The Student Enrollment System is a web-based application that allows users to manage student profiles. Users can add, view, update, and delete student information, including their personal details and enrolled courses.

Features:
Create: Add new student profiles with details like name, age, and enrolled courses.
Read: View a list of all enrolled students and filter them based on course or age.
Update: Modify existing student profiles (e.g., change the enrolled course or update personal details).
Delete: Remove students who have graduated or dropped out from the system.
Table of Contents
Features
Technology Stack
Installation
Running the Application
API Endpoints
Postman Usage
Contributing
Technology Stack
Backend: Django (Django REST Framework)
Database: SQLite (default Django database)
Frontend: Django templates (HTML, CSS, JavaScript)
API Tool: Django REST Framework for creating and consuming APIs
Installation
Prerequisites:
Python 3.x installed on your system.
Virtual environment tool like virtualenv or venv.
Git installed for version control.
first to Install
Then clone the repository

bash
Copy code
https://github.com/rutujakale111/Student_enrollment_system
cd student_enrollment_system
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # For Linux/macOS
# OR
venv\Scripts\activate     # For Windows
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
python manage.py migrate
Create a superuser for admin access:

bash
Copy code
python manage.py createsuperuser
Start the Django development server:

bash
Copy code
python manage.py runserver
The application will be available at http://127.0.0.1:8000.

Running the Application
Go to http://127.0.0.1:8000/ to access the homepage.
Access the admin panel at http://127.0.0.1:8000/admin/ to manage users, courses, and other aspects of the system.
Use the REST API to interact with the system programmatically.
API Endpoints
Students:
GET /api/students/: Retrieve a list of all students.
GET /api/students/{id}/: Retrieve details of a specific student.
POST /api/students/: Create a new student.
PUT /api/students/{id}/: Update an existing student.
DELETE /api/students/{id}/: Delete a student.
Courses:
GET /api/courses/: Retrieve a list of all available courses.
POST /api/courses/: Add a new course.
PUT /api/courses/{id}/: Update a course.
DELETE /api/courses/{id}/: Delete a course.
Postman Usage
You can interact with the system via Postman for testing purposes. Below is how you can perform basic CRUD operations:

1. Create a Student

2. View Students

3. Update a Student

4. Delete a Student

