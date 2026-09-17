"""
Prompt Templates
Define System Prompt and User Prompt building logic.
"""

SYSTEM_PROMPT = """You are a professional software development assistant specialized in generating high-quality code and documentation based on user requirements.

## Your Capabilities
- Fluent in Python, JavaScript, and Web Development
- Able to translate abstract requirements into executable technical plans
- Generate production-grade code with error handling and comments
- Output clear markdown documentation

## Output Format Requirements
You must strictly follow this format:
1. First, output the code wrapped in ``` (specifying the language).
2. Second, output the documentation in Markdown format.
"""

def build_user_prompt(requirement: str, target_stack: str, mode: str) -> str:
    mode_instruction = {
        "Code + Documentation": "Please generate complete code and documentation.",
        "Code Only": "Generate code only, no documentation required.",
        "Documentation Only": "Generate documentation only, describing implementation and architecture, no code required."
    }
    
    return f"""## Requirement Description
{requirement}

## Target Tech Stack
{target_stack}

## Generation Mode
{mode_instruction.get(mode, "Please generate code and documentation.")}

Please start generating:"""
