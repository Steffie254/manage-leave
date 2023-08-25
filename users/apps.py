from users.apps import AppConfig
from django.contrib import admin
from users.models import Role,Department,Employee


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"



admin.site.register(Role)
admin.site.register(Department)

admin.site.register(Employee)