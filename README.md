# AirSpotter Community

AirSpotter Community ia a Django-based web application for aviation enthusiasts to record, manage, and share aircraft sightings.
Users can log sightings, upload photos, organize them into collections, and interact with aviation-related data through both a web interface and a REST API.

---

## Features
### Authentication and Users
- User registration, login, and logout
- Custom user model (`AirSpotterUser`)
- User profile with additional fields (display name, avatar, country)
- Personal dashboard with statistics

### Sightings
- Full CRUD functionality (Create, Read, Update, Delete)
- Each sighting include:
  - aircraft
  - airport
  - timestamp
  - status (draft/published)
  - visibility (public/private)
- Owner-based access control

### Photo Management
- Upload photos to sightings
- Edit and delete photos
- Media file handling

### Collections
- Group sightings into collections
- Add/remove sightings
- Owner-only access
- Public/private collections

### REST API (Django REST Framework)
- List public sightings
- Retrieve sightings details
- Create sightings (authenticated users)
- List aircraft

### Tests
- 20+ unit tests covering:
  - authentication
  - views
  - permissions
  - CRUD operations

### UI & Templates
- Base template with navigation
- Response layout
- Custom error pages (404, 500)

---

## Project Structure
```text
airspotter_project/
│
├── accounts/          # User management
├── aviation/          # Aircraft, airlines, airports
├── sightings/         # Sightings and photos
├── community/         # Collections
├── api/               # REST API
├── core/              # Shared logic & async tasks
│
├── templates/
├── static/
├── media/
```
---
## Tech Stack
- Python  3.12
- Django 6.x
- Django REST Framework
- PostgreSQL
- HTML & CSS

---

## Installation and Setup
### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/airspotter-project.git
cd airspotter-project
```

### 2. Create virtual environment
```bash
pyton -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment variables
Create a .env file in the project root
```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=airspotter_project
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=127.0.0.1
DB_PORT=5432
```
### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### Run the server
```bash
python manage.py runserver
```

### 7. Open in browser
https://127.0.0.1:8000/


##  API Endpoints
### Sightings
- GET/api/sightings/
- GET/api/sightings<id>/
- POST/api/sightings/create/
### Aircraft
- GET/api/aircraft/

## Asynchronous Tasks
The project uses Python threading to simulate asynchronous processing.
Example:
- A background task is triggered after user registration
- It simulates sending a welcome email without blocking the main request

## Running Tests
```bash
pytnon manage.py test
```

## Security
- CSRF protection enabled
- Login-required views
- Owner-based access control
- Environment variables for sensitive data

## Deployment
- Render
- Railway
- Heroku
(Deployment link can be added here)

## Notes
- This project is built for the Django Advanced course at SoftUni
- The implementation follows best practices for:
  - CVBs
  - clean code
  - modular structure

## Author
Galin Hristov
