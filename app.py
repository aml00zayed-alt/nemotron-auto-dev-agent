"""
Nemotron Auto-Dev Agent - Streamlit Frontend
Users input software requirements, and the AI automatically generates code and documentation.
"""

import streamlit as st
from agent import AutoDevAgent
from config import Config

# ========== Page Configuration ==========
st.set_page_config(
    page_title="Nemotron Auto-Dev Agent",
    page_icon="🤖",
    layout="wide"
)

# ========== Initialize Agent ==========
@st.cache_resource
def get_agent():
    """Cache the Agent instance to avoid redundant initialization"""
    return AutoDevAgent()

agent = get_agent()

# ========== Sidebar ==========
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # Target Tech Stack
    target_stack = st.selectbox(
        "Target Tech Stack",
        ["Python (Flask)", "Python (FastAPI)", "Python (Pure Script)", "JavaScript (Node.js)"]
    )
    
    # Generation Mode
    gen_mode = st.radio(
        "Generation Mode",
        ["Code + Documentation", "Code Only", "Documentation Only"]
    )
    
    st.divider()
    st.caption("Powered by NVIDIA Nemotron | Nebius Token Factory")

# ========== Main Interface ==========
st.title("🤖 Nemotron Auto-Dev Agent")
st.markdown("Enter your software requirements, and let AI automatically generate code, documentation, and architecture plans.")

# Requirement Input Area
with st.form("requirement_form"):
    requirement = st.text_area(
        "📝 Describe Your Requirement",
        placeholder="e.g., Create a REST API supporting user registration, login, and profile retrieval using JWT authentication...",
        height=150
    )
    
    submitted = st.form_submit_button("🚀 Generate Code", type="primary")

# ========== Handle Request ==========
if submitted and requirement:
    with st.spinner("Nemotron is thinking and generating..."):
        try:
            result = agent.generate(
                requirement=requirement,
                target_stack=target_stack,
                mode=gen_mode
            )
            
            # Show Results
            st.success("✅ Generation Complete!")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("📄 Generated Code")
                st.code(result["code"], language="python" if "Python" in target_stack else "javascript")
            
            with col2:
                st.subheader("📋 Project Documentation")
                st.markdown(result["docs"])
            
            # Download Button
            st.download_button(
                label="⬇️ Download Code File",
                data=result["code"],
                file_name=f"generated_{target_stack.split()[0].lower()}.py",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"Generation Failed: {str(e)}")
            st.info("Please check if your API Key is correctly configured.")

elif submitted:
    st.warning("Please enter your requirement description first.")

# ========== Footer ==========
st.divider()
st.caption("Nemotron Auto-Dev Agent | Nebius Token Factory Hackathon")
