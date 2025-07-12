from django.urls import path
from .views import EmailServiceView 



urlpatterns = [
    path('send-email/', EmailServiceView.as_view(), name='send_email'),
]