📌 Django Todo App (With Authentication + MySQL + Due Time)

A clean and beginner-friendly Django Todo Application with:

🔐 User Authentication (Signup / Login / Logout)

📝 CRUD Operations (Add / Edit / Delete Tasks)

👤 User-Specific Tasks (Authorization)

⏰ Due Date & Time for each task

✔ Mark Tasks as Completed

🎨 Responsive UI using Bootstrap

🗄 Database: MySQL

📁 Clean project structure

Perfect for anyone learning Django authentication, CRUD, models, views, templates, MySQL integration, and deployment workflows.

🚀 Features
🔐 Authentication & Authorization

User Signup

User Login

User Logout (POST-secure in Django 5)

Each user sees only their own tasks

📝 Task Management

Add new task

Edit existing task

Delete task

Mark as completed (✓)

Completed tasks appear with strikethrough

⏰ Due Time Management

Add due date & time using <input type="datetime-local">

Display deadline on task item

Supports:
20 Nov 2025, 06:30 PM

🎨 UI / UX

Bootstrap 5

Clean, simple interface

Mobile responsive

🗂️ Project Structure
todo_project/
│
├── todo/
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── update.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md

🛠️ Tech Stack
Component	Technology
Backend	Django 5
Frontend	HTML, CSS, Bootstrap 5
Auth	Django Auth System
Database	MySQL
Language	Python 3
Deployment	GitHub, Render / PythonAnywhere (optional)
⚙️ Installation & Setup (Local)
1️⃣ Clone Repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Create Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Configure MySQL Database

Create database in MySQL:

CREATE DATABASE todoappdb;


Update DATABASES inside settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todoappdb',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


If using PyMySQL add this to todo_project/__init__.py:

import pymysql
pymysql.install_as_MySQLdb()

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Create Superuser (Optional)
python manage.py createsuperuser

7️⃣ Start Server
python manage.py runserver


App URL:

http://127.0.0.1:8000/
