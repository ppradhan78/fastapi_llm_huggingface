# 🚀 Hugging Face FastAPI Chat Service

A structured FastAPI application integrated with Hugging Face, built
using clean architecture principles (routers → services → core →
exceptions).

---

## 📦 Project Setup

### 1️⃣ Clone the Repository

git clone `<your-repository-url>`{=html} cd huggingface_fastapi

---

### 2️⃣ Create Virtual Environment

python -m venv venv

---

### 3️⃣ Activate Virtual Environment

Windows:

.`\venv`{=tex}`\Scripts`{=tex}`\activate`{=tex}

Mac/Linux:

source venv/bin/activate

---

### 4️⃣ Install Dependencies

pip install -r requirements.txt

---

## ⚙️ Environment Configuration

Create a `.env` file in the project root:

HF_TOKEN=your_huggingface_token_here

---

## 🧾 config.toml

Place `config.toml` in the project root:

\[model\] name = "your-model-name" max_tokens = 200

---

## ▶️ Run the Application

From the project root:

uvicorn app.main:app --reload

The API will be available at: http://127.0.0.1:8000

Swagger documentation: http://127.0.0.1:8000/docs

---

## 🏗 Project Structure

huggingface_fastapi/
│
├── app/
│ │
│ ├── main.py
│ │
│ ├── core/
│ │ ├── config.py
│ │ ├── logging_config.py
│ │ └── exception_handler.py
│ │
│ ├── exceptions/
│ │ └── custom_exceptions.py
│ │
│ ├── routers/
│ │ └── chat.py
│ │
│ ├── services/
│ │ └── chat_service.py
│ │
│ ├── utility/
│ │ └── hf_client.py
│ │
│ ├── models/
│ │ └── chat_models.py
│ │
│ └── **init**.py
│
├── config.toml
├── .env
├── requirements.txt
├── README.md
└── .gitignore

---

## 🧠 Architecture Overview

- Routers → Handle HTTP layer
- Services → Business logic
- Core → Configuration, logging, global exception handling
- Exceptions → Custom domain exceptions

Clean separation of concerns. Production ready structure.
Folder Responsibilities
🔹 app/main.py

FastAPI app creation

Register routers

Register global exception handlers

Initialize logging

🔹 app/core/
config.py

Load config.toml

Load environment variables

Validate required settings

logging_config.py

Centralized logging configuration

Structured logging setup

exception_handler.py

Global FastAPI exception handlers

Maps custom exceptions → HTTP responses

🔹 app/exceptions/
custom_exceptions.py

Base AppException

ConfigurationException

ExternalServiceException

ValidationException

No FastAPI imports here. Pure domain logic.

🔹 app/routers/
chat.py

HTTP endpoints

Calls service layer

No business logic

No heavy try/except blocks

🔹 app/services/
chat_service.py

Business logic

Hugging Face integration

Raises custom exceptions

Logs technical failures

🔹 app/utility/
hf_client.py

Creates and configures Hugging Face client

Isolated external integration layer

🔹 app/models/
chat_models.py

Pydantic request/response models

Validation schemas

🧠 Architecture Flow
Client Request
↓
Router
↓
Service
↓
Utility (HF client)
↓
External API

Exceptions bubble up → handled globally → consistent JSON response.
