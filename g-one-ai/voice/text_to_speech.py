import pyttsx3
from core.config import VOICE_RATE


class TextToSpeech:
    def __init__(self):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", VOICE_RATE)
        except Exception as exc:
            self.engine = None
            print(f"Text-to-speech unavailable: {exc}")

    def speak(self, text):
        print(f"G-ONE: {text}")
        if not self.engine:
            return

        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as exc:
            print(f"Text-to-speech failed: {exc}")
