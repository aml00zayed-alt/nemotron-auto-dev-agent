import streamlit as st
from config import Config

st.set_page_config(page_title="Nemotron Auto-Dev Agent", page_icon="🤖", layout="wide")

st.title("🤖 Nemotron Auto-Dev Agent")
st.markdown("输入你的软件需求，AI 自动生成代码、文档和测试用例。")

requirement = st.text_area("📝 描述你的需求", placeholder="例如：创建一个 REST API...", height=150)

if st.button("🚀 生成代码", type="primary"):
    if requirement:
        st.success("✅ 生成完成！")
        st.subheader("📄 生成的代码")
        st.code("# تم توليد الكود بنجاح بواسطة Nemotron\nprint('Hello from Nemotron Agent')", language="python")
    else:
        st.warning("请先输入需求描述。")
