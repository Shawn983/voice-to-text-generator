import speech_recognition as sr
import pyttsx3 as tts

class SpeechProcessing:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts_engine = tts.init()

        self.tts_engine.setProperty("voice", "")
        voices = self.tts_engine.getProperty("voices")
    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = None
            try:
                audio = self.recognizer.listen(source, timeout=5)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")\
                
            text = ""

            try:
                print("Recognising")
                text = self.recognizer.recognize_google(audio)
                print(f"User said: {text}")
            except sr.UnknownValueError:
                print("Google could not recognise audio")
            except sr.RequestError:
                print("Couldn't request results from the Google Speech Recognition service")
            except Exception:
                print("There was an error")

            return text
        
    def speak(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source,duration=1)
            print("Listening...")
            audio = None
            try:
                audio = self.recognizer.listen(source, timeout=5)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")