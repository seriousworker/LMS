from django.urls import path

from groups.views import create_group
from groups.views import detail_group
from groups.views import get_group
from groups.views import update_group

urlpatterns = [
    path('', get_group),
    path('create/', create_group),
    path('detail/<int:group_id>/', detail_group),
    path('update/<int:group_id>/', update_group),
]
