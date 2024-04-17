from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'polls'
urlpatterns = [
    path('', views.custom_login, name='index'),
    path('home/', views.home, name='home'),
    path('poll_detail/<int:pollnum>/', views.poll_detail, name='detail'),
    path('poll_result/<int:pollnum>/', views.poll_result, name='result'),
    
    path('login/', views.custom_login, name='login'),
    path('join/', views.join, name='join'),

    #path('home/<int:votenum>/', views.get_vote, name='get_vote'),

    path('poll_create/', views.poll_create, name='poll_create'),


    path('logout/', LogoutView.as_view(), name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

