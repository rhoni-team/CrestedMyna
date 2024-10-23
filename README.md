# CrestedMyna

Web application to visualize Crested Myna expansion


# Installation

1. Clone the repository

2. Create a virtual environment

3. Install the dependencies

```bash
pip install -r requirements.txt
```
4. Create a `data` folder inside `data_analysis` folder

```bash
cd data_analysis
mkdir data
```

5. Copy the `crested_myna_records.csv` file to the `data` folder (they are in the private crested_myna_data repository)

6. Create a `.env.dev` file in the root folder and add the environment variables.

```bash
POSTGRES_DB="crested_myna"
POSTGRES_USER="your_username"
POSTGRES_PASSWORD="your_password"
PG_HOST=127.0.0.1
PG_PORT=5432
DEBUG=true
SECRET_KEY='django-insecure-something_random'
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
DJANGO_CORS_ALLOWED_ORIGINS=http://localhost http://127.0.0.1
```

7. Create the database

name: crested_myna
username: your_username
password: your_password

8. Run migrations

```bash
python manage.py migrate
```

9. Populate the database by using a management command

```bash
python manage.py populate_database_with_ebird_data
```

# Usage

1. Run the development server

```bash
python manage.py runserver
```

2. Open your web browser and navigate to `http://127.0.0.1:8000/`   


# Notes

1. You are going to see the home page.
