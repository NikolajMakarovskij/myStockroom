import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


#
# AUTH
def get_csrf(request):
    """_get_csrf_ Returns the CSRF token in a JSON response.

    Args:
        request (_type_):

    Returns:
        response (X-CSRFToken & JSON):
    """

    response = JsonResponse({"detail": "CSRF cookie set"})
    response["X-CSRFToken"] = get_token(request)
    return response


@require_POST
def login_view(request):
    """_login_view_ Authenticates and logs in a user.

    Args:
        request (_type_):

    Returns:
        response (JSON):
    """

    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    if username is None or password is None:
        return JsonResponse(
            {"detail": "Please provide username and password."}, status=400
        )

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"detail": "Invalid credentials."}, status=400)

    login(request, user)
    return JsonResponse({"detail": "Successfully logged in."})


def logout_view(request):
    """_logout_view_ Logs out a user.

    Args:
        request (_type_):

    Returns:
        response (JSON):
    """

    if not request.user.is_authenticated:
        return JsonResponse({"detail": "You're not logged in."}, status=400)

    logout(request)
    return JsonResponse({"detail": "Successfully logged out."})


class SessionView(APIView):
    """_SessionView_ View user sessions.

    Other parameters:
        authentication_classes (SessionAuthentication, BasicAuthentication):
        permission_classes (IsAuthenticated):
    """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        """_get_ Returns the authenticated user's session.

        Args:
            request (_type_):

        Returns:
            response (JSON):
        """

        return JsonResponse(
            {"isAuthenticated": True, "username": request.user.username}
        )


class WhoAmIView(APIView):
    """_WhoAmIView_ View the authenticated user's username.

    Other parameters:
        authentication_classes (SessionAuthentication, BasicAuthentication):
        permission_classes (IsAuthenticated):
    """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        """_get_ Returns the authenticated user's username.

        Args:
            request (_type_):

        Returns:
            response (JSON):
        """

        return JsonResponse({"username": request.user.username})
