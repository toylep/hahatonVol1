from django.urls import path,include
from community.views import CreateUserView,SessionCreateView,SessionGetView,GetUserView
urlpatterns = [
    path('reg/',CreateUserView.as_view()),
    path('session/',SessionCreateView.as_view()),
    path('session/get',SessionGetView.as_view()),
    path('session/user',GetUserView.as_view()),
]
