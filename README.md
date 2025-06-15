# TripVault Microservice

**TripVault Microservice** is a lightweight Python-based microservice designed for:

- 🧭 Optimal travel path generation based on user-defined constraints (budget, distance, rating, etc.)
- 🗣️ Natural language prompt processing via a custom Named Entity Recognition (NER) model

This microservice is part of the **TripVault** platform and communicates with the main backend via HTTP endpoints.

---

## 🚀 Features

- Beam Search–based pathfinding algorithm tailored for cultural trip planning
- Domain-specific NER model using `spaCy` for extracting user preferences from prompts
- FastAPI-powered web API for handling requests from the main application
- Modular and scalable for integration into microservice architectures

---

## 🛠 Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- spaCy (with the appropriate model)
- Any other dependencies listed in `requirements.txt`

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/tripvault-microservice.git
cd tripvault-microservice
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Service

Use `uvicorn` to start the FastAPI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

> Replace `main:app` with the actual Python module and FastAPI app instance if different.

The service will be available at:  
📍 [http://localhost:8000](http://localhost:8000)

Swagger documentation is available at:  
📚 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📄 License

This project is part of the TripVault research thesis. Usage and distribution may be subject to academic licensing terms.

---

## 👤 Author

**Alex-Matei Ignat**  
BSc Computer Science, 2025  
Babes-Bolyai University
