from voice.text_to_speech import TextToSpeech
from voice.speech_to_text import SpeechToText
from core.memory import MemoryManager
from core.commands import CommandProcessor
from ai.openai_engine import AIEngine

class GOneAssistant:
    def __init__(self):
        self.tts = TextToSpeech()
        self.stt = SpeechToText()
        self.memory = MemoryManager()
        self.commands = CommandProcessor()
        self.ai = AIEngine()

    def start(self):
        self.tts.speak("G-ONE systems initialized.")

        while True:
            command = self.stt.listen()

            if not command:
                continue

            if "shutdown" in command:
                self.tts.speak("Shutting down G-ONE.")
                break

            local_response = self.commands.process(command)

            if local_response:
                self.tts.speak(local_response)
                continue

            self.memory.save_user_message(command)

            response = self.ai.ask(
                command,
                history=self.memory.get_history()
            )

            self.memory.save_ai_message(response)
            self.tts.speak(response)
