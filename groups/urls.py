from django.urls import path

from .views import create_group
from .views import delete_group
from .views import detail_group
from .views import get_group
from .views import update_group

app_name = 'groups'

urlpatterns = [
    path('', get_group, name='list'),
    path('create/', create_group, name='create'),
    path('detail/<int:group_id>/', detail_group, name='detail'),
    path('update/<int:group_id>/', update_group, name='update'),
    path('delete/<int:group_id>/', delete_group, name='delete'),
]
