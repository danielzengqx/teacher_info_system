from django.contrib import admin

# Register your models here.
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'tid')


# admin.site.register()
admin.site.register(Teacher, TeacherAdmin)


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from rating.models import Profile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


