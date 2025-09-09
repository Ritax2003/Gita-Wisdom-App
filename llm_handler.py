import google.generativeai as genai
from typing import Dict

class GitaLLMHandler:
    def __init__(self, api_key=None):
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-2.5-flash-lite")
        else:
            self.model = None

    def generate_response(self, query: str, context: Dict) -> Dict:
        if not self.model:
            return {'response': "API not configured.", 'error': True}

        verses_text = context.get('formatted_context', '')
        themes = context.get('query_themes', [])

        prompt = f""" You are Krishna's wise guide. 
        User's Question: "{query}" 
        Relevant Verses: {verses_text} 
        Themes: {themes} """

        try:
            response = self.model.generate_content(prompt)
            return {'response': response.text, 'error': False}
        except Exception as e:
            return {'response': str(e), 'error': True}
