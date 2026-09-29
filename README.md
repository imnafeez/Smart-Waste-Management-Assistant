# ♻️ Smart Waste Management Assistant

A simple, clean, and complete 1-credit college mini project for waste identification, environmental impact awareness, and responsible disposal guidance.

---

## 📌 Project Overview
The **Smart Waste Management Assistant** is a web application designed to help users identify common types of waste and understand proper disposal procedures. Users can describe a waste item or select a common waste category to retrieve instant recommendations, environmental impact information, and handling instructions.

---

## 🎯 Project Objective
> *"To provide a simple and user-friendly tool for basic waste identification and responsible disposal guidance."*

---

## ✨ Features
- **🔍 Waste Identification**: Categorizes waste inputs into 10 common waste streams using a simple keyword-matching knowledge base.
- **🌱 Environmental Impact Awareness**: Displays clear explanations of how specific waste types impact ecosystems.
- **♻️ Disposal & Handling Guidance**: Provides step-by-step basic handling instructions and recommended disposal actions.
- **📜 Analysis History**: Stores analysis records in a local SQLite database for reference.
- **🎨 Professional UI**: Styled dark charcoal interface built with Streamlit and custom CSS.

---

## 🛠️ Technologies Used
- **Language**: Python 3.11+
- **Backend API**: FastAPI & Uvicorn
- **Frontend UI**: Streamlit
- **Database**: SQLite (built-in `sqlite3`)
- **HTTP Client**: Requests

---

## 📐 System Architecture

```text
  User (Web Browser)
        ↓
Streamlit Frontend (Port 8501)
        ↓  (HTTP POST / GET)
FastAPI Backend (Port 8000)
        ↓
Waste Analysis Logic (Keyword Matching)
        ↓
SQLite Database (data/waste.db)
```

---

## 📁 Project Structure

```text
smart-waste-assistant/
│
├── backend/
│   ├── main.py          # FastAPI application & API endpoints
│   ├── waste_logic.py   # Knowledge base & keyword matching algorithm
│   └── database.py      # SQLite database initialization & CRUD helper functions
│
├── frontend/
│   └── app.py           # Streamlit user interface
│
├── data/
│   └── waste.db         # SQLite database file (created automatically)
│
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── run_app.bat          # Windows batch script to launch services
```

---

## 🚀 Installation & Setup

1. **Clone or Navigate to Project Directory**:
   ```bash
   cd smart-waste-assistant
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ How to Run

### Option A: Using `run_app.bat` (Recommended for Windows)
Double-click `run_app.bat` or run:
```cmd
run_app.bat
```
This automatically launches both backend and frontend in separate command windows.

### Option B: Manual Launch

1. **Start FastAPI Backend**:
   ```bash
   python -m uvicorn backend.main:app --reload --port 8000
   ```

2. **Start Streamlit Frontend** (in another terminal):
   ```bash
   python -m streamlit run frontend/app.py
   ```

### Access Links
- **Streamlit Frontend**: [http://localhost:8501](http://localhost:8501)
- **FastAPI Backend**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **FastAPI Interactive Docs (Swagger)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 API Endpoints

### 1. `GET /api/health`
Checks backend status.
- **Response**:
  ```json
  {
    "status": "running"
  }
  ```

### 2. `POST /api/analyze`
Analyzes input waste description or category.
- **Request Body**:
  ```json
  {
    "waste_type": "Plastic bottle"
  }
  ```
- **Response**:
  ```json
  {
    "waste_category": "Plastic Waste",
    "disposal_method": "Place it in the appropriate recyclable/plastic-waste collection bin.",
    "environmental_impact": "Plastic waste can remain in the environment for a long period and may contribute to land and water pollution.",
    "basic_handling": "Empty and rinse the container or bottle completely before recycling. Compress to save space.",
    "recommended_action": "Send it to an authorized recycling or plastic waste collection facility."
  }
  ```

### 3. `GET /api/history`
Returns previously stored analysis records.
- **Response**: List of saved analysis JSON records from SQLite.

---

## 🗄️ Database Schema (`waste_history`)

Stored in `data/waste.db`:

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | `INTEGER` | Primary Key (Auto-increment) |
| `date` | `TEXT` | Timestamp of analysis (`YYYY-MM-DD HH:MM:SS`) |
| `waste_item` | `TEXT` | User text input or category |
| `category` | `TEXT` | Identified waste category |
| `disposal_method` | `TEXT` | Disposal guidance provided |

---

## 🔮 Future Enhancements
- Support for image-based waste classification.
- Location-based mapping to nearest local recycling hubs.
- Support for additional waste categories and multi-language guidance.

---

## ⚠️ Disclaimer
*This is a basic waste-management guidance assistant for academic demonstration. Follow local waste-disposal rules and consult the appropriate waste-management authority when required.*
