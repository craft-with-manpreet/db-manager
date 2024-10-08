# Author: Manpreet Singh
# Email: dev.manpreet.io@gmail.com
# GitHub: https://github.com/craft-with-manpreet
# Portfolio: https://dev-manpreet.web.app
from django.views import generic
from database_management import models
from django.shortcuts import get_object_or_404, render, redirect
from database_management.forms import ScheduleBackupForm
from database_management.scheduler import scheduler_instance, get_trigger
from database_management.utils import func_backup_database


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
            "object_list": objects
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
        form = ScheduleBackupForm(data=request.POST, initial={
            "database": database
        })
        if not form.is_valid():
            return render(request, "backup_schedule/create_backup_schedule.html", {
                "form": form
            })

        scheduled_backup: models.BackupSchedule = form.save()
        scheduled_backup.database = database
        scheduled_backup.save()
        scheduler_instance.add_job(func_backup_database, args=[database_id],
                                   trigger=get_trigger(scheduled_backup.frequency),
                                   id=str(scheduled_backup.id))

        return redirect("scheduled-backup-list", database_id=database_id)


class ScheduledBackupUpdateView(generic.View):
    def get(self, request, pk):
        instance = get_object_or_404(models.BackupSchedule, id=pk)
        form: ScheduleBackupForm = ScheduleBackupForm(instance=instance)
        return render(request, "backup_schedule/update_scheduled_backup.html", {
            "form": form,
            "object": instance
        })

    def post(self, request, pk):
        instance = get_object_or_404(models.BackupSchedule, id=pk)
        form: ScheduleBackupForm = ScheduleBackupForm(data=request.POST, instance=instance, initial={
            "database": instance.database,
        })
        if not form.is_valid():
            return render(request, "backup_schedule/update_scheduled_backup.html", {
                "form": form,
                "object": instance
            })

        form.save()
        try:
            scheduler_instance.add_job(func_backup_database, args=[instance.database.id],
                                       trigger=get_trigger(instance.frequency),
                                       id=str(pk), replace_existing=True)
        except Exception as e:
            print(e)
        return redirect("scheduled-backup-list", database_id=instance.database.id)


class ScheduledBackupDeleteView(generic.View):
    def get(self, request, pk):
        instance = get_object_or_404(models.BackupSchedule, id=pk)
        return render(request, "backup_schedule/remove_scheduled_backup.html", {
            "object": instance
        })

    def post(self, request, pk):
        instance = get_object_or_404(models.BackupSchedule, id=pk)
        database_id: str = instance.database.id
        instance.delete()
        try:
            scheduler_instance.remove_job(pk)
        except Exception as e:
            print(e)
        return redirect("scheduled-backup-list", database_id=database_id)
