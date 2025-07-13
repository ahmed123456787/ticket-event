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
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/main/icons/docker.svg" height="40" alt="Docker"/>
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

- 🐘 PostgreSQL (via Docker)
- 🔄 Django Migrations
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
<summary><b>🐳 Containerization</b></summary>
<br>

- 🐳 Docker for containerization
- 🔄 Docker Compose for orchestration
- 🌐 Nginx for reverse proxy
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
├── deployment/                # Docker deployment files
│   ├── docker-compose.yml     # Docker Compose configuration
│   ├── Dockerfile             # Docker image definition
│   ├── entrypoint.sh          # Container entry point script
│   └── nginx/                 # Nginx configuration
│       └── default.conf       # Nginx virtual host config
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

![Docker](https://img.shields.io/badge/Docker-required-blue?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-required-blue?style=for-the-badge&logo=docker&logoColor=white)

</div>

### ⚙️ Docker Installation Steps

<details open>
<summary><b>Step-by-Step Guide</b></summary>

1. **Clone the repository** 📥

   ```bash
   git clone https://github.com/ahmed123456787/ticket-event.git
   cd event_ticket
   ```

2. **Set up environment variables** 🔑

   Create a `config/.env` file in the project root with:

   ```
   SENDGRID_API_KEY=your_sendgrid_api_key
   DB_NAME=event_ticket
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=db
   REDIS_HOST=redis
   REDIS_PORT=6379
   ```

3. **Build and start the Docker containers** 🐳

   ```bash
   cd backend/deployment
   docker-compose up -d
   ```

4. **Create a superuser** 👑

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Access the application** 🚀

   The application will be available at:

   ```
   http://localhost:80
   ```

   </details>

### 🔧 Docker Commands Reference

<details>
<summary><b>Useful Docker Commands</b></summary>

1. **Start all services** 🏁

   ```bash
   docker-compose up -d
   ```

2. **Stop all services** 🛑

   ```bash
   docker-compose down
   ```

3. **View logs** 📋

   ```bash
   docker-compose logs -f web  # For web service logs
   docker-compose logs -f      # For all services
   ```

4. **Run Django management commands** 💻

   ```bash
   docker-compose exec web python manage.py <command>
   ```

5. **Rebuild containers after changes** 🔄
   ```bash
   docker-compose up -d --build
   ```
   </details>

## 📖 API Documentation

<div align="center">

Once the server is running, access the API documentation at:

[![Swagger UI](https://img.shields.io/badge/Swagger_UI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](http://localhost/api/docs/)
[![API Schema](https://img.shields.io/badge/API_Schema-5E97BD?style=for-the-badge&logo=openapi-initiative&logoColor=white)](http://localhost/api/schema/)

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

[![Public API](https://img.shields.io/badge/Public_API-E10098?style=for-the-badge&logo=graphql&logoColor=white)](http://localhost/graphql/public/)
[![Private API](https://img.shields.io/badge/Private_API-E10098?style=for-the-badge&logo=graphql&logoColor=white)](http://localhost/graphql/)

</div>

## 📄 License

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

</div>

---

<div align="center">
  <sub>Built with ❤️ by Ahmed</sub>
</div>
