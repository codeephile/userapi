from django.contrib import admin
from django.urls import path, include
from users.views import UserTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', UserTokenObtainPairView.as_view(), 
         name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(),  
         name='token_refresh'),

    path('api/', include('users.urls')),
    path('api/', include('music.urls')),
]