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

To initialize your database with the default required data run the below
command, It's mandatory to execute the below command for a smooth
experience while running your project.

```sh
python manage.py init
```

Finally, you can try running your server,

```sh
python manage.py runserver
```

[localhost]: <http://localhost:8000>

[GTK]: <https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases>

[Click Here]: <https://doc.courtbouillon.org/weasyprint/stable/first_steps.html>