from django.contrib import admin
from django.urls import path, include
from .views import home,submit_registration
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('create/', views.create_hackathon, name='create_hackathon'),
    path('hackathon/<int:pk>/', views.hackathon_details, name='hackathon_details'),
    path('register/', views.register_hackathon, name='register_hackathon'),
    path('submit_registration/', views.submit_registration, name='submit_registration'),# Changed path to 'register/'
    path('viewsubmission/', views.view_submission, name='view_submissions'),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('api/', include('submission.urls')),
]
