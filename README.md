### Student Enrollment System

### Description 
The Student Enrollment System is a web application that allows users to manage student profiles efficiently. Users can create, read, update, and delete student records, making it easy to maintain accurate and up-to-date student information. The system also includes filtering options to view students based on specific criteria like age or enrolled courses.

### Features
- **Create**: Add new student profiles with details such as name, age, and enrolled courses.
- **Read**  : View all enrolled students in a list and filter by course or age.
- **Update**: Edit student profiles, including updating courses or personal details.
- **Delete**: Remove student records for those who have graduated or dropped out.

### Technical Details
Framework: Built using Django and Django REST Framework.
Database: Utilizes SQLite for data storage, with options for scalability using other databases.
Frontend: Employs HTML for a basic yet functional user interface.
API Access: Provides RESTful API endpoints for seamless interaction with student data, supporting operations such as listing, creating, updating, and deleting student records.

### Project Structure
Student-enrollment-system/ ├── Student_enrollment/ # Main project folder │ ├── settings.py # Project settings │ └── urls.py # Main project URLs │ ├── students/ # App managing student data │ ├── migrations/ # Database migrations │ ├── models.py # Student model │ ├── serializers.py # Serializers for API (if using DRF) │ ├── views.py # Views for CRUD operations │ ├── urls.py # App URLs │ ├── admin.py # Register models in admin panel │ └── templates/ # HTML templates for rendering views │ └── student_list.html # Template for displaying student list │ ├── manage.py # Django management script └── db.sqlite3 # SQLite database file.


## Installation and Setup

1.Clone the repository:

git clone https://github.com/rutujakale111/Student_enrollment_system.git
cd Student-enrollment-system
2.Create a virtual environment and activate it:
python3 -m venv env
source env/bin/activate 

3. Install dependencies:
pip install 

4. Run migrations to set up the database:
python manage.py makemigrations
python manage.py migrate

5. Create a superuser to access the Django admin panel (optional):
python manage.py createsuperuser

6. Run the development server:
python manage.py runserver

To open and access the API for your Student Enrollment System built with Django (especially if you're using Django REST Framework), you'll follow these steps:

Install Django REST Framework
If you haven't already installed Django REST Framework, you can do so by adding it to your requirements.txt or installing it directly:
pip install djangorestframework

Then, make sure to add it to your INSTALLED_APPS in settings.py:
INSTALLED_APPS = [
    ...
    'rest_framework',
    'students', 
]

### Endpoints
/students/: To view the list of students and add new ones.
/students/<int:pk>/: To update or delete a specific student by ID.

Once your server is running (you can start it with python manage.py runserver), you can access the API endpoints using a web browser or tools like Postman
### API Endpoints:
GET /students/: Retrieve a list of all students.
POST /students/: Create a new student.
GET /students/<id>/: Retrieve a specific student by ID.
PUT /students/<id>/: Update a specific student by ID.
DELETE /students/<id>/: Delete a specific student by ID.

