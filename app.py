import streamlit as st
from bot_engine import initialize_gemini_chat

# 1. Page Configuration (Changed to 'wide' layout for a better chat experience)
st.set_page_config(page_title="TechGuide ", page_icon="⚡", layout="wide")

# 2. Custom CSS for UI Enhancement and Colors
st.markdown("""
<style>
    /* Gradient text for the main title */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #4A00E0, #8E2DE2); /* Cool purple gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }
    /* Subtitle styling */
    .subtitle { 
        text-align: center;
        color: #888888;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Display Custom Headers
st.markdown('<h1 class="main-title">⚡ TechGuide: AI Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask me anything about Software Engineering, AWS, Coding, or System Design.</p>', unsafe_allow_html=True)
st.divider()

# 3. Sidebar for Controls (Keeps the main UI clean)
with st.sidebar:
    st.header("⚙️ Controls")
    
    # Clear Chat Functionality
    # Using type="primary" makes the button stand out with your Streamlit theme's primary color
    if st.button("🗑️ Clear Chat History", type="primary", use_container_width=True):
        # Reset the session state memory by re-initializing the chat
        st.session_state.chat_session = initialize_gemini_chat()
        # st.rerun() forces the UI to reload from top to bottom, clearing the screen
        st.rerun() 

    st.divider()
    st.markdown("### 💡 About")
    st.info("TechGuide is a production-grade AI assistant. It remembers context and is fine-tuned for high-level technical queries.")

# 4. Main Chat Interface
# Initialize chat session in Streamlit state to maintain memory across re-runs
if "chat_session" not in st.session_state:
    st.session_state.chat_session = initialize_gemini_chat()

# Display chat history from the Gemini session object
for message in st.session_state.chat_session.history:
    # Ensure roles map correctly to Streamlit's UI
    role = "user" if message.role == "user" else "assistant"
    
    # Added custom emojis/avatars for better visual separation
    avatar = "🧑‍💻" if role == "user" else "🤖"
    
    with st.chat_message(role, avatar=avatar):
        st.markdown(message.parts[0].text)

# 5. User Input Box
# Added a rocket emoji to the input placeholder
if user_prompt := st.chat_input("Ask a technical question... 🚀"):
    
    # Display user message in UI
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_prompt)

    # Get response from Gemini
    with st.chat_message("assistant", avatar="🤖"):
        # Custom loading message
        with st.spinner("Analyzing and thinking... 💭"):
            try:
                # send_message automatically appends to the history
                response = st.session_state.chat_session.send_message(user_prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")