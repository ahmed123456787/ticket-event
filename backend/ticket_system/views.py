from django.http import HttpResponseForbidden, JsonResponse
from graphene_django.views import GraphQLView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login as django_login, logout as django_logout



class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    """
    Custom GraphQL view that requires user authentication.
    Supports both session-based authentication and custom auth methods.
    """
    login_url = '/admin/login/'  # URL to redirect to for login
    redirect_field_name = 'next'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # Check for session authentication
        if request.user.is_authenticated:
            # User is already authenticated via session
            return super().dispatch(request, *args, **kwargs)
        
        # For programmatic API login (optional)
        if request.method == 'POST' and request.headers.get('X-Auth-Method') == 'credentials':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Create a session
                return super().dispatch(request, *args, **kwargs)
        
        return HttpResponseForbidden("Authentication required")




class LoginView(APIView):
    """
    REST API view for user login.
    Returns a session cookie when authentication succeeds.
    """
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, name=username, password=password)

        if user:
            django_login(request, user)
            return Response({
                'success': True,
                'user': {
                    'id': user.id,
                    'username': user.name,
                    'email': getattr(user, 'email', ''),
                    'is_staff': user.is_staff,
                }
            })
        else:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )



class LogoutView(APIView):
    """
    REST API view for user logout.
    Destroys the session.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        django_logout(request)
        return Response({'success': True, 'message': 'Logged out successfully'})


# Add a session status check endpoint (optional but helpful)
def check_auth_status(request):
    """
    Simple endpoint to check if the user has an active session.
    """
    if request.user.is_authenticated:
        return JsonResponse({
            'authenticated': True,
            'username': request.user.username
        })
    return JsonResponse({'authenticated': False})
