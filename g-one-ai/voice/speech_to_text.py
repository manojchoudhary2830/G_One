import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
        except OSError as exc:
            print(f"Microphone unavailable: {exc}")
            return ""

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"USER: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as exc:
            print(f"Speech recognition failed: {exc}")
            return ""
