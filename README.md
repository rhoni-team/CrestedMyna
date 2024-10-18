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

5. Copy the `crested_myna_records.csv` file to the `data` folder

6. Run migrations

```bash
python manage.py migrate
```

7. Populate the database by using a management command

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

1. You are going to see the django welcome page.
