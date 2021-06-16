from django.urls import path
from . import views
#本地路由
urlpatterns = [
    path('',views.hello)
]
