# Gemini-Techguide-Ai-chatbot
# ⚡ TechGuide Pro AI

**Production-Ready Cloud & Software Engineering Assistant**

TechGuide Pro is a domain-specific, production-grade GenAI chatbot designed to assist users with high-level technical knowledge. It leverages Google's Gemini API (1.5 Flash) and is built with a modular, stateless architecture suitable for real-world deployment on cloud platforms like Streamlit AWS EC2.

---

## 🚀 Project Overview

TechGuide Pro simulates a real-world Generative AI production system. It includes:
* ✅ **Proper Gemini API integration** using the official SDK.
* ✅ **Multi-turn conversation memory** bound to Streamlit's session state.
* ✅ **Advanced prompt engineering** via system instructions for strict persona adherence.
* ✅ **Interactive & modern UI** featuring centered inputs, custom CSS gradients, and avatars.
* ✅ **Secure API key handling** using environment variables.
* ✅ **Clean modular code structure** separating frontend UI from backend LLM logic.
* ✅ **Deployment-ready architecture** configured for cloud hosting.

This chatbot is restricted strictly to Software Engineering, Cloud Computing, System Design, and Coding topics.

---

## 🏗 System Architecture

```text
User (Web Browser)
       ↓
Streamlit UI (app.py)
       ↓
Application Layer (Python Backend)
       ↓
Conversation Memory Manager (st.session_state)
       ↓
Prompt Engineering Layer (bot_engine.py)
       ↓
Google Gemini 1.5 Flash Model
       ↓
Response Output


## 🧠 Features
🔹 Domain-Specific Intelligence
TechGuide AI is fine-tuned to only answer questions related to:

Software Engineering Principles

Cloud Computing (AWS, GCP, Azure)

Programming & Scripting (Python, JavaScript, etc.)

System Design & Architecture

DevOps & CI/CD Pipelines

🔹 Advanced UI/UX & Multi-Turn Memory
Maintains session-based chat history for highly contextual, multi-turn responses.

Features a "Clear Chat" function to reset memory without refreshing the page.

Inline, centered chat input for a search-engine-style user experience.

🔹 Secure API Integration
Uses .env files for environment-based API key management, ensuring credentials are never exposed in the source code.

🔹 Production-Level Directory Structure
Plaintext
techguide-pro-ai/
│
├── app.py                  # Streamlit frontend & UI logic
├── bot_engine.py           # Gemini API client & prompt engineering
├── .env                    # Secret environment variables
├── requirements.txt        # Dependency tracking
└── README.md               # Project documentation
⚙️ Tech Stack
Language: Python 3.10+

Frontend: Streamlit

AI/LLM: Google Generative AI SDK (Gemini 1.5 Flash)

Configuration: python-dotenv

🔐 Environment Setup
1️⃣ Clone Repository
Bash
git clone <your-repo-url>
cd techguide-pro-ai
2️⃣ Create Virtual Environment
Bash
python -m venv venv
Activate:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3️⃣ Install Dependencies
Bash
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file in the root directory and add your API key:

Code snippet
GEMINI_API_KEY=your_google_gemini_api_key_here
▶️ Run Application locally
Bash
streamlit run app.py
The application will be available at: http://localhost:8501

🧪 Example Queries
"Explain the difference between a Monolithic architecture and Microservices."

"What is the best way to deploy a scalable web app on AWS?"

"Write a Python function to reverse a string and explain the time complexity."

"How do I optimize a slow SQL query?"

## ⚠️ Limitations
Domain Restricted: Does NOT provide advice on non-technical subjects (e.g., cooking, sports, medical advice).

Execution: Generates code but does not execute it directly within the chat environment.

☁️ Deployment (AWS EC2 Ready)
TechGuide Pro is fully deployable on cloud infrastructure including AWS EC2, Render, or Railway.

To run securely on a cloud server:

Bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
(Ensure port 8501 is open in your cloud provider's firewall/security groups).

🛡 Security Considerations
API keys are strictly stored in .env.

.gitignore is configured to prevent accidental credential leaks.

Domain-restricted prompt enforcement mitigates prompt-injection attacks for off-topic queries.

## 📌 Future Improvements
[ ] Database-backed persistent memory (PostgreSQL / MongoDB)

[ ] User Authentication & Login

[ ] Docker containerization (Dockerfile and docker-compose)

[ ] Export chat history to PDF/Markdown


👨‍💻 Author
[Rohit Ganeshe] Software Engineer | Cloud & AI Enthusiast [] 

📄 License
This project is developed for educational and demonstration purposes.

⚙️ Tech Stack
Language: Python 3.10+

Frontend: Streamlit

AI/LLM: Google Generative AI SDK (Gemini 1.5 Flash)

Configuration: python-dotenv

🔐 Environment Setup
1️⃣ Clone Repository
Bash
git clone <your-repo-url>
cd techguide-pro-ai
2️⃣ Create Virtual Environment
Bash
python -m venv venv
Activate:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3️⃣ Install Dependencies
Bash
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file in the root directory and add your API key:

Code snippet
GEMINI_API_KEY=your_google_gemini_api_key_here
▶️ Run Application locally
Bash
streamlit run app.py
The application will be available at: http://localhost:8501

🧪 Example Queries
"Explain the difference between a Monolithic architecture and Microservices."

"What is the best way to deploy a scalable web app on AWS?"

"Write a Python function to reverse a string and explain the time complexity."

"How do I optimize a slow SQL query?"

⚠️ Limitations
Domain Restricted: Does NOT provide advice on non-technical subjects (e.g., cooking, sports, medical advice).

Execution: Generates code but does not execute it directly within the chat environment.

☁️ Deployment (AWS EC2 Ready)
TechGuide Pro is fully deployable on cloud infrastructure including AWS EC2, Render, or Railway.

To run securely on a cloud server:

Bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
(Ensure port 8501 is open in your cloud provider's firewall/security groups).

🛡 Security Considerations
API keys are strictly stored in .env.

.gitignore is configured to prevent accidental credential leaks.

Domain-restricted prompt enforcement mitigates prompt-injection attacks for off-topic queries.

📌 Future Improvements
[ ] Database-backed persistent memory (PostgreSQL / MongoDB)

[ ] User Authentication & Login

[ ] Docker containerization (Dockerfile and docker-compose)

[ ] Export chat history to PDF/Markdown

👨‍💻 Author
[Your Name] Software Engineer | Cloud & AI Enthusiast [LinkedIn Profile Link] | [GitHub Profile Link]

📄 License
This project is developed for educational and demonstration purposes.
