import sendgrid
from sendgrid.helpers.mail import Mail
from django.conf import settings

def send_email_via_sendgrid(to_email, subject, html_content):
    print(settings.SENDGRID_API_KEY)  # Debugging line to check if the API key is set
    sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
    message = Mail(
        from_email='ahmed.zater@univ-constantine2.dz',
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    try:
        response = sg.send(message)
        print(f"Email sent with status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")
