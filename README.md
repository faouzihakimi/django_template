# Django Template Project

## Overview

This Django project provides a basic template with three main pages: Home, About, and Dashboards. The Dashboards page is restricted to registered users and features a plot created using Plotly. The project includes user authentication with login, registration, and logout functionality.

## Features

- Home page
- About page
- Dashboards page (for registered users only)
- User authentication (login, register, logout)
- Plotly integration for data visualization

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/faouzihakimi/django_template.git
   cd simple_app
   ```

2. Create a virtual environment and activate it (in the simple_app repo):
   ```
   python3 -m venv --prompt env_name .venv
   # This command creates a virtual environment named `.venv`, which is commonly ignored by Git (via `.gitignore`) to keep your repository clean.
   # The `--prompt env_name` option allows you to personalize the virtual environment's name for better visibility in your terminal prompt.
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Load initial data:
   ```
   python load_data.py
   ```

6. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```

## Usage

1. Start the development server:
   ```
   python manage.py runserver
   ```

2. Open a web browser and navigate to `http://localhost:8000`

3. To access the admin panel, go to `http://localhost:8000/admin` and log in with your superuser credentials.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
