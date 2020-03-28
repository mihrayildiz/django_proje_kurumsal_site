from django.contrib import admin

# Register your models here.
from announcement.models import Category, Announcement, Images

class AnnouncementImageInline(admin.TabularInline):
    model = Images
    extra =3


class CategoryAdmin(admin.ModelAdmin):
    list_display=['title', 'status', ]
    list_filter = ['status']


class AnnouncementAdmin(admin.ModelAdmin):
    list_display=['title', 'category','price','amount','status', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status','category']
    inlines = [AnnouncementImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display=['title', 'announcement', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(Images,ImagesAdmin)
