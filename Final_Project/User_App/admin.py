from django.contrib import admin
from .models import *

# Register your models here

class UserSignupAdmin(admin.ModelAdmin):
    list_display =['created', 'fullname', 'email', 'password', 'mobile']
admin.site.register(UserSignup, UserSignupAdmin)


class mynotesAdmin(admin.ModelAdmin):
    list_display =['uploaded_at', 'user', 'title', 'desc', 'subject', 'notes_file', 'status', 'updated_at']
admin.site.register(mynotes, mynotesAdmin)                                                                   