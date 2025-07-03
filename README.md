# 📚 Library Management System

A web-based application built using Django to manage library operations such as book inventory, user registration, author management, and more. This system is ideal for small educational institutions, schools, or personal learning projects.

This project demonstrates my understanding of core Django features like models, views, templates, authentication, and admin interface.


 🔧 Tech Stack

* **Framework:** Django (Python)
* **Database:** SQLite (default Django DB)
* **Backend:** Python (Django Views)
* **Frontend:** Django Templates (HTML rendered by Django views)
* **Authentication:** Django built-in User Model
* **Version Control:** Git & GitHub

🚀 Features

* 🔐 User Registration and Login
* 📚 Add, Edit, View, and Delete Books
* ✍️ Manage Authors and Students
* 📖 Track book availability and details
* ⚙️ Django Admin for full backend control
* 🧩 Modular apps: `books`, `users`
* ✅ Simple UI with functional navigation

 📁 Folder Structure
Library-Management-System/
│
├── library_system/        # Django project configuration
├── books/                 # Book-related models, views, and templates
├── users/                 # Login, registration, and user management
├── templates/             # HTML templates for rendering views
├── db.sqlite3             # Default SQLite database
├── manage.py              # Django's CLI tool
└── requirements.txt       # Python dependencies

 🛠️ Installation Instructions

Follow the steps below to set up the project locally:

 1. Clone the Repository

git clone https://github.com/Varshu2806/Library-Management-System.git
cd Library-Management-System

 2. Create Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate      # For Windows
source venv/bin/activate   # For macOS/Linux

 3. Install Dependencies

pip install -r requirements.txt

> If `requirements.txt` is missing, run:
> `pip install django` and then:
> `pip freeze > requirements.txt`

 4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

 5. Create Superuser (for admin access)

python manage.py createsuperuser
6. Run Development Server

python manage.py runserver

Now, open your browser and go to:

http://127.0.0.1:8000/

 🔑 Admin Panel

Access Django admin at:
📍 `http://127.0.0.1:8000/admin`
Login with the credentials of the superuser you created.

 ✍️ Author

**Varshini Avvari**
📧 Email: [varshiniavvari@gmail.com](mailto:varshiniavvari@gmail.com)
🔗 GitHub: [Varshu2806](https://github.com/Varshu2806)

## ⭐ Contribute / Feedback

If you'd like to contribute or suggest improvements, feel free to fork the repo and open a pull request.
If this project helped you, please consider giving it a ⭐ on GitHub.

## 📌 License

This project is for educational and personal use only. No commercial license applied.
