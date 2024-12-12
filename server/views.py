from rest_framework import permissions, generics, serializers
from django.contrib.auth.models import User
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from urllib.parse import urljoin
import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from secret import *
from django.shortcuts import render
from django.views import View

class LoginPage(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "login.html",
            {
                "google_callback_uri": GOOGLE_OAUTH_CALLBACK_URL,
                "google_client_id": GOOGLE_OAUTH_CLIENT_ID,
            },
        )


class GoogleLoginCallback(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        token_endpoint_url = urljoin("http://localhost:8000", reverse("google_login"))
        response = requests.post(url=token_endpoint_url, data={"code": code})

        return Response(response.json(), status=status.HTTP_200_OK)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/api/v1/auth/google/callback/"
    client_class = OAuth2Client

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]



class UserUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]



