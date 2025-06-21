from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .email_service import send_email_via_sendgrid
from .serializers import EmailSerializer

class EmailServiceView(GenericAPIView):
    """
    View to handle email service operations.
    """
    serializer_class = EmailSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to send an email.
        """
        email_data = self.get_serializer(data=request.data)
        email_data.is_valid(raise_exception=True)
        send_email_via_sendgrid(
            to_email=email_data.validated_data['recipient_email'],
            subject=email_data.validated_data['subject'],
            html_content=email_data.validated_data['body']
        )

        return Response({"message": "Email sent successfully"}, status=200)