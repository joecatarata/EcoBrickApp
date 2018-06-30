from django.urls import path, include
from . import views
import django.views.defaults

urlpatterns = [
    path('', views.homepage, name="home"),
    path('staff/',views.staff_view,name="staff"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name= "register"),
    path('profile/<int:userid>', views.user_profile, name="userprofile"),
    path('rewards/', views.rewards, name="rewards"),
    path('logout/', views.logout_view,name="logout"),
    path('partners/', views.partners, name="partners"),
    path('about/',views.about,name="about"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
]
