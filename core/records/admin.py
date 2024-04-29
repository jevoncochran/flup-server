from django.contrib import admin
from .models import User, Application

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name']

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'position', 'employment_status', 'salary_min', 'salary_max', 'location', 'is_confirmed', 'source', 'link', 'follow_up_date_1', 'follow_up_date_2', 'has_received_response', 'has_received_interview_invitation', 'was_rejected', 'notes', 'user']

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Application, ApplicationAdmin)

    
    