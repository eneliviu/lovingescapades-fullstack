"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import root_route, HelloView  # , logout_route

urlpatterns = [
    path('', root_route),
    path('hello/', HelloView.as_view(), name='hello'),
    path('admin/', admin.site.urls),

    # For the browsable API login and logout views
    path('api/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('dj-rest-auth/logout/', logout_route),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', 
    #      include('dj_rest_auth.registration.urls')),

    path('', include('user_profiles.urls')),
    path('', include('testimonials.urls')),
    path('', include('trip.urls')),
]
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
