SYSTEM_PROMPT = "你是一个专业的软件开发助手，专门根据用户需求生成高质量的代码和文档。"
def build_user_prompt(requirement: str, target_stack: str, mode: str) -> str:
    return f"需求：{requirement}\n技术栈：{target_stack}\n模式：{mode}"
