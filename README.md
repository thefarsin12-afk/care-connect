# CareConnect — Healthcare Appointment Booking API

CareConnect is a healthcare appointment booking REST API developed using **Python, Django, and Django REST Framework**. It provides API endpoints for managing doctors and booking appointments, with automatic token generation and appointment time scheduling.

This was my first major backend development project, through which I gained practical experience with serializers, URL configuration, CRUD operations, data validation, authentication, and appointment scheduling logic.

## 🚀 Features

• **Doctor Management:** Create, retrieve, update, and delete doctor records.

• **Doctor Specializations:** Store doctor details, including specialization, qualification, consultation fee, and email.

• **Appointment Booking:** Book appointments by selecting a doctor and appointment date.

• **Automatic Token Generation:** Generate sequential appointment token numbers for each doctor and appointment date.

• **Automatic Appointment Scheduling:** Calculate appointment times at 15-minute intervals, starting from 10:00 AM.

• **Data Validation:** Validate doctor information, consultation fees, and appointment dates using Django REST Framework serializers.

• **User Registration:** Provide an endpoint for user registration.

• **Admin Registration:** Implement an endpoint for creating administrator accounts.

• **Authentication and Permissions:** Apply Basic Authentication and admin-only permissions to doctor management endpoints.

• **REST API Operations:** Support creating, listing, retrieving, updating, and deleting records through API endpoints.

## 🛠️ Technologies Used

• Python

• Django

• Django REST Framework

• SQLite

• REST APIs

• Git and GitHub

## 📂 Project Structure

```text
care_connect/
├── booking/
│   ├── models.py
│   ├── serializer.py
│   └── views.py
├── booking_v2/
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── staff/
│   ├── models.py
│   └── views.py
├── staff_v2/
│   ├── serializers.py
│   └── views.py
├── care_connect/
│   └── urls.py
├── API DOC.http
├── manage.py
├── db.sqlite3
├── .env
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd care_connect
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the main dependencies:

```bash
pip install django djangorestframework
```

### 5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

The API server will run at:

`http://127.0.0.1:8000/`

## 🔗 API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/doctors/` | List doctors |
| POST | `/doctors/` | Create a doctor |
| GET | `/v2/doctor/` | List doctors using serializers |
| POST | `/v2/doctor/` | Create a doctor using serializers |
| GET | `/v2/doctor/<id>/` | Retrieve a doctor |
| PUT | `/v2/doctor/<id>/` | Update a doctor |
| DELETE | `/v2/doctor/<id>/` | Delete a doctor |
| POST | `/admin-register/` | Register an administrator |
| GET | `/appoinment/` | List appointments |
| POST | `/appoinment/` | Book an appointment |
| POST | `/v2/booking/signup/` | Register a user |
| GET | `/v2/booking/appointment/` | List appointments |
| POST | `/v2/booking/appointment/` | Create an appointment |
| GET | `/v2/booking/appointment/<id>/` | Retrieve an appointment |
| PUT/PATCH | `/v2/booking/appointment/<id>/` | Update an appointment |
| DELETE | `/v2/booking/appointment/<id>/` | Delete an appointment |

## 🧪 Example Appointment Request

**POST** `/v2/booking/appointment/`

```json
{
    "patient_name": "Alex",
    "phone": "9876543210",
    "doctor": 1,
    "appointment_date": "2026-12-11",
    "problem": "Leg pain"
}
```

The doctor ID must correspond to an existing doctor record.

## 📚 Key Learning Outcomes

• Building REST APIs using Django REST Framework.

• Working with Django models and ModelSerializers.

• Configuring URL routing across multiple Django applications.

• Implementing CRUD operations and serializer validation.

• Applying authentication and permission classes.

• Generating appointment tokens and calculating appointment times automatically.

• Managing relationships between doctors and appointments.

## 👨‍💻 Author

**Muhammad Farsin M**

Python Django Developer Trainee

---

*CareConnect was developed as a learning project to gain practical experience in backend development and REST API design.*
