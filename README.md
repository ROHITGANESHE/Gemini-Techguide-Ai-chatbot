<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechGuide Pro AI - Documentation</title>
    <style>
        :root {
            --primary-color: #4A00E0;
            --secondary-color: #8E2DE2;
            --text-color: #333;
            --bg-color: #f9f9f9;
            --code-bg: #1e1e1e;
            --code-text: #d4d4d4;
            --card-bg: #ffffff;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            background: var(--card-bg);
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            border-radius: 12px;
        }

        /* Header Styling */
        header {
            text-align: center;
            border-bottom: 2px solid #eee;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }

        h1 {
            font-size: 3rem;
            margin-bottom: 0.2rem;
            background: -webkit-linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .tagline {
            font-size: 1.2rem;
            color: #666;
            font-weight: 600;
        }

        h2 {
            color: var(--primary-color);
            border-left: 5px solid var(--secondary-color);
            padding-left: 10px;
            margin-top: 40px;
        }

        h3 {
            color: #444;
            margin-top: 25px;
        }

        /* Lists */
        ul {
            list-style-type: none;
            padding-left: 0;
        }

        li {
            margin-bottom: 10px;
            padding-left: 20px;
            position: relative;
        }

        li::before {
            content: "•";
            color: var(--primary-color);
            font-weight: bold;
            position: absolute;
            left: 0;
        }

        /* Code Blocks */
        pre {
            background-color: var(--code-bg);
            color: var(--code-text);
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9rem;
        }

        code {
            background-color: #eee;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: 'Consolas', 'Monaco', monospace;
            color: #d63384;
        }

        pre code {
            background-color: transparent;
            color: var(--code-text);
            padding: 0;
        }

        /* Architecture Diagram Simulation */
        .architecture-box {
            background: #f4f4f4;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            font-family: monospace;
            white-space: pre-wrap;
            border: 1px dashed #aaa;
        }

        /* Tables/Grids for Tech Stack */
        .tech-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        
        .tech-card {
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
        }

        .tech-card strong {
            display: block;
            color: var(--primary-color);
            margin-bottom: 5px;
        }

        /* Footer */
        footer {
            margin-top: 50px;
            text-align: center;
            font-size: 0.9rem;
            color: #777;
            border-top: 1px solid #eee;
            padding-top: 20px;
        }

        .btn {
            display: inline-block;
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            margin-top: 10px;
        }
        
        /* Directory Structure */
        .directory {
            font-family: monospace;
            color: #333;
            background: #fffbe6;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #ffd700;
        }

    </style>
</head>
<body>

<div class="container">

    <header>
        <h1>⚡ TechGuide Pro AI</h1>
        <div class="tagline">Production-Ready Cloud & Software Engineering Assistant</div>
        <p style="margin-top:15px; max-width: 600px; margin-left: auto; margin-right: auto;">
            A domain-specific, production-grade GenAI chatbot leveraging Google's Gemini API (1.5 Flash). Built with modular architecture for real-world deployment on AWS EC2.
        </p>
    </header>

    <section>
        <h2>🚀 Project Overview</h2>
        <p>TechGuide Pro simulates a real-world Generative AI production system. It includes:</p>
        <ul>
            <li>✅ <strong>Proper Gemini API integration</strong> using the official SDK.</li>
            <li>✅ <strong>Multi-turn conversation memory</strong> bound to Streamlit's session state.</li>
            <li>✅ <strong>Advanced prompt engineering</strong> via system instructions for strict persona adherence.</li>
            <li>✅ <strong>Interactive & modern UI</strong> featuring centered inputs, custom CSS gradients, and avatars.</li>
            <li>✅ <strong>Secure API key handling</strong> using environment variables.</li>
            <li>✅ <strong>Clean modular code structure</strong> separating frontend UI from backend LLM logic.</li>
            <li>✅ <strong>Deployment-ready architecture</strong> configured for cloud hosting.</li>
        </ul>
        <p><em>This chatbot is restricted strictly to Software Engineering, Cloud Computing, System Design, and Coding topics.</em></p>
    </section>

    <section>
        <h2>🏗 System Architecture</h2>
        <div class="architecture-box">
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
        </div>
    </section>

    <section>
        <h2>🧠 Features</h2>
        
        <h3>🔹 Domain-Specific Intelligence</h3>
        <p>TechGuide AI is fine-tuned to only answer questions related to:</p>
        <ul>
            <li>Software Engineering Principles</li>
            <li>Cloud Computing (AWS, GCP, Azure)</li>
            <li>Programming & Scripting (Python, JavaScript, etc.)</li>
            <li>System Design & Architecture</li>
            <li>DevOps & CI/CD Pipelines</li>
        </ul>

        <h3>🔹 Advanced UI/UX & Memory</h3>
        <ul>
            <li>Maintains session-based chat history for highly contextual, multi-turn responses.</li>
            <li>Features a "Clear Chat" function to reset memory without refreshing.</li>
            <li>Inline, centered chat input for a search-engine-style experience.</li>
        </ul>

        <h3>🔹 Production-Level Directory Structure</h3>
        <div class="directory">
<pre>
techguide-pro-ai/
│
├── app.py                  # Streamlit frontend & UI logic
├── bot_engine.py           # Gemini API client logic
├── .env                    # Secret environment variables
├── requirements.txt        # Dependency tracking
└── README.md               # Project documentation
</pre>
        </div>
    </section>

    <section>
        <h2>⚙️ Tech Stack</h2>
        <div class="tech-grid">
            <div class="tech-card">
                <strong>Language</strong>
                Python 3.10+
            </div>
            <div class="tech-card">
                <strong>Frontend</strong>
                Streamlit
            </div>
            <div class="tech-card">
                <strong>AI Model</strong>
                Google Gemini 1.5 Flash
            </div>
            <div class="tech-card">
                <strong>Config</strong>
                python-dotenv
            </div>
        </div>
    </section>

    <section>
        <h2>🔐 Environment Setup</h2>
        
        <h3>1️⃣ Clone Repository</h3>
        <pre><code>git clone &lt;your-repo-url&gt;
cd techguide-pro-ai</code></pre>

        <h3>2️⃣ Create Virtual Environment</h3>
        <pre><code>python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate</code></pre>

        <h3>3️⃣ Install Dependencies</h3>
        <pre><code>pip install -r requirements.txt</code></pre>

        <h3>4️⃣ Configure Environment Variables</h3>
        <p>Create a <code>.env</code> file in the root directory:</p>
        <pre><code>GEMINI_API_KEY=your_google_gemini_api_key_here</code></pre>

        <h3>▶️ Run Application</h3>
        <pre><code>streamlit run app.py</code></pre>
        <p>The application will be available at: <a href="http://localhost:8501">http://localhost:8501</a></p>
    </section>

    <section>
        <h2>🧪 Example Queries</h2>
        <ul>
            <li>"Explain the difference between a Monolithic architecture and Microservices."</li>
            <li>"What is the best way to deploy a scalable web app on AWS?"</li>
            <li>"Write a Python function to reverse a string and explain the time complexity."</li>
            <li>"How do I optimize a slow SQL query?"</li>
        </ul>
    </section>

    <section>
        <h2>⚠️ Limitations</h2>
        <ul>
            <li><strong>Domain Restricted:</strong> Does NOT provide advice on non-technical subjects (e.g., cooking, sports).</li>
            <li><strong>Execution:</strong> Generates code but does not execute it directly within the chat environment.</li>
        </ul>
    </section>

    <section>
        <h2>☁️ Deployment (AWS EC2 Ready)</h2>
        <p>TechGuide Pro is fully deployable on cloud infrastructure (AWS EC2, Render, Railway).</p>
        <p>To run securely on a cloud server:</p>
        <pre><code>streamlit run app.py --server.port 8501 --server.address 0.0.0.0</code></pre>
        <p><em>(Ensure port 8501 is open in your cloud provider's firewall/security groups).</em></p>
    </section>

    <section>
        <h2>📌 Future Improvements</h2>
        <ul>
            <li>[ ] Database-backed persistent memory (PostgreSQL / MongoDB)</li>
            <li>[ ] User Authentication & Login</li>
            <li>[ ] Docker containerization (Dockerfile)</li>
            <li>[ ] Export chat history to PDF/Markdown</li>
        </ul>
    </section>

    <footer>
        <p><strong>👨‍💻 Author: Rohit Ganeshe</strong></p>
        <p>Software Engineer | Cloud & AI Enthusiast</p>
        <p>📄 License: Developed for educational and demonstration purposes.</p>
    </footer>

</div>

</body>
</html>
