import uuid

from django.db import models
from encrypted_model_fields import fields


class Database(models.Model):
    id = models.TextField(default=uuid.uuid4, primary_key=True, auto_created=True)
    database_type = models.CharField(choices=(("mysql", "My SQL"), ("postgres", "Postgres"),), max_length=30)
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=79, blank=True, null=True, default=None)
    host = fields.EncryptedCharField(max_length=253, help_text="Example: localhost")
    name = fields.EncryptedCharField(max_length=128, help_text="Specify your database name")
    user = fields.EncryptedCharField(max_length=128, help_text="Example: root")
    password = fields.EncryptedCharField(max_length=128, blank=True)
    port = models.DecimalField(max_digits=5, decimal_places=0, default=None, null=True, blank=True)
    is_connected = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class DatabaseLog(models.Model):
    database = models.ForeignKey(Database, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=(
        ("success", "Success"),
        ("failed", "Failed"),
        ("error", "Error")
    ))
    created_at = models.DateTimeField(auto_now_add=True)
