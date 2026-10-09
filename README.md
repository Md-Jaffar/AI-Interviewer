# AI-Interviewer

An AI-driven mock interview platform built with Django. 

## Tech Stack
* **Framework:** Django (Python)
* **Database:** SQLite (Default for development)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Md-Jaffar/AI-Interviewer.git
   cd AI-Interviewer
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations:**
   ```bash
   cd ai_interviewer
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

## License
MIT
