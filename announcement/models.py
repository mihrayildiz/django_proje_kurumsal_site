from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.db import models
#from ckeditor.widgets import CKEditorWidget
# Create your models here.
from django.forms import ModelForm, Select, TextInput, FileInput
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category (MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),

    )

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    # create_at = models.DataTimeField(auto_now_add=True)
    # update_at = models.DataTimeFiled(auto_now_add=True)



    class MPTTMeta:

        order_insertion_by = ['title']


    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])


    def image_tag(self):
        return mark_safe('<img src="{}" height ="50/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Announcement(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),

    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    detail = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    # create_at = models.DataTimeField(auto_now_add=True)
    # update_at = models.DataTimeFiled(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height ="50/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('announcement_detail', kwargs={'slug': self.slug})




class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['category', 'title', 'slug', 'image', 'keywords', 'description', 'detail']
        widgets = {
            'category': Select(attrs={'class': 'input', 'placeholder': 'type'}, choices=Category.objects.all()),
            'title': TextInput(attrs={'class': 'input', 'placeholder': 'title'}),
            'slug': TextInput(attrs={'class': 'input', 'placeholder': 'slug '}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
            'keywords': TextInput(attrs={'class': 'input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'description'}),
            'detail':  CKEditorWidget(),
        }


class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),

    )

    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank = True)
    comment = models.TextField(max_length=200,blank = True)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS,default="New")
    ip = models.CharField(blank=True, max_length=20)
    # create_at = models.DataTimeField(auto_now_add=True)
    # update_at = models.DataTimeFiled(auto_now_add=True)




    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment','rate']

class Images (models.Model):
    announcement = models.ForeignKey(Announcement,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height ="50/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class AnnouncementImageForm(ModelForm):
    class Meta:
        model = Images
        fields = ['title','image']











