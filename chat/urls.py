from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index_view, name='chat-index'),
    path('<str:room_name>/', views.room_view, name='chat-room'),
]