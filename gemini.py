import os
from dotenv import load_dotenv
from google import genai

class Gemini:
    def __init__(self):
        load_dotenv()
        self.client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

    def generate_text(self,prompt):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    
