
import sys
from modules.menu import Menu

settings = {
    'API_KEY': '1234',
}

# If settings.text exists, load settings from file
# CAUTION: This is not a secure way to store API keys
#! SHOULD USE THIS FORMAT, NO SPACES AROUND THE EQUAL SIGN: 
#! API_KEY=__YOUR_API_KEY__

try:
    with open("settings.txt", "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            settings[key] = value
except:
    pass

def save_settings():
    with open("settings.txt", "w") as f:
        for key, value in settings.items():
            f.write(f"{key}={value}\n")

 
# Set API KEY if passed as argument
if len(sys.argv) > 1:
    settings["API_KEY"] = sys.argv[1]

# Show main options menu
options = ["API Settings", "Manage DNS Records", "Save Settings"]

while True:
    
    choice = Menu(settings).show_mainmenu(options)
    sys.exit(0) if choice == "0" else None

    Menu(settings).edit_settings(settings) if choice == "1" else None
    try:
        save_settings() if choice == "3" else None
    except:
        print("    Error while saving settings")
        continue