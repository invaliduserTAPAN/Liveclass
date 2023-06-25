# streaming_app/urls.py

from django.urls import path
from streaming_app.views import streaming_view

urlpatterns = [
    path('', streaming_view, name='streaming'),
    
]
