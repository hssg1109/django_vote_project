from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'polls'
urlpatterns = [
    path('', views.custom_login, name='index'),
    path('join/',views.join,name='join'),
    path('home/', views.home, name='home'),
    path('poll_detail/<int:pollnum>/', views.poll_detail, name='detail'),
    path('<int:pollnum>/vote/', views.vote, name='vote'),
    path('<int:pollnum>/result/', views.poll_result, name='result'),

    path('login/', views.custom_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('poll_create/',views.poll_create,name='create')


    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

