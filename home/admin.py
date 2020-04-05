from django.contrib import admin

# Register your models here.
from home.models import Settings,ContactFormMessage

class ContactForMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status','subject']
    list_filter = ['status']

admin.site.register(Settings)
admin.site.register(ContactFormMessage,ContactForMessageAdmin)