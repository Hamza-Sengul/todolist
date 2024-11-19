from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Task

admin.site.unregister(User)  # Varsayılan kullanıcıyı kaldır
admin.site.register(User, UserAdmin)  # Kendi admin görünümümüzle tekrar ekle


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_completed')
    list_filter = ('is_completed', 'user')
    search_fields = ('title', 'description', 'user__username')