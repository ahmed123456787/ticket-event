# 🎫 Event Ticketing System 🎟️

<div align="center">

![Django](https://img.shields.io/badge/Django-5.2.1-brightgreen?style=for-the-badge&logo=django&logoColor=white&labelColor=092E20)
![DRF](https://img.shields.io/badge/DRF-3.16.0-red?style=for-the-badge&logo=django&logoColor=white&labelColor=A30000)
![GraphQL](https://img.shields.io/badge/GraphQL-3.4.3-pink?style=for-the-badge&logo=graphql&logoColor=white&labelColor=E10098)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

<p align="center">
A full-featured event ticketing platform backend built with Django, allowing organizers to create events and visitors to purchase tickets with QR code functionality.
</p>

<div align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/main/icons/django.svg" height="40" alt="Django"/>
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/main/icons/python.svg" height="40" alt="Python"/>
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/main/icons/graphql.svg" height="40" alt="GraphQL"/>
</div>

---

## ✨ Features

<table>
  <tr>
    <td>👥 <b>User Management</b></td>
    <td>Multi-role system (Admin, Organizer, Visitor)</td>
  </tr>
  <tr>
    <td>🗓️ <b>Event Management</b></td>
    <td>Create, update, and delete events</td>
  </tr>
  <tr>
    <td>🎟️ <b>Ticket System</b></td>
    <td>Purchase, verify, and check-in with QR codes</td>
  </tr>
  <tr>
    <td>📧 <b>Email Notifications</b></td>
    <td>Send ticket confirmations with embedded QR codes</td>
  </tr>
  <tr>
    <td>🔔 <b>Real-time Notifications</b></td>
    <td>WebSocket-based event reminders</td>
  </tr>
  <tr>
    <td>📊 <b>Analytics</b></td>
    <td>Track event views, purchases, and other interactions</td>
  </tr>
  <tr>
    <td>🔍 <b>GraphQL API</b></td>
    <td>Flexible data querying and manipulation</td>
  </tr>
  <tr>
    <td>🌐 <b>REST API</b></td>
    <td>Standard RESTful endpoints for events and tickets</td>
  </tr>
</table>

## 🛠️ Tech Stack

<details>
<summary><b>🧰 Backend Framework</b></summary>
<br>

- 🟢 Django 5.2.1
- 🔴 Django REST Framework 3.16.0
- 🟣 Graphene (GraphQL) 3.4.3
</details>

<details>
<summary><b>🔐 Authentication</b></summary>
<br>

- 🔑 Django OAuth Toolkit
- 🔓 djangorestframework-simplejwt
- 👤 Social Authentication
</details>

<details>
<summary><b>💾 Database</b></summary>
<br>

- 🗃️ SQLite (development)
- 🔄 Migrations support for other databases in production
</details>

<details>
<summary><b>⚙️ Asynchronous Processing</b></summary>
<br>

- 🔄 Celery for background tasks
- 🚀 Redis for message broker
- 📡 Django Channels for WebSockets
</details>

<details>
<summary><b>📁 Media Handling</b></summary>
<br>

- 🖼️ Pillow for image processing
- 📱 QR Code generation
</details>

<details>
<summary><b>📧 Email Service</b></summary>
<br>

- 📨 SendGrid integration
</details>

<details>
<summary><b>📚 Documentation & Schemas</b></summary>
<br>

- 📝 DRF Spectacular for API documentation
</details>

## 📂 Project Structure

```
event_ticket/backend/
│
├── manage.py                  # Django management script
├── requirements.txt           # Project dependencies
├── client.html                # WebSocket test client
│
├── ticket_system/             # Main Django project
│   ├── __init__.py
│   ├── asgi.py                # ASGI config for async support
│   ├── celery.py              # Celery configuration
│   ├── schedule.py            # Task scheduling
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL routing
│   ├── views.py               # Top-level views
│   ├── wsgi.py                # WSGI configuration
│   │
│   ├── core/                  # Core app with models and base functionality
│   │   ├── models.py          # User, Event, Ticket, Stats models
│   │   ├── serializers.py     # Data serializers
│   │   ├── permissions.py     # Custom permission classes
│   │   ├── admin.py           # Admin interface
│   │   └── manager.py         # Custom user manager
│   │
│   ├── events/                # Events app
│   │   ├── views.py           # Event and Ticket ViewSets
│   │   ├── serializers.py     # Event serializers
│   │   ├── urls.py            # Event URL routing
│   │   ├── consumers.py       # WebSocket consumers
│   │   ├── tasks.py           # Celery tasks
│   │   ├── routing.py         # WebSocket URL routing
│   │   └── middleware.py      # WebSocket auth middleware
│   │
│   ├── services/              # Services app
│   │   ├── email_service.py   # SendGrid email service
│   │   ├── qr_code.py         # QR code generation
│   │   ├── views.py           # Service views
│   │   └── urls.py            # Service URL routing
│   │
│   └── graphql/               # GraphQL app
│       ├── schema.py          # GraphQL schema
│       ├── query.py           # GraphQL queries
│       ├── mutation.py        # GraphQL mutations
│       └── types.py           # GraphQL types
│
├── media/                     # User-uploaded media
│   └── qr_codes/              # Generated ticket QR codes
│
└── staticfiles/               # Static files
```

## 🚀 Setup & Installation

### 📋 Prerequisites

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-required-red?style=for-the-badge&logo=redis&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-optional-orange?style=for-the-badge&logo=rabbitmq&logoColor=white)

</div>

### ⚙️ Installation Steps

<details open>
<summary><b>Step-by-Step Guide</b></summary>

1. **Clone the repository** 📥

   ```bash
   git clone https://github.com/ahmed123456787/ticket-event.git
   cd event_ticket/backend
   ```

2. **Create and activate a virtual environment** 🔮

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies** 📦

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** 🔑

   Create a `.env.dev` file in the project root with:

   ```
   SENDGRID_API_KEY=your_sendgrid_api_key
   ```

5. **Run migrations** 🔄

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** 👑

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server** 🚀
   ```bash
   python manage.py runserver
   ```
   </details>

### 🔧 Additional Services Setup

<details>
<summary><b>Start Required Services</b></summary>

1. **Start Redis server** 🔴

   ```bash
   redis-server
   ```

2. **Run Celery worker** 🧠

   ```bash
   celery -A ticket_system worker -l info
   ```

3. **Run Celery beat** ⏰
   ```bash
   celery -A ticket_system beat -l info
   ```
   </details>

## 📖 API Documentation

<div align="center">

Once the server is running, access the API documentation at:

[![Swagger UI](https://img.shields.io/badge/Swagger_UI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](http://localhost:8000/api/docs/)
[![API Schema](https://img.shields.io/badge/API_Schema-5E97BD?style=for-the-badge&logo=openapi-initiative&logoColor=white)](http://localhost:8000/api/schema/)

</div>

## 🔐 Authentication

<details>
<summary><b>Available Authentication Methods</b></summary>

1. **JWT Authentication** 🔑

   - Get token: `POST /api/token/`
   - Refresh token: `POST /api/token/refresh/`

2. **Session Authentication** 🖥️

   - Login: `POST /api/login/`
   - Logout: `POST /api/logout/`
   - Check status: `GET /api/auth-status/`

3. **OAuth2 Authentication** 🌐
   - OAuth endpoints: `/auth/`
   </details>

## 👥 User Roles

<div align="center">

| Role             | Description                              |
| ---------------- | ---------------------------------------- |
| 👑 **Admin**     | Complete system access                   |
| 🎭 **Organizer** | Create and manage events, verify tickets |
| 🙂 **Visitor**   | Browse events, purchase and use tickets  |

</div>

## 🔍 GraphQL API

<div align="center">

GraphQL API is available at:

[![Public API](https://img.shields.io/badge/Public_API-E10098?style=for-the-badge&logo=graphql&logoColor=white)](/graphql/public/)
[![Private API](https://img.shields.io/badge/Private_API-E10098?style=for-the-badge&logo=graphql&logoColor=white)](/graphql/)

</div>

## 📄 License

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

</div>

---

<div align="center">
  <sub>Built with ❤️ by Ahmed</sub>
</div>
