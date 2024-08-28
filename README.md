# Database Manager

![alt text](https://repository-images.githubusercontent.com/846434854/fda81a33-739b-4a98-a294-c5cace6a204f)

## Installation

DB Manager is built on [Python](https://www.python.org/) Version 3.12.4

To install dependencies use the following commands:

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

### Docker Installation

This project uses Docker to manage a PostgreSQL database and a web application with Gunicorn and Django.

#### Prerequisites

Before you begin, ensure you have the following installed:

- Docker
- Docker Compose

#### Commands

```sh
docker compose build
```

```sh
docker compose up
```

<br>

### Sample Database Details

#### Postgres

- **Host:** pg-a974fbd-db-manager.h.aivencloud.com
- **Name:** pagila
- **User:** avnadmin
- **Password:** AVNS_46E_2sLim7Pahvnbzpx
- **Port:** 22906

#### MySQL

- **Host:** mysql-2d0b84d6-db-manager.h.aivencloud.com
- **Name:** defaultdb
- **User:** avnadmin
- **Password:** AVNS_MDHboaEuN37kByz4xZC
- **Port:** 22906

[localhost]: <http://localhost:8000>

[GTK]: <https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases>

[Click Here]: <https://doc.courtbouillon.org/weasyprint/stable/first_steps.html>