# Cloud-Based Student Record System

A resume-ready project demonstrating **Python (Flask)** + **MySQL** integration with **AWS EC2 & S3** deployment concepts.

## Features
- Add / View / Delete student records (CRUD)
- MySQL database connectivity
- Example AWS S3 upload utility (`s3_upload.py`)
- Clean project structure

## Tech Used
- Python, Flask
- MySQL
- AWS (EC2 deployment-ready, S3 upload concept)
- HTML Templates

## Setup (Local)
1) Create DB & table:
```sql
-- run schema.sql in MySQL
```

2) Create a `.env` file (same folder as app.py):
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=student_db
DB_PORT=3306

# Optional (for S3):
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_DEFAULT_REGION=ap-south-1
```

3) Install deps & run:
```bash
pip install -r requirements.txt
python app.py
```

Open: http://127.0.0.1:5000

## AWS Notes (Interview)
- EC2: Flask app can be deployed on an Ubuntu EC2 instance (install Python, dependencies, run with gunicorn/nginx if needed).
- S3: `s3_upload.py` shows how a report/file could be uploaded to S3 using `boto3`.

## Screenshots
Add screenshots here after running locally.
