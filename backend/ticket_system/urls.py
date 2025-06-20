from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from ticket_system.schema import schema
from ticket_system.views import PrivateGraphQLView, check_auth_status, LoginView, LogoutView, track_email_open, track_event_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView





urlpatterns = [
    path('admin/', admin.site.urls),
    # Public GraphQL endpoint (if needed)
    path('graphql/public/', GraphQLView.as_view(graphiql=True, schema=schema)),
    # Private GraphQL endpoint requiring authentication
    path('graphql/', PrivateGraphQLView.as_view(graphiql=True, schema=schema)),
    # REST Framework Auth endpoints
    path('api/auth-status/', check_auth_status, name='auth_status'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/track/email/<str:tracking_id>', track_email_open, name='track_email_open'),
    path('api/track/view/<int:event_id>', track_event_view, name='track_event_view'),
    path('',include('ticket_system.events.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
