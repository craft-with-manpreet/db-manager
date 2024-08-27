import traceback
import subprocess
import datetime
from database_management.models import Database, DatabaseLog
from typing import Type
from mysql import connector as mysql_connector
import os


class DatabaseInstance:
    def __init__(self, *args, **kwargs):
        self.database_id: str = args[0]
        database_object: Type[Database] = Database.objects.get(id=self.database_id)
        self.database_type = database_object.database_type

    def get_database_object(self) -> Type[Database]:
        database = Database.objects.get(id=self.database_id)
        return database

    def connect(self) -> object:
        database_object = Database.objects.get(id=self.database_id)

        if self.database_type == "mysql":
            try:
                connection = mysql_connector.connect(
                    host=database_object.host,
                    user=database_object.user,
                    password=database_object.password,
                    database=database_object.name,
                    port=f"{database_object.port}"
                )
                if connection:
                    if not database_object.is_connected:
                        database_object.is_connected = True
                        database_object.save()
                        DatabaseLog.objects.create(database_id=self.database_id,
                                                   title=f"Connection Successful",
                                                   description=f"Connection to the database made successfully",
                                                   status="success")
                    return connection

                DatabaseLog.objects.create(database_id=self.database_id,
                                           title=f"Connection Failed",
                                           description=f"Connection to the database failed",
                                           status="failed")
                print("Connection to the database failed")
                return False
            except Exception as e:
                print(f"Connection Error: 0001, \n {e}, \n {traceback.format_exc()}")
                DatabaseLog.objects.create(database_id=self.database_id,
                                           title=f"Connection Error: 0001 - {e}",
                                           description=f"{traceback.format_exc()}",
                                           status="error")
                return False

        return False

    def create_my_sql_backup(self):
        connection = self.connect()
        if not connection:
            return False

        database_object = self.get_database_object()
        host = database_object.host
        user = database_object.user
        password = database_object.password
        database = database_object.name
        port = database_object.port
        backup_dir = '.'
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        backup_file = os.path.join(backup_dir, f'{database}_backup_{timestamp}.sql')

        # Construct mysqldump command
        mysqldump_cmd = [
            'mysqldump',
            '-h', f"{host}",
            '-u', f"{user}",
            '-P', f"{port}",
        ]

        # Add password option only if it is not empty
        if password:
            mysqldump_cmd.append(f'-p{password}')
        else:
            mysqldump_cmd.append('-p')  # MySQL expects this flag even for empty password

        mysqldump_cmd.append(database)

        # Run the command and write the output to the backup file
        try:
            with open(backup_file, 'wb') as f:
                result = subprocess.run(mysqldump_cmd, stdout=f, stderr=subprocess.PIPE, check=True)

                print(f"Backup successful & saved to -> {backup_file}")
            return True
        except subprocess.CalledProcessError as e:
            print(f'Error during backup: {e.stderr.decode()}')

        return False

    def create_pg_backup(self):
        try:
            database_object = self.get_database_object()
            host = database_object.host
            user = database_object.user
            password = database_object.password
            database = database_object.name
            port = database_object.port
            backup_dir = '.'
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            backup_file = os.path.join(backup_dir, f'{database}_backup_{timestamp}.sql')
            process = subprocess.Popen(
                ['pg_dump',
                 '--dbname=postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, database),
                 '-Fc',
                 '-f', backup_file,
                 '-v'],
                stdout=subprocess.PIPE
            )
            output = process.communicate()[0]
            if int(process.returncode) != 0:
                print('Command failed. Return code : {}'.format(process.returncode))
                exit(1)
            return output
        except Exception as e:
            print(e)
