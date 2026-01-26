# CarHolding — Django Web App for Managing Car Listings

A lightweight Django application that allows users to create, browse, and manage car listings.  
Includes authentication, personal dashboards, search, sorting, and a clean Bootstrap‑based UI.

---

## Features

### Authentication
- User registration  
- Login / logout  
- Access control for editing and deleting cars  
- Personalized **My Cars** page  

### Car Management
- Create car listings with images  
- Edit and delete your own cars  
- View detailed information  
- Search cars by title  
- Sort cars by:
  - price  
  - year  
  - title  
  - model  
  - category  

### UI / UX
- Responsive Bootstrap 5 layout  
- Card‑based car grid  
- Clean navigation bar  
- Dropdown sorting  
- Flash messages  

---

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Django | Backend, ORM, authentication |
| SQLite / PostgreSQL | Database |
| Bootstrap 5 | Frontend styling |
| Pillow | Image handling |

---

## Installation

### 1. Clone the repository

git clone <your-repo-url>
cd CarHolding

### 2. Create a virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Apply migrations

python manage.py  migrate

### 5. Run the development server

python manage.py  runserver


