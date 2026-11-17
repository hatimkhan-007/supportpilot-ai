# SupportPilot AI – Frontend

The frontend of **SupportPilot AI**, an intelligent customer support platform built with React and Vite. It provides a user-friendly interface with Firebase authentication and secure communication with the FastAPI backend.

## Features

- **User Authentication:** Register and log in using Firebase Authentication.
- **Protected Routes:** Restrict dashboard access to authenticated users.
- **Firebase Integration:** Manage user sessions and authentication tokens.
- **API Integration:** Communicate with the FastAPI backend using Axios.
- **Dashboard:** Access the authenticated user area.
- **Environment Configuration:** Manage API and Firebase settings through environment variables.

## Tech Stack

| Technology | Purpose |
|---|---|
| React | UI development |
| Vite | Development server and build tool |
| JavaScript | Application logic |
| Firebase Authentication | User authentication |
| Axios | HTTP requests |
| React Router | Client-side routing |

## Project Structure

```text
frontend/
├── public/
├── src/
│   ├── components/
│   │   └── ProtectedRoute.jsx
│   ├── config/
│   │   └── firebase.js
│   ├── context/
│   │   └── AuthContext.jsx
│   ├── pages/
│   │   ├── Login.jsx
│   │   ├── Register.jsx
│   │   └── Dashboard.jsx
│   ├── services/
│   │   └── api.js
│   ├── App.jsx
│   └── main.jsx
├── .env.example
├── .gitignore
├── package.json
└── vite.config.js
```

## Prerequisites

Make sure you have installed:

- Node.js (LTS recommended)
- npm
- A configured Firebase project
- The SupportPilot AI backend

## Installation

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

## Environment Variables

Create a `.env` file in the frontend root directory using `.env.example` as a template.

Configure the following variables:

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

**Note:** Never commit your `.env` file or Firebase Admin SDK service account credentials.

## Running the Application

Start the Vite development server:

```bash
npm run dev
```

The application will be available at:

```text
http://localhost:5173
```

## Available Scripts

| Command | Description |
|---|---|
| `npm run dev` | Start development server |
| `npm run build` | Build production application |
| `npm run preview` | Preview production build |

## Backend Integration

The frontend communicates with the FastAPI backend through Axios.

The API base URL is configured using `VITE_API_BASE_URL`.

Authenticated requests automatically attach the Firebase ID token:

```text
Authorization: Bearer <firebase_id_token>
```

The backend verifies this token using Firebase Admin SDK before providing access to protected endpoints.

## Authentication Flow

1. A user registers or logs in through Firebase Authentication.
2. Firebase manages the authentication session.
3. The frontend retrieves the user's Firebase ID token.
4. Axios attaches the token to authenticated API requests.
5. FastAPI verifies the token using Firebase Admin SDK.
6. Authorized users can access protected resources.

## Production Build

Generate an optimized production build:

```bash
npm run build
```

The generated files will be available in the `dist/` directory.

## Project

**SupportPilot AI**  
An intelligent customer support platform designed to streamline customer interactions and support operations.

---

*Frontend developed as part of the SupportPilot AI project.*