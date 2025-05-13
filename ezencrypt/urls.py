from .views import EzEncryptAPI
from django.urls import path


urlpatterns = [
    path('', EzEncryptAPI.as_view()),
    path('encrypt/', EzEncryptAPI.as_view(), name='encrypt-file'),
    path('decrypt/', EzEncryptAPI.as_view(), name='decrypt-file')
]
