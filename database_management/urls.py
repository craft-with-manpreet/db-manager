# Author: Manpreet Singh
# Email: dev.manpreet.io@gmail.com
# GitHub: https://github.com/craft-with-manpreet
# Portfolio: https://dev-manpreet.web.app
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Database Management
    path('databases',
         login_required(views.DatabaseListView.as_view(template_name='database_management/database_list.html')),
         name="database-list"),

    path('create-database', login_required(views.DatabaseCreateView.as_view(
        template_name='database_management/create_database.html')),
         name="create-database"),

    path('update-database/<str:pk>', login_required(views.DatabaseUpdateView.as_view(
        template_name='database_management/update_database.html')),
         name="update-database"),

    path('delete-database/<str:pk>', login_required(views.DatabaseDeleteView.as_view(
        template_name='database_management/delete_database.html')), name="delete-database"),

    path('database-info/<str:pk>', login_required(views.DatabaseDeleteView.as_view(
        template_name='database_management/database_info.html')), name="database-info"),

    # Scheduled Backups
    path('scheduled-backups/<str:database_id>',
         login_required(views.ScheduledBackupListView.as_view()),
         name="scheduled-backup-list"),

    path('create-backup-schedule/<str:database_id>', login_required(views.BackupScheduleCreateView.as_view()),
         name="create-backup-schedule"),

    path('update-scheduled-backup/<str:pk>', login_required(views.ScheduledBackupUpdateView.as_view()),
         name="update-scheduled-backup"),

    path('remove-scheduled-backup/<str:pk>', login_required(views.ScheduledBackupDeleteView.as_view()),
         name="remove-scheduled-backup"),
]
