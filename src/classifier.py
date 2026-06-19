from google import genai
from src.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def classify_customer_persona(message):
    prompt = f"""
Classify the user into ONE of these personas:

1. Technical Expert
2. Frustrated User
3. Business Executive

Return ONLY the persona name.

Message:
{message}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()