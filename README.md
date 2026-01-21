# IRCTC Mini Backend System

A simplified backend of an IRCTC-like train booking system built using
**Django REST Framework**.\
This project demonstrates how a real-world backend is designed with
authentication, role-based access, transactional booking logic, logging,
and analytics.

Repository:\
https://github.com/AnmolChauhan1234/irctc-railsync-backend

------------------------------------------------------------------------

## ✨ Features

-   User registration & login using JWT
-   Role-based access (USER / ADMIN)
-   Admin-only train creation & update
-   Train search with pagination
-   Atomic seat booking (prevents overbooking)
-   "My Bookings" API for users
-   API request logging in MongoDB
-   Analytics using MongoDB aggregation
-   Clean separation between transactional data and analytics data

> Uses `mysql-connector-python` to ensure compatibility in restricted
> environments.\
> Logout is client-managed by discarding JWT tokens. Server-side
> blacklisting is not implemented as it was not required.

------------------------------------------------------------------------

## 🛠 Tech Stack

-   **Backend:** Django + Django REST Framework\
-   **Authentication:** JWT (SimpleJWT)\
-   **Databases:**
    -   **MySQL** -- Main transactional data (Users, Trains, Bookings)
    -   **MongoDB** -- API logs & analytics
-   **Environment Management:** python-dotenv

------------------------------------------------------------------------

## 🧭 System Overview

    Client (Postman / Frontend)
            |
            |  HTTP + JWT
            v
    Django REST API
            |
            |---------------------------|
            |                           |
         MySQL                      MongoDB
     (Users, Trains,            (Search logs,
      Bookings)                  Analytics)

-   MySQL stores core business data.
-   MongoDB stores search logs and performance data.
-   Analytics is generated using MongoDB aggregation pipelines.

------------------------------------------------------------------------

## 📦 What's Included in This Repository

-   `requirements.txt` → All Python dependencies\
-   `.env.example` → Sample environment configuration\
-   `IRCTC_Mini_Backend.postman_collection.json` → Ready-to-use Postman
    collection\
-   Complete source code for all modules

The Postman collection allows evaluators to test the full flow without
manual setup.

------------------------------------------------------------------------

## 🚀 Clone & Run the Project

``` bash
git clone https://github.com/AnmolChauhan1234/irctc-railsync-backend.git
cd irctc-railsync-backend

python -m venv .venv
source .venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`:

``` env
SECRET_KEY=your_secret_key
DEBUG=True

MYSQL_DB=irctc
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_PORT=3306

MONGO_URI=mongodb://localhost:27017
MONGO_DB=irctc_logs
```

Create the MySQL database:

``` sql
CREATE DATABASE irctc;
```

Run:

``` bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Server runs at:

    http://127.0.0.1:8000/

------------------------------------------------------------------------

## ⚙️ Databases Setup

This project uses **two databases**:

-   **MySQL** → Main transactional data (users, trains, bookings)
-   **MongoDB** → API logs & analytics (search history, execution time,
    etc.)

Both are expected to run **locally**.

------------------------------------------------------------------------

### 🐬 MySQL Setup

Ensure MySQL is running:

-   **Linux**

``` bash
sudo systemctl start mysql
```

-   **macOS (Homebrew)**

``` bash
brew services start mysql
```

-   **Windows** Start MySQL Server from *Services* or *MySQL Installer*.

Create database:

``` sql
CREATE DATABASE irctc;
```

(Optional) Create user:

``` sql
CREATE USER 'irctc_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON irctc.* TO 'irctc_user'@'localhost';
FLUSH PRIVILEGES;
```

Update `.env`:

``` env
MYSQL_DB=irctc
MYSQL_USER=irctc_user
MYSQL_PASSWORD=password
MYSQL_HOST=localhost
MYSQL_PORT=3306
```

------------------------------------------------------------------------

### 🍃 MongoDB Setup (Logs & Analytics)

MongoDB is used only for logging and analytics.

It stores:

-   Endpoint name\
-   Query parameters\
-   User ID\
-   Execution time\
-   Timestamp

These logs power analytics like:

    GET /api/analytics/top-routes/

Start MongoDB:

-   **Linux**

``` bash
sudo systemctl start mongod
```

-   **macOS (Homebrew)**

``` bash
brew services start mongodb-community
```

-   **Windows** Start MongoDB Server from *Services*.

MongoDB runs at:

    mongodb://localhost:27017

Set in `.env`:

``` env
MONGO_URI=mongodb://localhost:27017
MONGO_DB=irctc_logs
```

You do **not** need to manually create the database.\
It is created automatically on first write.

Verify:

``` bash
mongosh
```

``` js
use irctc_logs
show collections
```

------------------------------------------------------------------------

## 🔗 API Endpoints

### Authentication

-   `POST /api/register/`
-   `POST /api/login/`

All other APIs require:

    Authorization: Bearer <access_token>

------------------------------------------------------------------------

### Trains

-   `POST /api/trains/` *(Admin only)*\
-   `GET /api/trains/search/?source=&destination=&limit=&offset=`

------------------------------------------------------------------------

### Booking

-   `POST /api/bookings/`\
-   `GET /api/bookings/my/`

Uses:

-   `transaction.atomic()`
-   `select_for_update()`

to prevent overbooking.

------------------------------------------------------------------------

### Analytics

-   `GET /api/analytics/top-routes/`

Example:

``` json
[
  { "source": "DEL", "destination": "BOM", "count": 120 },
  { "source": "DEL", "destination": "BLR", "count": 98 }
]
```

------------------------------------------------------------------------

## 🧩 Design Highlights

-   Stateless authentication using JWT\
-   Clean separation of responsibilities\
-   Transaction-safe booking logic\
-   Pagination for scalable search\
-   Production-style API design\
-   Easily extendable architecture

------------------------------------------------------------------------

This project is designed to mimic a real-world backend service and
follows best practices for scalable API development.
