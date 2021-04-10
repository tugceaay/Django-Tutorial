from django.contrib import admin
from .models import SchoolModel, StudentModel, ClassModel, ParentModel



# Register your models here.

admin.site.register(SchoolModel)
admin.site.register(StudentModel)
admin.site.register(ClassModel)
admin.site.register(ParentModel)
