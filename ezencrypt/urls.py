from .views import EzEncryptAPI
from django.urls import path


urlpatterns = [
    path('', EzEncryptAPI.as_view()),
	path('create/encrypt/', EzEncryptAPI.as_view())
]