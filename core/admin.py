from django.contrib import admin
from .models import SchoolModel, StudentModel, ClassModel



# Register your models here.

admin.site.register(SchoolModel)
admin.site.register(StudentModel)
admin.site.register(ClassModel)
