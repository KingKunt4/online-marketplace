from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, forms

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(authentication_form=forms.LoginForm), name='login')
]