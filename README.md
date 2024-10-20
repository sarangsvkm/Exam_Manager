Django Exam Manager

This project is a simple Django application for managing exam details. It allows users to view, add, and manage exams with essential information such as subject name, subject code, exam date, exam time, semester, and exam slot.

Features
View a list of exams with details.
Add new exams with specific attributes.
User-friendly interface built with Bootstrap.
Prerequisites
Before running this project, ensure you have the following installed on your system:
Python 3.x
Django 5.x
pip (Python package installer)
Installation
Clone the repository:

git clone <repository-url>
cd exam_manager
Create a virtual environment :

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:


pip install -r requirements.txt
Apply migrations:

python manage.py migrate
Create a superuser (optional for admin access):

python manage.py createsuperuser
Usage
Run the development server:


python manage.py runserver
Open your web browser and go to:

http://127.0.0.1:8000/

Navigate through the application:

View the list of exams.
Add new exams using the "Add Exam" feature.
Folder Structure

exam_manager/
├── exam/                 # Django app for managing exams
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates for views
│   ├── urls.py           # URL routing for the exam app
│   ├── views.py          # Views for handling requests
│   └── models.py         # Models defining the database structure
├── exam_manager/         # Main project folder
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
└── manage.py             # Django management script
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
