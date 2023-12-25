from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AdvancedAuthenticationForm

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', form_class=AdvancedAuthenticationForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='profile_update')
]