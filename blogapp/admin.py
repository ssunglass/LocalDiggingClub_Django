from django.contrib import admin
from .models import Blog
from .models import User


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'registered_dttm', 'status')

admin.site.register(Blog, BlogAdmin)
admin.site.register(User, UserAdmin)
