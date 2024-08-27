from django.views import generic
from database_management import models


class DatabaseListView(generic.ListView):
    model = models.Database
    paginate_by = 10


class DatabaseCreateView(generic.CreateView):
    model = models.Database
    fields = ("title", "database_type", "description", "host", "name", "user", "password", "port",)
    success_url = "/manage/databases"


class DatabaseUpdateView(generic.UpdateView):
    model = models.Database
    fields = ("title", "database_type", "description", "host", "name", "user", "password", "port", "is_active")
    success_url = "/manage/databases"


class DatabaseDeleteView(generic.DeleteView):
    model = models.Database
    success_url = "/manage/databases"
