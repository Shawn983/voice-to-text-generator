import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIAgent:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def get_response(self, command):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a vocal assistant. You have to answer in a simple, efficient and concise way. Your answer should not take more than 30 seconds to say out loud."},
                {"role": "user", "content": command}
            ]
        )

        assistant_reply = response["choices"][0]["message"]["content"]

        return assistant_reply
        
    def get_command_label(self, command):
        response = openai.ChatCompletion.create(
            model = self.model,
            messages=[
                {"role": "system", "content": "You are vocal assistant."},
                {"role": "system", "content": "Your role is to classify the user's command and return only the corresponding label."},
                {"role": "system", "content": "The labels are: to-do list,normal question."},
                {"role": "system", "content": "If you recognise the users command as a todo list request (for example), then return 'to-do list'."},
                {"role": "user", "content": command}
            ]
        )

        label = response["choices"][0]["messages"]["content"]
        return label