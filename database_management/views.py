# Author: Manpreet Singh
# Email: dev.manpreet.io@gmail.com
# GitHub: https://github.com/craft-with-manpreet
# Portfolio: https://dev-manpreet.web.app
from django.views import generic
from database_management import models
from django.shortcuts import get_object_or_404, render, redirect
from database_management.forms import ScheduleBackupForm


# =============================
# ==== Database Management ====
# =============================

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


# ============================
# ===== Scheduled Backup =====
# ============================

class ScheduledBackupListView(generic.View):
    def get(self, request, database_id):
        database = get_object_or_404(models.Database, id=database_id)
        objects = models.BackupSchedule.objects.filter(database=database)
        return render(request, "backup_schedule/scheduled_backup_list.html", {
            "objects": objects
        })


class BackupScheduleCreateView(generic.View):
    def get(self, request, database_id):
        get_object_or_404(models.Database, id=database_id)
        form = ScheduleBackupForm()
        return render(request, "backup_schedule/create_backup_schedule.html", {
            "form": form
        })

    def post(self, request, database_id):
        database = get_object_or_404(models.Database, id=database_id)
        form = ScheduleBackupForm(data=request.data)
        if not form.is_valid():
            return render(request, "backup_schedule/create_backup_schedule.html", {
                "form": form
            })

        scheduled_backup: models.BackupSchedule = form.save()
        scheduled_backup.database = database
        scheduled_backup.save()
        return redirect("scheduled-backups", database_id=database_id)


class ScheduledBackupUpdateView(generic.View):
    def get(self, request, pk):
        scheduled_backup = get_object_or_404(models.BackupSchedule, id=pk)
        form: ScheduleBackupForm = ScheduleBackupForm(instance=scheduled_backup)
        return render(request, "backup_schedule/update_backup_schedule.html", {
            "form": form
        })

    def post(self, request, pk):
        instance = get_object_or_404(models.BackupSchedule, id=pk)
        form: ScheduleBackupForm = ScheduleBackupForm(data=request.data, instance=instance)
        if not form.is_valid():
            return render(request, "backup_schedule/update_backup_schedule.html", {
                "form": form
            })

        form.save()
        return redirect("scheduled-backups", database_id=instance.database.id)


class ScheduledBackupDeleteView(generic.View):
    def get(self, request, pk):
        instance = get_object_or_404(models.BackupSchedule, id=pk)
        return render(request, "backup_schedule/delete_backup_schedule.html", {
            "object": instance
        })

    def post(self, request, pk):
        instance = get_object_or_404(models.BackupSchedule, id=pk)
        database_id: str = instance.database.id
        instance.delete()
        return redirect("scheduled-backups", database_id=database_id)
