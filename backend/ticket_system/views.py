from django.http import HttpResponseForbidden, JsonResponse, HttpResponse
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
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from ticket_system.core.models import Event, User, EventStats
# from .services.email_service import track_event_action

# Create a transparent 1x1 pixel for tracking email opens
TRANSPARENT_PIXEL = bytes.fromhex('47494638396101000100800000000000ffffff21f90401000000002c00000000010001000002024401003b')


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
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {'error': 'Please provide both email and password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, email=email, password=password)

        if user:
            django_login(request, user)
            return Response({
                'success': True,
                'user': {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'role': user.role,
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
            'username': request.user.name
        })
    return JsonResponse({'authenticated': False})


@require_GET
def track_email_open(request, tracking_id):
    """
    Track email opens by serving a transparent tracking pixel.
    Expected URL format: /api/track/email/{tracking_id}?event_id={event_id}&user_id={user_id}
    """
    event_id = request.GET.get('event_id')
    user_id = request.GET.get('user_id')
    
    if event_id:
        try:
            event = get_object_or_404(Event, pk=event_id)
            user = None
            
            if user_id:
                user = get_object_or_404(User, pk=user_id)
            
            # Extract client information
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR')
                
            user_agent = request.META.get('HTTP_USER_AGENT')
            
            # Record the email open event
            EventStats.objects.create(
                event=event,
                action_type='email_open',
                user=user,
                ip_address=ip_address,
                user_agent=user_agent,
                referrer=f"Email tracking ID: {tracking_id}"
            )
        except Exception as e:
            # Log the error but don't stop the response
            print(f"Error tracking email open: {str(e)}")
    
    # Always return a transparent 1x1 GIF pixel
    return HttpResponse(TRANSPARENT_PIXEL, content_type='image/gif')

@require_GET
def track_event_view(request, event_id):
    """
    Track event page views
    """
    user_id = request.GET.get('user_id')
    
    try:
        event = get_object_or_404(Event, pk=event_id)
        user = None
        
        if user_id:
            user = get_object_or_404(User, pk=user_id)
            
        # Track the page view
        # track_event_action(event, 'view', user, request)
        
        return HttpResponse(status=204)  # No content response
    except Exception as e:
        return HttpResponse(str(e), status=400)


