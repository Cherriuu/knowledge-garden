from django.urls import path
from . import views

app_name = 'learning_log'

urlpatterns = [
    path('', views.index, name='index'), # ' ' for homepage, views.index will call index function when someone visits this url, name = is a nickname for this url
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]