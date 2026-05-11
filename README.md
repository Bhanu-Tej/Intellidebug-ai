# 🚀 IntelliDebug AI

An AI-Powered Debugging Intelligence & Observability Platform built to practically understand modern AI system architecture including semantic retrieval, vector search, workflow orchestration, and contextual AI reasoning.

---

# 📌 Project Goal

This project was developed as a hands-on AI engineering learning platform to understand how modern AI systems work internally beyond basic chatbot development.

The focus was on implementing:

- Semantic Retrieval
- Embeddings
- Vector Databases
- Retrieval-Augmented AI Workflows
- LangGraph Orchestration
- Context-Aware AI Recommendations
- Full-Stack AI Architecture

---

# 🧠 Key AI Concepts Implemented

✅ Embeddings using Sentence Transformers  
✅ Semantic Search using FAISS  
✅ Retrieval-Augmented AI Workflows  
✅ LangGraph Agentic Workflow Orchestration  
✅ Contextual AI Reasoning  
✅ Vector-Based Historical Failure Retrieval  
✅ Stateful AI Workflow Pipelines  

---

# ⚙️ Features

- Analyze backend/API failures
- Categorize failures intelligently
- Retrieve semantically similar historical issues
- Generate contextual debugging recommendations
- Track failure severity analytics
- Visualize observability metrics through React dashboard
- AI-powered workflow orchestration using LangGraph

---

# 🏗️ System Architecture

```text
Frontend Dashboard (React)
        ↓
FastAPI Backend
        ↓
Failure Classification Engine
        ↓
Embedding Generator
        ↓
FAISS Semantic Retrieval
        ↓
LangGraph Workflow Orchestration
        ↓
Contextual AI Recommendation Engine
        ↓
SQLite Persistence
🔍 AI Workflow
Error Input
    ↓
Classification Node
    ↓
Embedding Generation
    ↓
Semantic Retrieval
    ↓
Context Building
    ↓
AI Recommendation
    ↓
Final Response

🖥️ Dashboard Features

Failure Analytics
Severity Tracking
Historical Failure Monitoring
AI Insights Panel
Semantic Similarity Visualization
Contextual AI Recommendations
Pie Chart Observability Metrics

🛠️ Tech Stack

Backend
FastAPI
SQLAlchemy
SQLite
LangGraph
Sentence Transformers
FAISS
Frontend
React
TailwindCSS
Recharts
Axios

📊 Example AI Response
{
  "severity": "MEDIUM",
  "category": "AUTH",
  "similar_errors": [
    "invalid token detected"
  ],
  "contextual_ai_recommendation":
    "Verify token expiration and inspect authentication middleware."
}

📂 Project Structure

intellidebug-ai/

├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── database/
│   │   ├── embeddings/
│   │   ├── models/
│   │   ├── retrievers/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   │
│   └── package.json
│
├── README.md
└── .gitignore

🚀 Local Setup

Backend Setup
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload

Backend runs on:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs

Frontend Setup
cd frontend

npm install

npm run dev

Frontend runs on:

http://localhost:5173


📚 What I Learned

This project helped me practically understand:

Embeddings & Vector Search
Semantic Retrieval Systems
Retrieval-Augmented AI Architecture
LangGraph Agentic Workflows
AI Workflow Orchestration
Full-Stack AI Integration
Observability Engineering Concepts
Context-Aware AI Reasoning

👨‍💻 Author

Bhanu Tej