from speech_processing import SpeechProcessing
from command_processing import CommandProcessing
from openai_agent import OpenAIAgent
from todo_manager import TodoManager

class MainApp:
    def __init__(self):
        self.speech_processor = SpeechProcessing()
        self.command_processor = CommandProcessing()
        self.openai_agent = OpenAIAgent()
        self.todo_manager = TodoManager()

    def run(self):
        while True:
            command = self.speech_processor.listen()
            if command != "":

                label = self.command_processor.handle_command(command)
                print(f"Label recognized by GPT: {label}")

                if label == "to-do list":
                    print("Do something with the todo list manager !")
                    self.speech_processor.speak("Do something with the todo list manager !")
            else:
                gpt_answer = self.openai_agent.get_response(command)
                print(f"ChatGPT Answered: {gpt_answer}")
                self.speech_processor.speak(gpt_answer)

if __name__ == "__main__":
    app = MainApp()
    app.run()
