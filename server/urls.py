"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserCreateListAPIView.as_view(), name="users"),
    path("users/<int:pk>", UserUpdateDeleteAPIView.as_view(), name='user_detail'),
    path("auth/", include("dj_rest_auth.urls")),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path("api/v1/auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("api/v1/auth/google/callback/",GoogleLoginCallback.as_view(),name="google_login_callback",),
    path("login/", LoginPage.as_view(), name="login"),
]
