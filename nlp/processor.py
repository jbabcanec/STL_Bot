import openai
import os

class ChatHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def ask_chatgpt(self, question, context=""):
        messages = [
            {"role": "system", "content": (
                "You are a helpful assistant. Generate only OpenSCAD code based on the given prompt. Just give me the code only with no other comments. Your output will be put directly into OpenSCAD"
            )},
            {"role": "system", "content": context},
            {"role": "user", "content": question}
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-2024-05-13",
                messages=messages,
                max_tokens=4096,
                temperature=0.3,
                top_p=1.0,
                n=1
            )
            response_text = response.choices[0].message['content'].strip()
            scad_code = self.extract_code(response_text)
            token_count = response.usage['total_tokens']
            return scad_code, token_count
        except Exception as e:
            return f"Failed to call ChatGPT API: {str(e)}", 0

    def extract_code(self, text):
        # Extract code block from the response
        start = text.find('```openscad')
        end = text.find('```', start + 1)
        if start != -1 and end != -1:
            return text[start + len('```openscad'):end].strip()
        return text.strip()

def process_prompt(prompt):
    # Read the API key from credentials.txt in the parent directory
    credentials_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'credentials.txt')
    with open(credentials_file, 'r') as file:
        api_key = file.read().strip()
    
    chat_handler = ChatHandler(api_key)
    scad_code, token_count = chat_handler.ask_chatgpt(prompt)
    return scad_code, token_count
