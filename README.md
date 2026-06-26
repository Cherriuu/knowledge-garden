# Knowledge Garden 🌱

A Django app for logging topics you're learning and tracking entries under each one.

## Requirements

- Python 3.10+ (developed with 3.14)
- pip

## Setup

1. **Clone the repo**
   ```bash
   git clone <your-repo-url>
   cd knowledge_garden
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Mac/Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create an admin user**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set a username, email, and password.

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open the app**

   Visit [http://localhost:8000/](http://localhost:8000/) in your browser. Register a new account or log in with the superuser you just created.

## Features

- Create topics and log dated entries under each one
- Each user only sees and manages their own topics and entries
- Register, log in, and log out
