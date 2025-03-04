from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import  ModelForm,TextInput, Textarea
from django.utils.safestring import mark_safe


class Settings(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),

    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    school = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=255)
    smtserver =models.CharField(blank=True,max_length=20)
    smtemail =models.CharField(blank=True,max_length=20)
    smtpassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook =models.CharField(blank=True,max_length=50)
    instagram =models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references =  RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    # create_at = models.DataTimeField(auto_now_add=True)
    # update_at = models.DataTimeFiled(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),

    )
    name = models.CharField(blank = True, max_length=20)
    email= models.CharField(blank = True,max_length=50)
    subject = models.CharField(blank = True,max_length=50)
    message = models.CharField(blank = True,max_length=255)
    status = models.CharField (max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank = True,max_length=20)
    note = models.CharField(blank = True,max_length=100)
    # create_at = models.DataTimeField(auto_now_add=True)
    # update_at = models.DataTimeFiled(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
             'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Name & Surname'}),
             'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
             'email' : TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
             'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows':'5'}),
        }




class UserProfile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(blank =True,max_length=20)
    adress = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    image =models.ImageField(blank=True, upload_to='images/users/')


    def __str__(self):
        return self.user.username

    def user_name(self):
        return  self.user.first_name + ' ' + self.user.last_name + ' ' + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height ="50/>'.format(self.image.url))

    image_tag.short_description = 'Image'



class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'adress', 'city', 'country', 'image']


class FAQ(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),

    )
    ordernumber =models.IntegerField()
    question = models.CharField(max_length=150)
    answer = models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS)
    #created_at
    #updated_at

    def __str__(self):
        return self.question