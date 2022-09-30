from django.urls import path

from teachers.views import create_teacher
from teachers.views import detail_teacher
from teachers.views import get_teacher
from teachers.views import update_teacher

urlpatterns = [
    path('', get_teacher),
    path('create/', create_teacher),
    path('detail/<int:teacher_id>/', detail_teacher),
    path('update/<int:teacher_id>/', update_teacher),
]
