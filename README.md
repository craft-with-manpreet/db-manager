# Database Manager

## Installation

DB Manager is built on [Python](https://www.python.org/) Version 3.12.4

To install dependencies use the following commands:

### Windows:

```sh
python -m venv venv
```

```sh
venv\Scripts\activate
```

```sh
pip install -r requirements.txt
```

#### SETUP YOUR ENVIRONMENT VARIABLES (.env file)

- Create one .env file in the project directory.
- Copy the content from env.txt (present in project directory).
- Paste the content with appropriate details or values in .env file that you've created.
- Save .env to project directory where manage.py or requirements.txt is present.

```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```

#### Create super-user using below command

```sh
python manage.py createsuperuser
```

After creating the super-user. Finally, you can try running your server with the following command

```sh
python manage.py runserver
```

[localhost]: <http://localhost:8000>

[GTK]: <https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases>

[Click Here]: <https://doc.courtbouillon.org/weasyprint/stable/first_steps.html>