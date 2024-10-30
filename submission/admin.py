from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Hackathon

@admin.register(Hackathon)
class HackathonAdmin(admin.ModelAdmin):
    list_display = ('title','description','start_date','end_date')
    search_fields = ('username','email', 'first_name','last_name')
    

admin.site.unregister(User)
   



