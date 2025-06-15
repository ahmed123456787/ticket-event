from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from ticket_system.schema import schema
from ticket_system.views import PrivateGraphQLView, check_auth_status, LoginView, LogoutView

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
]
