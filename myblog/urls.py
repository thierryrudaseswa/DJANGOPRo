from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index)
    # path('', views.home_view, name='home'),
    # path('contact/', views.contact_view, name='contact'),
    # path('contact/success', views.contact_success_view, name='contact-success')
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    
]