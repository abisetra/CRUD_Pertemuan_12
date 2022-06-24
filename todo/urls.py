from django.urls import path
from .views import *

app_name = 'todo'
urlpatterns = [
    path('', index_view, name='index'),
    path('<int:task_id>/', detail_view, name='detail'),
    path('create/', create_view, name='create'),
    path('<int:task_id>/update/', update_view, name='update'),
    path('<int:task_id>/delete/', delete_view, name='delete'),
]