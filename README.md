🗣️ HYDRA - AI Voice Assistant (Jarvis Clone)
<div align="center">
"Hey Hydra time" → "The time is 5:18 PM"
"Hey Hydra joke" → Random funny joke
Always listening - Zero button clicks!

[
[
[

</div>
✨ Features
🎙️ Wake Word	"Hey Hydra" 
🗣️ Speech	Natural Microsoft voices
👤 Voice Input	Google Speech Recognition
🌐 Web Control	YouTube, Google, Poki Games
🎨 GUI	Modern CustomTkinter dark theme
💾 Logs	Chat history + Save feature
🚀 30-Second Setup
bash
git clone https://github.com/YOUR_USERNAME/HYDRA-Voice-Assistant.git
cd HYDRA-Voice-Assistant
pip install -r requirements.txt
python HYDRA.py
HYDRA auto-starts & listens for "Hey Hydra"!

🎯 Voice Commands
Command	Response
Hey Hydra time	Current time
Hey Hydra date	Today's date (Feb 17, 2026)
Hey Hydra joke	Random joke
Hey Hydra play [song]	YouTube playback
Hey Hydra search [term]	Google search
Hey Hydra who is [name]	Wikipedia summary
Hey Hydra open google	Opens Google
Hey Hydra open youtube	Opens YouTube
Hey Hydra games	Poki.com games
Hey Hydra stop	Graceful shutdown
📱 Demo Flow
text
F5 → "Hey Hydra is active!" (auto)
👤 "Hey Hydra time" 
🤖 "The time is 5:18 PM"
👤 "Hey Hydra joke"
🤖 "Why don't programmers like nature? It has too many bugs!"
🛠️ Tech Stack
python
customtkinter==5.2.2      # Modern dark GUI
pyttsx3==2.90            # Windows SAPI5 TTS
speechrecognition==3.10.0 # Google Speech API
pywhatkit==5.4           # YouTube automation
wikipedia==1.4.0         # Knowledge base
pyjokes==1.0.0           # Entertainment
numpy==1.24.3            # Audio processing
📦 Complete Installation
Prerequisites
text
✓ Python 3.8+ 
✓ Windows 10/11
✓ Microphone + Speakers
✓ Internet (Google Speech API)
One-Command Setup
bash
pip install -r requirements.txt
python HYDRA.py
Troubleshooting
text
❌ No speech → Windows Sound → App volume → Python.exe
❌ Mic error → Settings → Privacy → Microphone → Allow apps  
❌ ImportError → pip install pyaudio --upgrade
📸 Screenshots
<div align="center"> <img src="https://via.placeholder.com/350x250/1a202c/60a5fa?text=Modern+Dark+GUI" width="45%" alt="HYDRA GUI"> <img src="https://via.placeholder.com/350x250/1a202c/60a5fa?text=Hey+Hydra+Active" width="45%" alt="Always Listening"> </div>
🏗️ Project Structure
text
HYDRA-Voice-Assistant/
├── HYDRA.py            # Main application (~400 lines)
├── requirements.txt    # Dependencies
├── README.md          # This file
└── .gitignore         # Python ignores
🔧 Customization Guide
Change Wake Word
python
# Line ~95 - Edit this:
if "hey jarvis" in command:  # Your choice!
Voice Settings
python
engine.setProperty('rate', 200)    # Speed (150-250)
engine.setProperty('volume', 1.0)  # Volume (0.0-1.0)
Add New Commands
python
elif 'weather' in command:
    speak("Opening weather app")
    os.system("start ms-weather:")
🤝 Contributing
Fork repository

git checkout -b feature/cool-feature

git commit -m "Add cool feature"

git push origin feature/cool-feature

Open Pull Request

📄 License
MIT License - Free to use, modify, distribute!

👨‍💻 Author
Yash Chhipa
B.Tech 1st Year | Web Developer | AI Enthusiast
📍 Jaipur, Rajasthan, India (Studying in Lucknow)
📧 yashchhipa8@gmail.com 
💼 LinkedIn 

🙏 Acknowledgments
text
🔹 CustomTkinter - Stunning GUI library
🔹 pyttsx3 - Reliable Windows TTS  
🔹 SpeechRecognition - Google STT
🔹 Perplexity AI - Debug assistance
🔹 Yash's debugging skills! 💪
⭐ Support the Project
text
⭐ Star if you like it!
🍴 Fork for your version
🐛 Issues → Help improve!
<div align="center">
🎙️ Built with ❤️ in Jaipur, India
"Hey Hydra" → Your personal AI companion!
February 2026

</div>
