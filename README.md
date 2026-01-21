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






