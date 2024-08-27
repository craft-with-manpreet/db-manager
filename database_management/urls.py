from django.urls import path
from . import views
from . import utils

urlpatterns = [
    path('databases',
         views.DatabaseListView.as_view(template_name='database_management/database_list.html'),
         name="database-list"),

    path('create-database', views.DatabaseCreateView.as_view(
        template_name='database_management/create_database.html'),
        name="create-database"),

    path('update-database/<str:pk>', views.DatabaseUpdateView.as_view(
        template_name='database_management/update_database.html'),
        name="update-database"),

    path('delete-database/<str:pk>', views.DatabaseDeleteView.as_view(
        template_name='database_management/delete_database.html'), name="delete-database"),
]