from .  import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    path('watchlist', views.get_watchlists, name='get_watchlists'),
    path('watchlist/<int:watchlist_id>/', views.get_watchlist, name='get_watchlist'),
    path('streamingservice', views.get_streaming_services, name='get_streamingservice'),
    path('streamingservice/<int:streaming_service_id>', views.get_streaming_service, name='get_streamingservice'),
    # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
]

