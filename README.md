.: # 🤖 Nemotron Auto-Dev Agent

An AI-powered autonomous coding assistant built for the **Nebius x NVIDIA Global AI Hackathon**. This project leverages NVIDIA's state-of-the-art Nemotron models hosted on Nebius Token Factory to generate production-ready code, tests, and documentation from natural language requirements.

---

## ✨ Features
- **Natural Language to Code**: Instantly translates software requirements into clean, structured code.
- **Powered by NVIDIA Nemotron**: Utilizes high-performance models (`Nemotron-3-Ultra-550b-a55b`) for complex software engineering tasks.
- **Nebius Token Factory Integration**: Optimized for fast and scalable AI inference using Nebius infrastructure.
- **Interactive Web Interface**: Built with Streamlit for seamless user interaction and real-time code generation.

---

## 🏗️ Project Architecture
```text
nemotron-auto-dev-agent/
├── app.py                 # Streamlit Frontend UI
├── agent.py               # Core Auto-Dev Agent logic (Nemotron integration)
├── prompts.py             # Optimized system and user prompts
├── config.py              # Configuration settings and API endpoints
└── requirements.txt       # Project dependencies
.: 🚀 Quick Start & Installation
.: Clone the Repository:
.: git clone [https://github.com/aml00zayed-alt/nemotron-auto-dev-agent.git](https://github.com/aml00zayed-alt/nemotron-auto-dev-agent.git)
cd nemotron-auto-dev-agent
.: Install Dependencies:
.: pip install -r requirements.txt
.: Configure Your API Key:
Get your API key from Nebius Token Factory. Set it up in your environment variables or create a .streamlit/secrets.toml file:
.: NEBIUS_API_KEY = "your-nebius-api-key-here"
.: Run the Application:
.: streamlit run app.py
