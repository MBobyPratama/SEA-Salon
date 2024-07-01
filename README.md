# SEA Salon

SEA Salon is a web application for managing a beauty salon, allowing customers to make reservations and leave reviews. This project was developed as part of the registration process for Compfest 2024.

## Project Description

SEA Salon demonstrates web development, database management, and user interface design. It incorporates key features such as user authentication, appointment scheduling, and a review system, all of which are essential for a real-world salon management application.

## Setup

1. Clone the repository:

```sh
git clone https://github.com/MBobyPratama/SEA-Salon.git
```

2. Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
```

3. Install the requirements:

```sh
pip install -r requirements.txt
```

4. Set up the database:

```sh
python manage.py migrate
```

5. Create a superuser:

```sh
python manage.py createsuperuser
```

## Running the Application

1. Start the development server:

```sh
python manage.py runserver
```

2. Open a web browser and go to `http://127.0.0.1:8000/`

## Admin Access

To access the admin features of the application, you can use the pre-configured admin account:

1. After setting up the database, run the following command to create the admin user:

```sh
python manage.py create_admin
```

2. You can now log in with the following credentials:
   - Username: thomas
   - Password: Admin123

This admin account has full access to the admin dashboard and can manage branches, services, and other administrative tasks.

## Environment Variables

The following environment variables are used in the application:

- `SECRET_KEY`: Django secret key (default is set in settings.py, but should be changed for production)
- `DEBUG`: Set to `True` for development, `False` for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts (e.g., `localhost,127.0.0.1`)

You can set these variables in a `.env` file in the project root or export them in your shell.

## Project Structure

- `SEA_salon/`: Main project directory
  - `settings.py`: Project settings
  - `urls.py`: Main URL configuration
- `main/`: Main application directory
  - `models.py`: Database models
  - `views.py`: View functions
  - `forms.py`: Form definitions
  - `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript)

## Features

- User registration and authentication
- Customer dashboard
- Admin dashboard
- Reservation system
- Review system
- Service and branch management

## Technologies Used

- Django
- Bootstrap
- jQuery
- SQLite (default database, can be changed in settings.py)
