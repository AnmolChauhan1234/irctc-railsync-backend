“Uses mysql-connector-python to ensure compatibility in restricted environments.”




“Logout is client-managed by discarding JWT tokens. Server-side blacklisting is not implemented as it was not required.”





## Databases Setup

This project uses **two databases**:

- **MySQL** → Main transactional data (users, trains, bookings)
- **MongoDB** → API logs & analytics (search history, execution time, etc.)

Both are expected to run **locally**.

---

### MySQL Setup

1. Make sure MySQL is running.

- **Linux**
```bash
sudo systemctl start mysql
macOS (Homebrew)

bash
Copy code
brew services start mysql
Windows
Start MySQL Server from Services or MySQL Installer.

Create the database:

sql
Copy code
CREATE DATABASE irctc;
(Optional) Create a user:

sql
Copy code
CREATE USER 'irctc_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON irctc.* TO 'irctc_user'@'localhost';
FLUSH PRIVILEGES;
Update your .env:

env
Copy code
DB_NAME=irctc
DB_USER=irctc_user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=3306
MongoDB Setup (Logs & Analytics)
MongoDB is used only for logging and analytics.

It stores:

Endpoint name

Query parameters

User ID

Execution time

Timestamp

These logs power analytics like:

swift
Copy code
GET /api/analytics/top-routes/
Start MongoDB:

Linux

bash
Copy code
sudo systemctl start mongod
macOS (Homebrew)

bash
Copy code
brew services start mongodb-community
Windows
Start MongoDB Server from Services.

MongoDB runs locally at:

arduino
Copy code
mongodb://localhost:27017
Set in .env:

env
Copy code
MONGO_URI=mongodb://localhost:27017/irctc_logs
You do not need to manually create the MongoDB database.
It is created automatically on first write.

To verify:

bash
Copy code
mongosh
Inside shell:

js
Copy code
use irctc_logs
show collections
Collections will appear once API calls are made.

markdown
Copy code

This single section:

- Explains *why* both DBs exist  
- Works across **Linux / macOS / Windows**  
- Matches real industry README style  
- Is clear and evaluator-friendly








Here is a complete, professional README.md you can directly copy into your project. It is written in a way that looks production-grade and clearly explains your design choices.

# IRCTC Mini Backend System

A simplified backend of an IRCTC-like train booking system built using **Django REST Framework**.  
This project demonstrates how a real-world backend is designed with authentication, role-based access, transactional booking logic, logging, and analytics.

The system supports:

- User registration & login using JWT
- Role-based access (User / Admin)
- Train creation and search
- Atomic seat booking to prevent overbooking
- User-specific booking history
- API request logging in MongoDB
- Analytics using MongoDB aggregation

---

## Tech Stack

- **Backend:** Django + Django REST Framework  
- **Authentication:** JWT (SimpleJWT)  
- **Databases:**
  - **MySQL** – transactional data (Users, Trains, Bookings)
  - **MongoDB** – API logs & analytics
- **Environment Management:** python-dotenv

---

## System Overview



Client (Postman / Frontend)
|
| HTTP + JWT
v
Django REST API
|
|---------------------------|
| |
MySQL MongoDB
(Users, Trains, (Search logs,
Bookings) Analytics)


- MySQL stores core business data.
- MongoDB stores train search logs.
- Analytics is generated using MongoDB aggregation.

---

## Features

- JWT-based authentication
- Custom User model with `USER` and `ADMIN` roles
- Admin-only train creation/updation
- Train search with pagination
- Atomic seat booking using DB transactions
- User-specific booking history
- Search logging in MongoDB
- Top-routes analytics from MongoDB

---

## Setup Instructions

### Prerequisites

- Python 3.9+
- MySQL Server
- MongoDB Community Edition

---

### Installation

```bash
git clone <your-repo-url>
cd irctc-mini-backend

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env


Fill .env with your credentials:

SECRET_KEY=your-secret
DEBUG=True

MYSQL_DB=irctc
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=localhost
MYSQL_PORT=3306

MONGO_URI=mongodb://localhost:27017
MONGO_DB=irctc_logs


Create database in MySQL:

CREATE DATABASE irctc;


Run migrations:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Server runs at:

http://127.0.0.1:8000/

API Endpoints
Authentication

POST /api/register/

POST /api/login/

All other APIs require:

Authorization: Bearer <access_token>

Trains

POST /api/trains/ (Admin only)
Create or update train details.

GET /api/trains/search/?source=&destination=&limit=&offset=
Search trains between two stations.
Each request is logged in MongoDB.

Booking

POST /api/bookings/
Book seats on a train.

GET /api/bookings/my/
Get all bookings of the logged-in user.

Booking uses:

transaction.atomic()

select_for_update()

to prevent overbooking under concurrent requests.

Analytics

GET /api/analytics/top-routes/

Returns the top 5 most searched (source, destination) routes using MongoDB aggregation.

Example response:

[
  { "source": "DEL", "destination": "BOM", "count": 120 },
  { "source": "DEL", "destination": "BLR", "count": 98 }
]

Design Highlights

Stateless authentication using JWT

Clean separation of responsibilities:

MySQL → core data

MongoDB → logs & analytics

Transaction-safe booking logic

Production-style API design

Easily extendable architecture

This project is designed to mimic a real-world backend service and follows best practices for scalable API development.







## 📦 Prerequisites

Before running this project, ensure the following are installed on your system:

- Python 3.10+
- MySQL Server (8.x recommended)
- MongoDB Community Server (6.x recommended)

This project uses:
- **MySQL** for core relational data (users, bookings, trains, etc.)
- **MongoDB** for logs and analytics

Both database servers must be installed and running locally.

Download:
- MySQL: https://dev.mysql.com/downloads/
- MongoDB: https://www.mongodb.com/try/download/community

---

## ⚙️ Database Setup

After installing MySQL and MongoDB, start the services based on your OS.

### 🐧 Linux (Ubuntu/Debian)

```bash
# Start MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod
mongosh

# Start MySQL
sudo systemctl start mysql
sudo systemctl enable mysql
mysql -u root -p
Verify:

bash
Copy code
sudo systemctl status mongod
sudo systemctl status mysql
🪟 Windows
powershell
Copy code
# MongoDB
net start MongoDB
mongosh

# MySQL
net start MySQL
mysql -u root -p
Verify:

powershell
Copy code
sc query MongoDB
sc query MySQL
🍎 macOS (Homebrew)
bash
Copy code
# MongoDB
brew services start mongodb-community
mongosh

# MySQL
brew services start mysql
mysql -u root -p
Verify:

bash
Copy code
brew services list | grep mongodb
brew services list | grep mysql
🔐 Environment Configuration
Create a .env file in the project root:

env
Copy code
SECRET_KEY=your_secret_key
DEBUG=True

MYSQL_DB=irctc
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_PORT=3306

MONGO_URI=mongodb://localhost:27017
MONGO_DB=irctc_logs
Make sure both MySQL and MongoDB are running before starting the backend.

Copy code






