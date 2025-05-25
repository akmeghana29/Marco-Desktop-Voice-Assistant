This desktop voice assistant, Marco, is built using Python and follows a modular structure. The backend is developed with Flask to allow REST API integration in future updates. Voice input is captured using the SpeechRecognition library and processed using conditional logic. pyttsx3 is used for offline text-to-speech feedback. For actions like opening websites, YouTube playback, or sending WhatsApp messages, it integrates pywhatkit and webbrowser. Notes are saved locally as text files and can be read back using voice commands. The CLI interface is set up in cli.py to allow direct terminal execution. Each functionality is wrapped in functions inside marco.py, and routing support via routes.py prepares it for web integration. The assistant listens continuously in a loop until given an exit command. It’s lightweight, efficient, and built to feel like a personal digital companion.

How to Use the Assistant:

Install Python 3.8+ from python.org
Open terminal or CMD and run: git clone https://github.com/your-username/marco-assistant.git
Or download the ZIP, extract it, and navigate into the folder
Navigate to the main directory using cd path\to\Marco Assistant
Install required libraries using pip install -r requirements.txt
If requirements.txt is missing, run:
pip install pyttsx3 speechrecognition pywhatkit wikipedia pyjokes Flask
Then run the assistant using: python cli.py
Allow microphone access and speak clearly after the beep

Commands You Can Use: 

"Increase Volume"
"Decrease VOlume"
"Mute the Volume"
"Unmute the mic"
"Take notes"
"Save the notes"
"Read Notes"
"Open Saved Notes"
"Open (name of the note)"
"Play Music"
"Stop(to stop the assistant)"
"Search (anything of choice) from wikipedia"
"Open Downloads"
"Open Documents"
"Open YouTube"
"Open Google"
"Open Gmail"
"Whats the weather today"
"What's the time now"
"Who are you"
"Who made you"
"What's in today's news"
"Take a photo"
"Search (anything) from internet"
"log off(shut the the system)"
