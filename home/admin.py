from django.contrib import admin

# Register your models here.
from home.models import Settings, ContactFormMessage, UserProfile, FAQ


class ContactForMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status','subject']
    list_filter = ['status']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','adress','city','country','image_tag']


class FAQAdmin(admin.ModelAdmin):
    list_display = [ 'ordernumber', 'question', 'answer', 'status',]
    list_filter = ['status']

admin.site.register(Settings)
admin.site.register(ContactFormMessage,ContactForMessageAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(FAQ,FAQAdmin)
