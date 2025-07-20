# 🤖 WhatsApp Lead Extraction Bot

This AI-powered FastAPI app reads raw WhatsApp chat exports (`.txt` files) and returns structured, CRM-ready JSON output. It's designed to help sales and support teams quickly extract lead information like name, email, interest, timeline, and more — with zero manual effort.

---

## Tech Stack

- ⚙️ **FastAPI** — Backend API for file upload and LLM response
- 🤖 **LangChain + LLM (e.g., Groq)** — For intelligent lead extraction
- 🧹 **Regex Cleaning** — To parse unstructured WhatsApp chat formats
- 🌐 **Vanilla JS** — Simple frontend for file upload and viewing results

---

## Features

- Upload WhatsApp `.txt` file directly
- Automatically extracts:
  - Name
  - Company
  - Email
  - Phone
  - Interest
  - Usage
  - Timeline
  - Location
  - Budget
  - Notes
  - Source (always `"WhatsApp"`)
- Flags missing fields using `"N/A"`
- Returns clean JSON — ready to copy into CRM tools

---

## How to Run

### 1. Clone the Project

```bash
git clone https://github.com/gauravjha9/whatsapp-chat-extract.git
cd whatsapp-chat-extract
```

### 2. Backend setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt 
```

### 3. Setup .env file

APP_NAME="WhatsApp Lead Extraction Bot"
APP_ENV=development
APP_DEBUG=True
APP_VERSION=1.0.0
API_VERSION=v1

GROQ_API_KEY=your-groq-api-key



### 4. Start FastAPI Server
```bash
fastapi dev
```

### 5. Frontend
1. Open frontend/index.html in your browser.
2. Choose a file (Text).
3. Click Upload & Extract.
4. JSON response will appear below.