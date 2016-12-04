from django.contrib import admin

# Register your models here.
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'tid')


# admin.site.register()
admin.site.register(Teacher, TeacherAdmin)
