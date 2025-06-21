import sendgrid
from sendgrid.helpers.mail import Mail
from django.conf import settings
import base64
from sendgrid.helpers.mail import Attachment, FileContent, FileType, FileName, Disposition, ContentId


def send_email_via_sendgrid(to_email, subject, html_content,qr_buffer=None):
    print(settings.SENDGRID_API_KEY)  # Debugging line to check if the API key is set
    sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
    message = Mail(
        from_email='ahmed.zater@univ-constantine2.dz',
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    try:

        if qr_buffer:
            encoded_file = base64.b64encode(qr_buffer.getvalue()).decode()
            attachment = Attachment()
            attachment.file_content = FileContent(encoded_file)
            attachment.file_type = FileType('image/png')
            attachment.file_name = FileName('ticket_qr.png')
            attachment.disposition = Disposition('attachment')  # ✅ Downloadable
            message.attachment = attachment
        response = sg.send(message)

        print(f"Email sent with status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")
