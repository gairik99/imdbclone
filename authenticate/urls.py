from .  import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    # path('watchlist/', views.get_watchlists, name='get_watchlists'),
    # path('watchlist/<int:pk>/', views.get_watchlist, name='get_watchlist'),
    path('watchlist/', views.WatchListListCreateView.as_view(), name='get_watchlists'),
    path('watchlist/<int:pk>/', views.WatchListDetailView.as_view(), name='get_watchlist'),
    path('streamingservice/', views.StreamingServiceListCreateView.as_view(), name='get_streamingservices'),
    path('streamingservice/<int:pk>/', views.StreamingServiceDetailView.as_view(), name='get_streamingservice'),
    # path('streamingservice/<int:pk>/', views.get_streaming_service, name='get_streamingservice'),
    # path('streamingservice/', views.get_streaming_services, name='get_streamingservices'),
    # path('review', views.ReviewList.as_view(), name='get_reviews'),
    # path('review/<int:pk>', views.ReviewDetail.as_view(), name='get_reviews'),
    path('watchlist/<int:pk>/review/', views.ReviewList.as_view(), name='get_reviews'),
    path('watchlist/<int:pk>/create-review/', views.CreateReview.as_view(), name='create_review'),
    path('watchlist/review/<int:pk>/', views.ReviewDetail.as_view(), name='get_review'),
    
    
    # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
]

