from .  import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path('movies', views.get_movies, name='get_movies'),
    path('movies/<int:movie_id>/', views.get_movie, name='get_movie'),
    # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
]

