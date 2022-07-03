from django.urls import path
from crawler import views
from .views import *

urlpatterns = [
    path("",home,name="home_page"),
    path('blog/<str:number>', find_blog, name="find_blog")
]