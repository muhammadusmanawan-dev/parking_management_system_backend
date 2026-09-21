# Parking Management System Backend

A backend REST API for managing parking operations using **Django** and **Django REST Framework (DRF)**.

The system provides APIs for managing users, customers, vehicles, parking spots, parking tickets, ticket checkout, and payments. It also includes authentication, validation, fare calculation, and payment service architecture.

---

## Features

* User authentication using Django REST Framework Token Authentication
* Customer management
* Vehicle management
* Parking spot management
* Parking ticket creation and management
* Ticket validation
* Prevention of duplicate active tickets
* Automatic parking spot status management
* Ticket checkout functionality
* Automatic exit time recording
* Fare calculation
* Payment records
* Payment service architecture
* Stripe payment integration
* Safepay payment service placeholder
* API validation and error handling
* Database relationships using Django ORM
* RESTful API architecture
* Postman API testing support

---

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* Token Authentication
* Stripe API
* Safepay payment service architecture
* Postman
* Git & GitHub

---

# Project Structure

```text
parking_management_system_backend/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── customers/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── vehicles/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── parking_spots/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── tickets/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── payments/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── services/
│       ├── base.py
│       ├── factory.py
│       ├── stripe.py
│       └── safepay.py
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── .editorconfig
└── README.md
```

---

# Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/muhammadusmanawan-dev/parking_management_system_backend.git
```

Move into the project directory:

```bash
cd parking_management_system_backend
```

---

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

STRIPE_SECRET_KEY=your-stripe-secret-key
```

Do not commit your real `.env` file or secret keys to GitHub.

An `.env.example` file can be used to document the required environment variables without exposing secrets.

---

# Database Setup

Run migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

# Create Admin User

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter the required credentials.

---

# Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# Authentication

The API uses **Django REST Framework Token Authentication**.

After logging in, the API returns an authentication token.

For protected endpoints, send the token in the request header:

```text
Authorization: Token YOUR_TOKEN
```

Example:

```text
Authorization: Token 7fcc22da08c0b3775d76beed976da85f6f862d22a
```

Replace the example token with your own token.

---

# Authentication Endpoints

Base URL:

```text
http://127.0.0.1:8000/api/v1/auth/
```

## Register

```http
POST /api/v1/auth/register/
```

Example request:

```json
{
    "email": "user@example.com",
    "username": "parkinguser",
    "password": "StrongPassword123"
}
```

---

## Login

```http
POST /api/v1/auth/login/
```

Example request:

```json
{
    "email": "user@example.com",
    "password": "StrongPassword123"
}
```

A successful login returns an authentication token.

---

## Logout

```http
POST /api/v1/auth/logout/
```

Header:

```text
Authorization: Token YOUR_TOKEN
```

---

# 👥 Customer API

Base URL:

```text
http://127.0.0.1:8000/api/v1/
```

## Customer List

```http
GET /api/v1/customers/
```

## Create Customer

```http
POST /api/v1/customers/
```

## Retrieve Customer

```http
GET /api/v1/customers/<id>/
```

## Update Customer

```http
PUT /api/v1/customers/<id>/
```

## Delete Customer

```http
DELETE /api/v1/customers/<id>/
```

Protected endpoints require:

```text
Authorization: Token YOUR_TOKEN
```

---

# Vehicle API

## Vehicle List

```http
GET /api/v1/vehicles/
```

## Create Vehicle

```http
POST /api/v1/vehicles/
```

## Retrieve Vehicle

```http
GET /api/v1/vehicles/<id>/
```

## Update Vehicle

```http
PUT /api/v1/vehicles/<id>/
```

## Delete Vehicle

```http
DELETE /api/v1/vehicles/<id>/
```

---

# Parking Spot API

## Parking Spot List

```http
GET /api/v1/parking-spots/
```

## Create Parking Spot

```http
POST /api/v1/parking-spots/
```

## Retrieve Parking Spot

```http
GET /api/v1/parking-spots/<id>/
```

## Update Parking Spot

```http
PUT /api/v1/parking-spots/<id>/
```

## Delete Parking Spot

```http
DELETE /api/v1/parking-spots/<id>/
```

Parking spots maintain a status such as:

```text
available
occupied
```

---

# Ticket API

Tickets represent a vehicle's parking session.

Base URL:

```text
http://127.0.0.1:8000/api/v1/
```

## List Tickets

```http
GET /api/v1/tickets/
```

## Create Ticket

```http
POST /api/v1/tickets/
```

## Retrieve Ticket

```http
GET /api/v1/tickets/<ticket_id>/
```

---

# Ticket Checkout

Checkout completes an active parking ticket.

```http
POST /api/v1/tickets/<ticket_id>/checkout/
```

The checkout process:

1. Finds the ticket.
2. Checks whether the ticket is still active.
3. Records the exit time.
4. Changes the ticket status to `completed`.
5. Makes the associated parking spot available again.
6. Returns the updated ticket.

If the ticket has already been completed, the API returns an error instead of processing it again.

---

# Fare Calculation

The system calculates the parking fare based on the parking duration and the configured parking rules.

The fare is associated with the parking ticket and can be used when processing payment.

---

# Payment API

The payment system uses a service-based architecture so that different payment providers can be supported without changing the main payment logic.

Currently supported architecture includes:

* Stripe
* Safepay placeholder

---

## Stripe

Stripe is used for payment processing through the Stripe API.

The Stripe secret key should be configured through the environment:

```env
STRIPE_SECRET_KEY=your-stripe-secret-key
```

The application uses Stripe's PaymentIntent flow for payment processing.

---

## Safepay

Safepay is included as a payment provider placeholder so that the architecture can support another provider in the future.

---

# Payment Service Architecture

The payment system separates payment logic from API views.

The architecture follows this general flow:

```text
API Request
     │
     ▼
Payment View
     │
     ▼
Payment Service Factory
     │
     ├───────────────┐
     ▼               ▼
 Stripe          Safepay
 Provider        Provider
     │
     ▼
External Payment API
```

This makes it easier to add additional payment providers later.

For example:

```text
Stripe
Safepay
PayPal
JazzCash
EasyPaisa
```

can be added without rewriting the entire payment API.

---

# API Response & Status Codes

The API uses standard HTTP status codes.

Common responses include:

| Status Code                 | Meaning                                           |
| --------------------------- | ------------------------------------------------- |
| `200 OK`                    | Request completed successfully                    |
| `201 Created`               | Resource created successfully                     |
| `400 Bad Request`           | Invalid request or validation error               |
| `401 Unauthorized`          | Authentication credentials are missing or invalid |
| `404 Not Found`             | Requested resource does not exist                 |
| `500 Internal Server Error` | Unexpected server-side error                      |

---

# Validation & Error Handling

The API uses Django REST Framework serializers for request validation.

For example, invalid data may return:

```json
{
    "field": [
        "This field is required."
    ]
}
```

Authentication errors may return:

```json
{
    "detail": "Authentication credentials were not provided."
}
```

The API validates business rules such as:

* Required fields
* Valid relationships
* Duplicate active tickets
* Parking spot availability
* Ticket status before checkout
* Valid payment information

---

# Parking Flow

A typical parking workflow looks like this:

```text
1. User Login
      ↓
2. Create Customer
      ↓
3. Add Vehicle
      ↓
4. Create Parking Spot
      ↓
5. Vehicle Enters Parking
      ↓
6. Create Ticket
      ↓
7. Parking Spot → Occupied
      ↓
8. Vehicle Leaves
      ↓
9. Checkout Ticket
      ↓
10. Calculate Fare
      ↓
11. Process Payment
      ↓
12. Ticket → Completed
      ↓
13. Parking Spot → Available
```

---

# Testing With Postman

The API can be tested using Postman.

Recommended testing order:

### 1. Register

```http
POST /api/v1/auth/register/
```

### 2. Login

```http
POST /api/v1/auth/login/
```

Copy the returned token.

### 3. Add Token

For protected endpoints, use:

```text
Authorization
```

Type:

```text
Token
```

Value:

```text
YOUR_TOKEN
```

### 4. Create Customer

```http
POST /api/v1/customers/
```

### 5. Create Vehicle

```http
POST /api/v1/vehicles/
```

### 6. Create Parking Spot

```http
POST /api/v1/parking-spots/
```

### 7. Create Ticket

```http
POST /api/v1/tickets/
```

### 8. Retrieve Ticket

```http
GET /api/v1/tickets/<ticket_id>/
```

### 9. Checkout

```http
POST /api/v1/tickets/<ticket_id>/checkout/
```

### 10. Process Payment

Use the payment endpoint with the required payment information.

---

# Architecture

The project follows a Django application-based architecture.

Each major business area is separated into its own Django app:

```text
users
customers
vehicles
parking_spots
tickets
payments
```

Within each app, responsibilities are separated between:

```text
Models
    ↓
Serializers
    ↓
Views
    ↓
URLs
```

Models handle database structure.

Serializers handle:

* Data conversion
* Validation
* API input/output representation

Views handle API requests and business operations.

URLs connect API endpoints to views.

---

# Security

The project uses:

* Token-based authentication
* Authenticated API endpoints
* Environment variables for sensitive configuration
* Django's built-in security features
* Serializer validation

Sensitive credentials such as API keys should never be committed to Git.

---

# Git Workflow

The project follows a feature-branch workflow:

```text
feature/<feature-name>
          ↓
         dev
          ↓
         main
```

Typical workflow:

```bash
git switch dev
git pull origin dev

git switch -c feature/my-feature
```

After completing the feature:

```bash
git add .
git commit -m "feat: description"
git push -u origin feature/my-feature
```

Create a Pull Request:

```text
feature/my-feature → dev
```

After review and merging:

```bash
git switch dev
git pull origin dev
```

When the development branch is ready:

```text
dev → main
```

---

# Code Formatting

The project includes an `.editorconfig` file to maintain consistent formatting across supported editors.

Current formatting rules include:

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
```

These settings help maintain:

* UTF-8 encoding
* LF line endings
* Final newline at the end of files
* No unnecessary trailing whitespace

---

# API Base URL

For local development:

```text
http://127.0.0.1:8000/
```

API base:

```text
http://127.0.0.1:8000/api/v1/
```

Authentication:

```text
http://127.0.0.1:8000/api/v1/auth/
```

---

# Future Improvements

Possible future improvements include:

* Refresh token authentication
* Role-based permissions
* Parking management dashboard
* Advanced parking availability search
* Payment refunds
* Payment webhooks
* Additional payment providers
* Automated tests
* API documentation using Swagger/OpenAPI
* Production database such as PostgreSQL
* Docker support
* CI/CD pipeline
* Production deployment

---

# Development

This project was developed as a Django REST Framework backend to demonstrate:

* Django fundamentals
* REST API development
* DRF serializers and views
* Authentication
* Database relationships
* API validation
* Business logic
* Payment architecture
* Third-party API integration
* Git/GitHub workflow
* Backend project organization

---