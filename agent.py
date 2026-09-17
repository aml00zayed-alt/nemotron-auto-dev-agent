import os
from openai import OpenAI
from prompts import SYSTEM_PROMPT, build_user_prompt
from config import Config

class AutoDevAgent:
    def __init__(self):
        api_key = self._get_api_key()
        if not api_key:
            raise ValueError("未找到 NEBIUS_API_KEY。")
        self.client = OpenAI(base_url=Config.BASE_URL, api_key=api_key)
        self.model = Config.MODEL_ID
    
    def _get_api_key(self):
        key = os.environ.get("NEBIUS_API_KEY")
        if key: return key
        try:
            import streamlit as st
            return st.secrets["NEBIUS_API_KEY"]
        except: return None
    
    def generate(self, requirement: str, target_stack: str, mode: str) -> dict:
        user_prompt = build_user_prompt(requirement, target_stack, mode)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_prompt}],
            temperature=0.3, max_tokens=4096
        )
        return self._parse_output(response.choices[0].message.content)
    
    def _parse_output(self, raw: str) -> dict:
        code, docs = "", ""
        if "```" in raw:
            parts = raw.split("```")
            for i, part in enumerate(parts):
                if i % 2 == 1:
                    code = part.strip()
                    break
            docs = "```".join(parts[::2]).strip()
        else:
            code = raw.strip()
        return {"code": code, "docs": docs or "生成的文档将显示在这里。"}
