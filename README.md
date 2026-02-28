# Cloud-Based Student Record System

A full-stack web application developed using Python (Flask) and MySQL for managing student records.  
The project demonstrates backend development, database integration, and cloud deployment concepts using AWS EC2 and S3 fundamentals.

---

## 🚀 Features

- Add new student records
- View all student records
- MySQL database integration
- Server-side form handling
- Dynamic HTML rendering using Jinja2
- AWS S3 file upload integration (concept demonstration)
- AWS EC2 deployment ready

---

## 🛠 Tech Stack

- **Backend:** Python (Flask)
- **Database:** MySQL
- **Frontend:** HTML
- **Cloud Concepts:** AWS EC2, AWS S3
- **Version Control:** Git & GitHub

---

## 📂 Project Structure
Cloud-Based-Student-Record-System/
│
├── app.py
├── db_config.py
├── requirements.txt
├── schema.sql
├── s3_upload.py
├── README.md
└── templates/
├── index.html
├── add_student.html
└── view_students.html

---
Installation & Setup

1️⃣ Clone the repository

```bash
git clone https://github.com/shashi2077/Cloud-Based-Student-Record-System.git
cd Cloud-Based-Student-Record-System
2️⃣Install dependencies
pip install -r requirements.txt
3️⃣ Setup MySQL Database

Run the schema.sql file inside MySQL:

source schema.sql;
4️⃣ Run the Application
python app.py

Open browser:

http://127.0.0.1:5000
☁️ AWS Deployment Concept

This project is designed to be deployed on:

AWS EC2 for hosting the Flask application

AWS S3 for file storage integration

Deployment steps include:

Launch EC2 instance

Install Python & dependencies

Configure security groups (port 5000)

Run Flask app inside EC2

🎯 Learning Outcomes

CRUD operations with Flask

MySQL database connectivity

Template rendering with Jinja2

Basic cloud deployment architecture

Project structuring for production readiness
👨‍💻 Author
Shashikant Yadav
B.Tech Computer Engineering
Aspiring Cloud & Backend Developer
#📸 Application Preview
