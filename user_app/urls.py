# from rest_framework.authtoken.views import obtain_auth_token
from .views import register
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    # path('login/', obtain_auth_token, name='login'),
    path('register/', register, name='register'),
    # path('logout/', logout, name='logout'),    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
