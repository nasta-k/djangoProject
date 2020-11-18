from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('user', views.user, name='user_page'),
    path('user/<int:task_id>', views.change_state_by_id, name='change_state'),
]
