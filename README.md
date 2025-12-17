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

3. Download OpenAPI documentation:

```
http://localhost:8000/api/schema/
```

4. Swagger UI documentation:

```
http://localhost:8000/api/schema/swagger-ui/
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

4. Start the development server:

```bash
python manage.py runserver
```

5. Swagger UI documentation:

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

---

## 📝 Demo Flow

1. **Register Users:**

   - Landlord registers an account.
   - Customer registers an account.

2. **Landlord Adds a Listing:**

   - Landlord creates a new listing with details such as title, description, city, price per night, and maximum guests.

3. **Customer Browses Listings:**

   - Customer views available listings through the API.

4. **Customer Creates Booking Request:**

   - Customer sends a booking request for a selected listing.
   - Validation ensures no overbooking and booking rules are respected.

5. **Landlord Reviews Booking Requests:**

   - Landlord views booking requests for their listings.
   - Landlord approves or rejects booking requests.

6. **Customer Initiates Checkout:**

   - For approved bookings, customer creates a fake checkout session.

7. **Customer Makes Fake Payment:**

   - Payment is processed with a `SUCCESS` status.
   - Checkout status is updated to `PAID`.

8. **Swagger UI Testing:**

   - All endpoints (auth, listings, bookings, checkout/payment) can be tested in Swagger UI.
   - JWT authentication is used to authorize and test endpoints directly.

---

## 📌 Notes

- Running the app with Docker (`docker compose up --build -d`) is enough to start the whole system, including migrations.
- Gunicorn is used inside the Docker container for production-ready deployment.
