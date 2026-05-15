from openai import OpenAI
import os
from dotenv import load_dotenv

SYSTEM_MESSAGE = "You are a chatbot. You will have a conversation with a user. Be friendly and concise"

if __name__ == "__main__":
    load_dotenv()
    URL = os.environ.get('OPENAI_BASE_URL')
    KEY = os.environ.get('OPENAI_API_KEY')
    MODEL = os.environ.get('MODEL')

    client = OpenAI(
        base_url=URL,
        api_key=KEY,
    )

    print(f"Chatting with {MODEL} model at {URL}\n")

    messages = [
        {'role': 'system', 'content': SYSTEM_MESSAGE}
    ]

    while True:
        user_input = input("> ")
        messages.append({'role': 'user', 'content': user_input})

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
        )

        assistant_text = response.choices[0].message.content
        messages.append({'role': 'assistant', 'content': assistant_text})

        print(assistant_text)
