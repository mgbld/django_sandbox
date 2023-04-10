from django.urls import path
from . import views


# URL Conf
urlpatterns = [
    # If no pattern error just add a r''
    # path(r'hello/', views.say_hello)
    path('hello/', views.say_hello)
]