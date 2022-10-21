from django.urls import path

from .views import CreateCourseView
from .views import DeleteCourseView
from .views import DetailCourseView
from .views import ListCourseView
from .views import UpdateCourseView

app_name = 'courses'

urlpatterns = [
    path('', ListCourseView.as_view(), name='list'),
    path('create/', CreateCourseView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailCourseView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateCourseView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteCourseView.as_view(), name='delete'),
]
