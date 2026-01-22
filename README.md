# 🔐 Advanced Django Auth System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/DRF-Framework-red?style=for-the-badge&logo=django&logoColor=white" alt="DRF">
  <img src="https://img.shields.io/badge/JWT-Secure-black?style=for-the-badge&logo=json-web-tokens&logoColor=white" alt="JWT">
</p>

A robust, production-ready Authentication API. This project demonstrates Clean Architecture by decoupling business logic from the delivery layer using the Service Layer Pattern.

---

## 🚀 Key Features

* Custom User Model | Extended profiles with birth_date, bio, location, and profile_image.
* JWT Auth | Stateless authentication using SimpleJWT with token rotation.
* Service Layer | Business logic is isolated in services.py for high testability.
* Validation | Strict data sanitization via DRF Serializers.
* Custom Exceptions | Granular error handling (e.g., Age Restriction < 13 years).
* Security | Built-in protection against common vulnerabilities and secure password reset workflows.

---

## 📂 Project Architecture

The project follows a modular structure to ensure scalability:

accounts/
├── exceptions.py   # Custom API Exception classes
├── serializers.py  # Data Validation & Transformation
├── services.py     # Pure Business Logic (The "Brain")
├── views.py        # Request/Response Handling (The "Voice")
└── models.py       # Database Schema

---

## ⚙️ Installation & Setup

### 1. Environment Preparation
- Clone the repo: git clone https://github.com/karim26010/authsystem.git
- Enter the directory: cd authsystem
- Create and activate virtual environment:
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate

### 2. Dependency Management
- pip install -r requirements.txt

### 3. Database Initialization
- python manage.py migrate

### 4. Launch
- python manage.py runserver

---

## 🔌 API Documentation (Quick Start)

### 📝 Authentication Flow

| Action | Method | Endpoint | Data Required |
| :--- | :--- | :--- | :--- |
| Register | POST | /api/register/ | username, email, password, birth_date |
| Login | POST | /api/login/ | username, password |
| Refresh | POST | /api/login/refresh/ | refresh_token |
| Profile | GET | /api/profile/ | Requires Bearer Token |

### 🧪 Example Registration JSON
{
    "username": "developer_test",
    "email": "dev@example.com",
    "password": "SecurePassword123!",
    "birth_date": "1995-12-30"
}

---

## 🛠️ Tech Stack
* Language: Python 3.12
* Framework: Django 6.0 + Django Rest Framework
* Security: SimpleJWT
* Database: SQLite (Dev) / PostgreSQL (Prod ready)

---

## 👤 Author
Karim - https://github.com/karim26010
