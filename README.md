<h1 align="center">⚡ TechGuide AI Chatbot </h1>

<p align="center">
TechGuide AI is a domain-focused, production-grade Generative AI assistant built to answer high-level technical questions in <b>Software Engineering, Cloud Computing, AWS, and System Design</b>.
</p>

<p align="center">
It leverages Google Gemini Flash models, implements multi-turn memory, and follows a clean modular architecture suitable for real-world deployment.
</p>

<hr>

<h2>🚀 Project Overview</h2>

<p>TechGuide AI simulates a real-world production GenAI system with:</p>

<ul>
<li>✅ Secure Gemini API Integration</li>
<li>✅ Multi-turn Conversation Memory</li>
<li>✅ Advanced Prompt Engineering</li>
<li>✅ Streamlit Interactive UI</li>
<li>✅ Secure API Key Handling (.env)</li>
<li>✅ Clean Modular Code Structure</li>
<li>✅ Deployment-Ready Architecture</li>
</ul>

<p><b>This chatbot is strictly restricted to technical topics such as:</b></p>

<ul>
<li>Cloud Computing</li>
<li>AWS Architecture</li>
<li>Backend Engineering</li>
<li>System Design</li>
<li>Data Structures & Algorithms</li>
<li>DevOps & CI/CD</li>
<li>Software Engineering Concepts</li>
</ul>

<hr>

<h2>🏗 System Architecture</h2>

<pre align="center">
User (Browser)
        ↓
Streamlit UI (Frontend)
        ↓
Application Layer (app.py)
        ↓
Bot Engine (Gemini Client + Prompt Layer)
        ↓
Gemini Flash Model
        ↓
Response Output
</pre>

<hr>

<h2>🧠 Core Features</h2>

<h3>🔹 Domain-Specific Intelligence</h3>
<p>
TechGuide strictly answers technical and engineering-related queries and politely declines non-technical topics.
This behavior is enforced through system-level prompt engineering inside <b>bot_engine.py</b>.
</p>

<h3>🔹 Multi-Turn Memory</h3>
<p>
Conversation history is maintained via Gemini’s <code>start_chat()</code> session,
enabling contextual and stateful responses.
</p>

<h3>🔹 Interactive Streamlit UI</h3>

<ul>
<li>Wide layout configuration</li>
<li>Gradient styled header</li>
<li>Sidebar controls</li>
<li>Clear Chat History button</li>
<li>Custom avatars (🧑‍💻 / 🤖)</li>
<li>Real-time spinner feedback</li>
</ul>

<p>Implemented in <b>app.py</b></p>

<h3>🔹 Advanced Prompt Engineering</h3>

<ul>
<li>Concise, technical responses</li>
<li>Structured formatting (bullet points, numbered lists)</li>
<li>Code explanations with comments</li>
<li>Domain restriction enforcement</li>
</ul>

<p>Prompt logic located in <b>bot_engine.py</b></p>

<h3>🔹 Secure API Integration</h3>

<ul>
<li>API keys stored in <code>.env</code></li>
<li>No hardcoded credentials</li>
<li><code>.gitignore</code> protection</li>
<li>Environment loading via <b>python-dotenv</b></li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
techguide-ai/
│
├── app.py                 # Streamlit UI
├── bot_engine.py          # Gemini configuration & system prompt
├── .env                   # API Key (Not committed)
├── requirements.txt
└── README.md
</pre>

<hr>

<h2>⚙️ Tech Stack</h2>

<ul>
<li>Python 3.12</li>
<li>Streamlit</li>
<li>Google Generative AI SDK</li>
<li>Gemini Flash Model (gemini-3-flash-preview)</li>
<li>python-dotenv</li>
</ul>

<hr>

<h2>🔐 Environment Setup</h2>

<h3>1️⃣ Clone Repository</h3>

<pre>
git clone &lt;your-repo-url&gt;
cd techguide-ai
</pre>

<h3>2️⃣ Create Virtual Environment</h3>

<pre>
python -m venv myenv
</pre>

<p><b>Activate:</b></p>

<p>Windows:</p>
<pre>myenv\Scripts\activate</pre>

<p>Mac/Linux:</p>
<pre>source myenv/bin/activate</pre>

<h3>3️⃣ Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<p>If no requirements file:</p>

<pre>
pip install streamlit google-generativeai python-dotenv
</pre>

<h3>4️⃣ Configure Environment Variables</h3>

<pre>
GEMINI_API_KEY=your_api_key_here
</pre>

<hr>

<h2>▶️ Run the Application</h2>

<pre>
streamlit run app.py
</pre>

<p>Runs locally at:</p>

<pre>http://localhost:8501</pre>

<hr>

<h2>🧪 Example Queries</h2>

<ul>
<li>Explain CAP theorem in distributed systems.</li>
<li>How does AWS Auto Scaling work?</li>
<li>Design a scalable URL shortener.</li>
<li>What is Infrastructure as Code?</li>
<li>Explain CI/CD pipeline architecture.</li>
</ul>

<hr>

<h2>⚠️ Limitations</h2>

<ul>
<li>❌ Does NOT answer non-technical topics.</li>
<li>❌ No medical, legal, or financial advice.</li>
<li>❌ No persistent database-backed memory (session-only).</li>
</ul>

<hr>

<h2>☁️ Deployment (Cloud Ready)</h2>

<p>TechGuide AI can be deployed on:</p>

<ul>
<li>AWS EC2</li>
<li>Render</li>
<li>Railway</li>
<li>Azure VM</li>
<li>GCP VM</li>
</ul>

<pre>
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
</pre>

<hr>

<h2>🛡 Security Considerations</h2>

<ul>
<li>API keys stored securely in <code>.env</code></li>
<li>.gitignore configured</li>
<li>No hardcoded secrets</li>
<li>Domain-restricted system prompt</li>
<li>Controlled temperature for factual responses</li>
</ul>

<hr>

<h2>📌 Future Improvements</h2>

<ul>
<li>Persistent database memory (Redis / PostgreSQL)</li>
<li>Authentication & user accounts</li>
<li>Role-based access</li>
<li>Logging & monitoring</li>
<li>CI/CD pipeline</li>
<li>Docker containerization</li>
<li>Kubernetes deployment</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
<b>Rohit Ganeshe</b><br>
AI & ML Engineer | Cloud & Software Engineering Enthusiast<br>
🔗 https://www.linkedin.com/in/rohit-ganeshe-rsg030/
</p>

<hr>

<h2>📄 License</h2>

<p>
This project is developed for educational and demonstration purposes.
</p>
