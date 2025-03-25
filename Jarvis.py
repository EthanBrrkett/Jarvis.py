import random
import webbrowser
import os

def print_logo():
    logo = r""" 
    

       __       ___      .______     ____    ____  __       _______.
      |  |     /   \     |   _  \    \   \  /   / |  |     /       |
      |  |    /  ^  \    |  |_)  |    \   \/   /  |  |    |   (----`
.--.  |  |   /  /_\  \   |      /      \      /   |  |     \   \    
|  `--'  |  /  _____  \  |  |\  \----.  \    /    |  | .----)   |   
 \______/  /__/     \__\ | _| `._____|   \__/     |__| |_______/    
    """
    print(logo)

def print_face():
    face = r"""
      _____
     /     \\
    |  O O  |
    |   >   |
     \  \_/ /
      \_____/
    """
    print(face)

def Jarvis():
    # Print the logo and face first before greeting
    print_logo()
    print_face()

    # Greeting after printing the logo and face
    print("Hello, i'm Jarvis. How can I help you today?", flush=True)

    while True:
        command = input("> ").strip().lower()

        if not command:
            continue

        if "hello" in command:
            print("Wassup! How was your day?")

        elif command.startswith("open "):
            words = command.split()
            if len(words) > 1:
                site_or_app = ' '.join(words[1:]).lower()

                # Dictionary for websites
                websites = {
                    "youtube": "https://www.youtube.com",
                    "yt": "https://www.youtube.com",
                    "google": "https://www.google.com",
                    "gmail": "https://mail.google.com",
                    "github": "https://github.com",
                    "reddit": "https://www.reddit.com",
                    "amazon": "https://www.amazon.com",
                    "stackoverflow": "https://stackoverflow.com",
                    "comptia": "https://login.comptia.org",
                    "chess": "https://www.chess.com/play",
                    "monkeytype": "https://monkeytype.com",
                    "dictionary": "https://www.dictionary.com",
                    "microsoft": "https://www.microsoft.com",
                    "excel": "https://excel.cloud.microsoft/?wdOrigin=APPHOME-WEB.DIRECT%2CAPPHOME-WEB.UNAUTH%2CAPPHOME-WEB.SHELL.SIGNIN",           
                }

                # Dictionary for common applications
                apps = {
                    "notepad": "notepad.exe",
                    "calculator": "calc.exe",
                    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
                    "steam": "C:\\Program Files (x86)\\Steam\\Steam.exe",
                    "discord": "C:\\Users\\User\\AppData\\Local\\app-*\\Discord.exe",
                    "spotify": "C:\\Users\\EthanWinstead\\Library\\Caches\\com.spotify.client\\Spotify.exe",
                    "pycharm": "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.3.4\\bin\\pycharm64.exe",
                }

                if site_or_app in websites:
                    url = websites[site_or_app]
                    print(f"Gotcha Big boss opening {url}...")
                    webbrowser.open(url)
                elif site_or_app in apps:
                    app_path = apps[site_or_app]
                    print(f"Gotcha Big boss opening {site_or_app}...")
                    os.startfile(app_path)
                else:
                    print(f"Sorry, I don't recognize '{site_or_app}'. Try using a full URL or specifying an installed application.")
            else:
                print("Please specify what to open (e.g., 'open YouTube' or 'open Notepad').")

        elif "roll" in command:
            print("You rolled a", random.randint(1, 6))

        elif "exit" in command:
            print("Don't keep me waiting boss")
            break

        elif "good" in command:
            print("As always, sir, delighted to be of service.")

        elif "bad" in command:
            print("Tell me about it, sir. I'm here to help.")

        elif "thank you" in command:
            print("You're welcome, sir.")

        else:
            print("I'm sorry, I don't understand.")
     
if __name__ == "__main__":
    Jarvis()

# In Jarvis.py, we have a chatbot function that can open a web browser, roll a die, and exit the program.
# The chatbot function will keep asking questions until the user types "exit".
# The chatbot function will open a web browser if the user types "open" followed by a URL.
