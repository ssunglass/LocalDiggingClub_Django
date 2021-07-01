from django.contrib import admin
from .models import Blog, User, Banner



# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'registered_dttm', 'status','is_superuser', 'is_active')
    list_display_links = ('email', )
    exclude = ('password', )

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title','location')

admin.site.register(Blog, BlogAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Banner, BannerAdmin)
