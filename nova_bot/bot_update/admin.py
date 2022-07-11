from django.contrib import admin

from .models import Login


class LoginAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'chat_id'
    )
    search_fields = ('chat_id',)


admin.site.register(Login, LoginAdmin)
