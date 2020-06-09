from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index,  name='index'),
    path('addannouncement/<int:id>', views.addcomment, name='addannouncement  ')
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),

]