# 🚀 MCP-Based AI Agent using Google ADK

## 📌 Overview

This project demonstrates a **production-style AI agent** built using:

- **Google Agent Development Kit (ADK)**
- **Model Context Protocol (MCP)**
- **Google Cloud Run**

The agent connects to external tools through an MCP server, retrieves structured data, and generates intelligent responses.

This project showcases how modern AI systems can **separate reasoning from tool execution** and interact with real-world systems in a scalable way.

---

## 🧠 Architecture
User
↓
AI Agent (ADK)
↓
MCP Client
↓
MCP Server (Cloud Run)
↓
External Tools (Maps + Database)
↓
AI Agent generates response

---

## ⚙️ Features

- ✅ AI Agent built using ADK principles  
- ✅ MCP-based tool integration  
- ✅ Multi-tool support (Location + Database)  
- ✅ Real-time structured data retrieval  
- ✅ Cloud Run deployment (serverless)  
- ✅ Scalable and modular architecture  
- ✅ REST API interface  

---

## 🛠️ Tech Stack

- Python  
- Google ADK (Agent Development Kit)  
- FastAPI  
- Google Cloud Run  
- Google Cloud Build  
- Docker  
- REST APIs  
- MCP (Model Context Protocol)  

---

## 📂 Project Structure
mcp-agent/
├── adk_agent/ # AI Agent (ADK)
│ ├── agent.py
│ ├── init.py
│ └── requirements.txt
│
├── mcp_tools_server/ # MCP Tool Server
│ ├── server.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── agent/ # Deployed API Agent (Cloud Run)
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
│
└── README.md

---

## 🔗 Live Deployment

### 🌐 AI Agent (Cloud Run)
https://pune-travel-agent-259827495710.asia-south1.run.app


### 🌐 MCP Server (Tools)

https://mcp-tools-server-259827495710.asia-south1.run.app


---

## 🧪 API Usage

### Get travel recommendations


GET /ask?city=Pune


### Example:

```bash
curl "https://pune-travel-agent-259827495710.asia-south1.run.app/ask?city=Pune"
Sample Response:
{
  "city": "Pune",
  "places": [
    {
      "place": "Shaniwar Wada",
      "category": "Historical Fort",
      "timings": "8:00 AM - 6:30 PM",
      "ticket_price": "₹25"
    }
  ],
  "answer": "Top places to visit in Pune..."
}
```
🚀 How to Run Locally
1. Clone repo
git clone https://github.com/Rajnandini-Patil-30/Mcp-Agent.git
cd Mcp-Agent
2. Set environment variable
export MCP_URL=https://mcp-tools-server-259827495710.asia-south1.run.app
3. Run ADK Web UI
adk web
☁️ Deployment (Cloud Run)
Deploy MCP Server
gcloud run deploy mcp-tools-server \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated
Deploy Agent
gcloud run deploy pune-travel-agent \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars MCP_URL=<MCP_URL>
