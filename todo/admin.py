from django.contrib import admin
# Register your models here.
from .models import Todo

#Show readonly fields in Admin page
class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Todo,TodoAdmin)