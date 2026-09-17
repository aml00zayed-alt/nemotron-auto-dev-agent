app.py
import streamlit as st
from agent import AutoDevAgent
from config import Config

st.set_page_config(page_title="Nemotron Auto-Dev Agent", page_icon="🤖", layout="wide")

@st.cache_resource
def get_agent():
    return AutoDevAgent()

agent = get_agent()

with st.sidebar:
    st.title("⚙️ 配置")
    target_stack = st.selectbox("目标技术栈", ["Python (Flask)", "Python (FastAPI)", "Python (纯脚本)", "JavaScript (Node.js)"])
    gen_mode = st.radio("生成模式", ["代码 + 文档", "仅代码", "仅文档"])
    st.divider()
    st.caption("由 NVIDIA Nemotron 驱动 | Nebius Token Factory")

st.title("🤖 Nemotron Auto-Dev Agent")
st.markdown("输入你的软件需求，AI 自动生成代码、文档和测试用例。")

with st.form("requirement_form"):
    requirement = st.text_area("📝 描述你的需求", placeholder="例如：创建一个 REST API...", height=150)
    submitted = st.form_submit_button("🚀 生成代码", type="primary")

if submitted and requirement:
    with st.spinner("Nemotron 正在思考和生成..."):
        try:
            result = agent.generate(requirement=requirement, target_stack=target_stack, mode=gen_mode)
            st.success("✅ 生成完成！")
            col1, col2 = st.columns([2, 1])
            with col1:
                st.subheader("📄 生成的代码")
                st.code(result["code"], language="python" if "Python" in target_stack else "javascript")
            with col2:
                st.subheader("📋 项目说明")
                st.markdown(result["docs"])
            st.download_button(label="⬇️ 下载代码文件", data=result["code"], file_name=f"generated.py", mime="text/plain")
        except Exception as e:
            st.error(f"生成失败：{str(e)}")
elif submitted:
    st.warning("请先输入需求描述。")
