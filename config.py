import os
import json
import getpass
import requests
from PyQt5.QtWidgets import QInputDialog
from updater import Updater

def get_api_key():
    """Retrieve API key from config file or ask the user to input it."""
    config_path = os.path.expanduser("~/.gita_config.json")
    username = getpass.getuser()

    first_time = not os.path.exists(config_path)  
    api_key = None

    if not first_time:
        try:
            with open(config_path, "r") as f:
                data = json.load(f)
                api_key = data.get("api_key", None)
        except:
            pass

    # If not found, ask the user
    if not api_key:
        api_key, ok = QInputDialog.getText(
            None,
            "Enter API Key",
            "Please enter your Google Gemini API Key:"
        )
        if ok and api_key.strip():
            with open(config_path, "w") as f:
                json.dump({"api_key": api_key.strip()}, f)
            api_key = api_key.strip()

   
