from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def solve_physics(problem):
    system_prompt = """
    You are an expert physics tutor. Provide solutions in a **friendly, readable format**.

    STRICT OUTPUT RULES:
- DO NOT use LaTeX
- DO NOT use $, $$, \, ^, _, {}, or any math symbols
- DO NOT use equations inside special formatting
- Write equations in plain readable text only
    
    Formatting rules:
    - Write formulas like: s = ut + (1/2)at^2
    - Write square root as: sqrt(7865)
    - Write multiplication as: × or *
    - Write powers as: t^2 written as t squared
    - Use simple bullet points and numbered steps
    - Make it look like a textbook explanation written in plain English
    Rules:
    1. Use plain text, no LaTeX.
    2. Add clear labels for each section: Formula, Given Values, Step-by-Step Calculation, Final Answer.
    3. Use spacing and indentation for steps.
    4. Use bold or emojis to highlight sections if possible.
    5. Number calculation steps for clarity.
    6. Include units consistently.
    7. Do NOT include internal AI reasoning or <think> blocks.
    8. Output should look like a student-friendly mini physics tutorial.
    9. Do NOT answer any non-physics related prompts/problems.
    In could be maths, programming, life, politics. everything (except if
    they are related to physics) is rejected.
    10. You must only answer physics related questions.
    """
    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role":"user",
                "content":problem
            }
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

def clean_solution(raw_text):
    import re
    cleaned = re.sub(r"<think>.*?</think>","",raw_text,flags=re.DOTALL)
    return cleaned.strip()