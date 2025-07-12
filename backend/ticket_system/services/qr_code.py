import qrcode
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from ticket_system.core.models import EventTicket


def generate_ticket_image(ticket: EventTicket) -> BytesIO:
    """Generate an image of the ticket with QR code, user details, and profile picture"""
    try:
        # Create a new image with white background - more realistic ticket size
        width, height = 1000, 400
        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)
        
        # Try to load fonts - use default if custom font fails
        try:
            title_font = ImageFont.truetype('arial.ttf', 28)
            header_font = ImageFont.truetype('arial.ttf', 22)
            text_font = ImageFont.truetype('arial.ttf', 16)
        except IOError:
            title_font = ImageFont.load_default()
            header_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
        
        # Add a border to make it look like a real ticket
        border_width = 3
        draw.rectangle([(border_width, border_width), (width-border_width, height-border_width)], 
                      outline='#3a86ff', width=border_width)
        
        # Add event title
        event_title = ticket.event.name
        draw.text((50, 40), event_title, fill='#333333', font=title_font)
        
        # Add divider line
        draw.line((50, 80, width-270, 80), fill='#3a86ff', width=2)
        
        # Add ticket details
        y_position = 100
        details = [
            f"Ticket Code: {ticket.ticket_code}",
            f"Attendee: {ticket.user.name}",
            f"Event Date: {ticket.event.date.strftime('%d %b %Y')}",
            f"Time: {ticket.event.date.strftime('%I:%M %p')} - {ticket.event.date.strftime('%I:%M %p')}",
            f"Location: {ticket.event.location}",
            f"Price Paid: ${ticket.price_paid:.2f}"
        ]
        
        for detail in details:
            draw.text((50, y_position), detail, fill='#333333', font=text_font)
            y_position += 30
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"TICKET:{ticket.ticket_code}")
        qr.make(fit=True)
        
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img = qr_img.resize((180, 180))
        
        # Paste QR code onto ticket
        image.paste(qr_img, (width-215, 150))
        
        # Add ticket validation text
        draw.text((width-215, 340), "Scan for verification", fill='#666666', font=text_font)
        
        # Save to in-memory file
        buffer = BytesIO()
        image.save(buffer, format='PNG')
        buffer.seek(0)
        
        return buffer
    except Exception as e:
        print(f"Error generating ticket image: {str(e)}")
        
        # Return a basic fallback image
        fallback = Image.new('RGB', (400, 200), color='white')
        draw = ImageDraw.Draw(fallback)
        font = ImageFont.load_default()
        draw.text((10, 10), f"Ticket Code: {ticket.ticket_code}", fill='black', font=font)
        draw.text((10, 30), f"Event: {ticket.event}", fill='black', font=font)
        
        buffer = BytesIO()
        fallback.save(buffer, format='PNG')
        buffer.seek(0)
        
        return buffer