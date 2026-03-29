# Student DBMS Project

## 📌 Description
This is a Student Database Management System built using Python (Flask), HTML, and MySQL.  
The application is connected to an AWS RDS MySQL database for remote data storage.

## 🛠 Tech Stack
- Python (Flask)
- MySQL (AWS RDS)
- HTML/CSS

## ☁️ AWS Integration
- Database hosted on AWS RDS
- Remote connection using endpoint, username, and password
- Ensures scalable and cloud-based storage

## ⚙️ Setup Instructions


### 1. Install dependencies
pip install flask mysql-connector-python

### 2. Configure Database Connection
Update your database credentials in `app.py`:

DB_HOST = "your-rds-endpoint"
DB_USER = "your-username"
DB_PASSWORD = "your-password"
DB_NAME = "your-database-name"

⚠️ Do NOT upload real credentials to GitHub. Use environment variables for security.

### 5. (Optional) Import database structure
If needed, import:
mysql -u username -p < database.sql

### 6. Run the application
python app.py

### 7. Open in browser
http://127.0.0.1:5000/

## 📁 Project Structure
- app.py → Backend (Flask)
- database.sql → Database schema
- templates/ → HTML pages

## ⚠️ Important Notes
- AWS RDS must be running and accessible
- Make sure your IP is allowed in RDS security group
- Never expose AWS credentials in public repositories