from google import genai
from src.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_response(query, persona, context):

    if persona == "Technical Expert":
        style = "Provide a detailed technical explanation."

    elif persona == "Frustrated User":
        style = "Be empathetic and explain simply."

    else:
        style = "Be concise and business-focused."

    prompt = f"""
Persona: {persona}

Style: {style}

Context:
{context}

User Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text