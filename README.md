# SupportPilot AI

**Intelligent Customer Support Platform**

SupportPilot AI is an AI-powered customer support platform designed to make customer support more efficient, accessible, and intelligent. It combines a modern React frontend with a FastAPI backend, Firebase authentication, and a Retrieval-Augmented Generation (RAG) module.

The project aims to provide a foundation for intelligent customer interactions, authenticated access, and AI-assisted support workflows.

## Overview

Traditional customer support systems can involve repetitive queries, slow response times, and inefficient information retrieval.

SupportPilot AI aims to address these challenges by bringing authentication, backend services, and AI-powered support capabilities together in one platform.

## Key Features

- **User Authentication:** Secure registration and login using Firebase Authentication.
- **Protected Routes:** Restrict access to authenticated areas of the application.
- **Backend API:** RESTful API development using FastAPI.
- **Token Verification:** Verify Firebase ID tokens on the backend using Firebase Admin SDK.
- **Frontend Integration:** Connect the React application with backend services through Axios.
- **RAG Module:** Project structure for Retrieval-Augmented Generation capabilities.
- **Modular Architecture:** Organized backend and frontend components for maintainability and future development.

## Technology Stack

### Frontend

| Technology | Purpose |
|---|---|
| React | User interface |
| Vite | Frontend development and build |
| JavaScript | Application logic |
| Axios | API communication |
| Firebase Authentication | User authentication |
| React Router | Client-side navigation |

### Backend

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | REST API framework |
| Firebase Admin SDK | Server-side authentication |
| Pydantic | Data validation |
| Uvicorn | ASGI server |

### AI & Data

- Retrieval-Augmented Generation (RAG)
- Backend database and model modules
- AI-powered customer support capabilities

## Project Architecture

```text
                  SUPPORTPILOT AI
                         |
              +----------+----------+
              |                     |
         React Frontend         FastAPI Backend
              |                     |
       +------+------+        +-----+------+
       |             |        |            |
   Firebase      Axios     Auth API    Core Services
   Auth          Client       |            |
       |             |        |       +----+----+
       |             +------->|       |         |
       |                 HTTP API  Database    RAG
       |                       |
       +---------------- Firebase Admin SDK
```

## Project Structure

```text
supportpilot-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── rag/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── secrets/
│   ├── .env.example
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── config/
│   │   ├── context/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── .env.example
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

## Getting Started

Follow these steps to run SupportPilot AI locally.

### Prerequisites

Make sure you have installed:

- Python 3.10 or later
- Node.js and npm
- Git
- A Firebase project

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd supportpilot-ai
```

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Backend Environment

Create a `.env` file inside the `backend` directory using `.env.example` as a reference.

Configure the Firebase service account path:

```env
FIREBASE_SERVICE_ACCOUNT_PATH=secrets/firebase-service-account.json
```

Download your Firebase Admin SDK service account JSON from the Firebase Console and place it inside:

```text
backend/secrets/firebase-service-account.json
```

**Security:** Never commit your service account JSON or backend `.env` file to GitHub.

### 4. Start the Backend Server

From the `backend` directory, run:

```bash
python -m uvicorn app.main:app --reload
```

Backend API:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 5. Frontend Setup

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

### 6. Configure Frontend Environment

Create a `.env` file inside `frontend` using `.env.example`.

Add your configuration:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000

VITE_FIREBASE_API_KEY=your_firebase_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your_project_id
VITE_FIREBASE_STORAGE_BUCKET=your_storage_bucket
VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
VITE_FIREBASE_APP_ID=your_app_id
```

Replace the placeholder values with your Firebase Web App configuration.

### 7. Start the Frontend

Run:

```bash
npm run dev
```

The frontend will be available at:

```text
http://localhost:5173
```

## Authentication Workflow

SupportPilot AI uses Firebase Authentication for user identity management.

The authentication workflow:

1. Users register or log in through the frontend.
2. Firebase authenticates the user.
3. The frontend retrieves a Firebase ID token.
4. Axios attaches the token to authenticated API requests.
5. FastAPI receives the request and verifies the token through Firebase Admin SDK.
6. Successfully authenticated users can access protected endpoints.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Backend root endpoint |
| GET | `/api/v1/health` | Health check |
| GET | `/api/v1/auth/me` | Retrieve authenticated user information |

## Development Commands

### Frontend

| Command | Description |
|---|---|
| `npm install` | Install dependencies |
| `npm run dev` | Start development server |
| `npm run build` | Create production build |
| `npm run preview` | Preview production build |

### Backend

| Command | Description |
|---|---|
| `pip install -r requirements.txt` | Install Python dependencies |
| `python -m uvicorn app.main:app --reload` | Start development server |

## Security Considerations

- Firebase ID tokens are verified on the backend.
- Protected endpoints require authentication.
- Environment variables are used for configuration.
- Firebase Admin SDK credentials must remain private.
- Never upload `.env` files, service account JSON files, or private credentials to version control.

## Future Development

Planned areas of development include:

- AI-powered customer response generation.
- Knowledge-base integration.
- Advanced RAG pipelines.
- Context-aware customer conversations.
- Conversation history and management.
- Customer support analytics.
- Improved dashboard and support workflows.

## Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Commit your changes with clear commit messages.
5. Submit a pull request.

## License

A license has not yet been specified for this project.

---

**SupportPilot AI**  
*Building smarter and more efficient customer support experiences.*