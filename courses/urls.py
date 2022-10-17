from django.urls import path

from .views import create_course
from .views import delete_course
from .views import detail_course
from .views import get_course
from .views import update_course

app_name = 'courses'

urlpatterns = [
    path('', get_course, name='list'),
    path('create/', create_course, name='create'),
    path('detail/<int:course_id>/', detail_course, name='detail'),
    path('update/<int:course_id>/', update_course, name='update'),
    path('delete/<int:course_id>/', delete_course, name='delete'),
]
