from automation.browser_control import BrowserControl
from automation.system_control import SystemControl
import datetime

class CommandProcessor:
    def process(self, command):
        if "time" in command:
            return f"Current time is {datetime.datetime.now().strftime('%H:%M')}"

        if "open google" in command:
            BrowserControl.open_google()
            return "Opening Google"

        if "open youtube" in command:
            BrowserControl.open_youtube()
            return "Opening YouTube"

        if "open notepad" in command:
            SystemControl.open_notepad()
            return "Opening Notepad"

        return None
