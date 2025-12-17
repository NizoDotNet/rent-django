# Rent API

A Django-based rental management API using PostgreSQL.

---

## ⚙️ Setup Instructions

### 1. Using Docker (recommended)

1. Run the app:

```bash
docker compose up --build
```

> Migrations and static files will run automatically.

2. Access the API at:

```
http://localhost:8000
```

3. Swagger UI documentation:

```
http://localhost:8000/api/schema/swagger-ui/#/bookings/bookings_create
```

---

### 2. Running Django without Docker

1. Create a `.env` file in the `server` folder with the following content:

```env
SECRET_KEY=''
DEBUG='True'
ALLOWED_HOSTS='localhost,127.0.0.1'
CSRF_TRUSTED_ORIGINS='http://localhost:8000,http://127.0.0.1:8000'

DATABASE_NAME='rent'
DATABASE_USER='user'
DATABASE_PASSWORD='password'
HOST='localhost'
```

2. Install dependencies (preferably in a virtual environment):

```bash
pip install -r requirements.txt
```

3. Apply database migrations:

```bash
python manage.py migrate
```

4. (Optional) Create a superuser:

```bash
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Access the API at:

```
http://localhost:8000
```

7. Swagger UI documentation:

```
http://localhost:8000/api/schema/swagger-ui/#/bookings/bookings_create
```

---

## 📝 Demo Flow

> Demo steps will be added later.

---

## 📌 Notes

- Running the app with Docker (`docker compose up --build`) is enough to start the whole system, including migrations.
- For production deployment, replace the development server with Gunicorn and configure allowed hosts properly.
