# Exam_Manager

This project is a simple Django application for managing exam details. It allows users to view, add, and manage exams with essential information such as subject name, subject code, exam date, exam time, semester, and exam slot.

# Features
 * View a list of exams with details.
 * Add new exams with specific attributes.
 * User-friendly interface built with Bootstrap.

#   Prerequisites
   Before running this project, ensure you have the following installed on your system:

  * Python 3.x
  * Django 5.x
  * pip (Python package installer)
# Installation
  1.Clone the repository:

       git clone https://github.com/sarangsvkm/Exam_Manager.git
       cd exam_manager
  2.Create a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

  3.Install the required packages:

    pip install -r requirements.txt
  4.Apply migrations:

     python manage.py migrate
     python manage.py makemigrations
  5.Create a superuser :

    python manage.py createsuperuser

# Usage

  1.Run the development server:

    python manage.py runserver

  2.Open your web browser and go to:
       
      http://127.0.0.1:8000/
 
3.Navigate through the application:

  * View the list of exams.
  * Add new exams using the "Add Exam" feature.      
 
# Folder Structure

    exam_manager/
    ├── exam/                 # Django app for managing exams
    │   ├── migrations/       # Database migrations
    │   ├── urls.py           # URL routing for the exam app
    │   ├── views.py          # Views for handling requests
    │   └── models.py         # Models defining the database structure
    ├── exam_manager/         # Main project folder
    │   ├── settings.py       # Project settings
    │   ├── urls.py           # Main URL routing
    │   └── wsgi.py           # WSGI configuration
    ├───static
    │   ├───css
    │   └───js
    └───templates             # HTML templates for views
    └── manage.py             # Django management script

# Contributing
 Contributions are welcome! Please follow these steps:

 1. Fork the repository.
 2. Create a new branch (git checkout -b feature-branch).
 3. Make your changes and commit (git commit -m 'Add new feature').
 4. Push to the branch (git push origin feature-branch).
 5. Create a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.


