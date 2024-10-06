from django.urls import path
from .views import registration_page, login_page


urlpatterns = [
    path('registration/', registration_page),
    path('login/', login_page)
]