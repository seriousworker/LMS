from django.urls import path

from .views import create_teacher
from .views import detail_teacher
from .views import get_teacher
from .views import update_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teacher, name='list'),
    path('create/', create_teacher, name='create'),
    path('detail/<int:teacher_id>/', detail_teacher, name='detail'),
    path('update/<int:teacher_id>/', update_teacher, name='update'),
]
