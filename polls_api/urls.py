from django.urls import path, include
from .views import *

urlpatterns = [
    path('poll/', PollList.as_view(), name='poll_list'),
    path('user/',UserList.as_view()),
    path('user/<int:pk>/',UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]