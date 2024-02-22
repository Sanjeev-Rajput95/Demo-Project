from django.urls import path
from . import views

urlpatterns = [
   path('demo_url/', views.demo),
    path('demo1_url/', views.demo1),
   # path('user_app/', include('user_app.urls')),
 ]
