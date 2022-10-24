from django.urls import path

from .views import AccountLoginView
from .views import AccountLogoutView
from .views import AccountRegisterView

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
]
