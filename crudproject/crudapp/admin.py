from django.contrib import admin

from crudapp.models import Student

# Register your models here.
@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','roll','name','age','address','city','state','zip']