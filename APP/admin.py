from django.contrib import admin

from .models import ClassRoom , College , Student , Teacher
# Register your models here.

admin.site.register(College)
admin.site.register(ClassRoom)
admin.site.register(Student)
admin.site.register(Teacher)

