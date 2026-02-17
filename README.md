# 🗣️ HYDRA – Wake Word Voice Assistant

HYDRA is a Python-based voice assistant with a modern GUI that listens for a wake word **("Hey Hydra")** and performs tasks like telling time/date, playing music, searching the web, telling jokes, and more.

Built using speech recognition, text-to-speech, and automation libraries, HYDRA is designed as a beginner-friendly yet extensible personal assistant project.

---

## 🚀 Features

- Wake word detection — Say **Hey Hydra** to activate  
- Speech recognition using Google Speech API  
- Text-to-speech voice responses  
- Modern GUI using CustomTkinter  
- Play songs directly on YouTube  
- Wikipedia-based information lookup  
- Open websites (Google, YouTube, Games)  
- Built-in joke generator  
- Web search automation  
- Save assistant conversation logs  
- Multithreading for smooth GUI performance  

---

## 🛠️ Tech Stack

**Language**
- Python  

**Libraries & Tools**
- CustomTkinter — GUI  
- SpeechRecognition — Voice Input  
- pyttsx3 — Text To Speech  
- PyWhatKit — YouTube & Search Automation  
- Wikipedia API — Knowledge Fetching  
- PyJokes — Joke Generator  
- Webbrowser — Browser Automation  
- Threading — Background Processing  

---

## 📦 Installation

### Clone Repository
```bash
git clone https://github.com/Yash-Chhipa/HYDRA-Voice-Assistant.git
cd HYDRA-Voice-Assistant
```

### Install Dependencies
```bash
pip install customtkinter SpeechRecognition pyttsx3 wikipedia pywhatkit pyjokes pyaudio
```

### If PyAudio Fails
```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ Run HYDRA

```bash
python hydra.py
```

---

## 🎤 Usage Guide

1. Click **START HYDRA**  
2. Say → **Hey Hydra**  
3. Speak your command  

### Example Commands
- Hey Hydra time  
- Hey Hydra date  
- Hey Hydra play Arijit Singh songs  
- Hey Hydra who is Albert Einstein  
- Hey Hydra joke  
- Hey Hydra search Python tutorials  
- Hey Hydra stop  

---

## 🖥️ GUI Controls

| Button | Action |
|---|---|
| 🚀 START HYDRA | Starts Assistant |
| ⏹️ STOP | Stops Assistant |
| 💾 SAVE LOGS | Saves Chat Logs |

---

## 🧠 Working Architecture

HYDRA follows a continuous loop:

1. Listen for Wake Word  
2. Activate Command Mode  
3. Process Voice Command  
4. Execute Task  
5. Return to Wake Mode  

---

## 📁 Project Structure

```
HYDRA-Voice-Assistant/
│
├ hydra.py
├ README.md
├ LICENSE
└ requirements.txt (optional)
```

---



## 🤝 Contributing

Contributions are welcome.

**Steps**
1. Fork Repository  
2. Create Feature Branch  
3. Commit Changes  
4. Push Branch  
5. Open Pull Request  

---

## 📜 License

Licensed under the **MIT License**.

---

## 👨‍💻 Maintainer & Contact

<div align="center">

### **Yash Chhipa**  
🚀 Student Developer | Python Enthusiast |
    February 2026

</div>

---

### 📌 Developer Profile

- **GitHub:** https://github.com/Yash-Chhipa  
- **LinkedIn:** www.linkedin.com/in/yash-chhipa-14b43b380 
- **Full Name:** Yash Chhipa  
- **Email:** yashchhipa8@gmail.com
- **Current Study Location:** Lucknow, India  
- **Permanent Residence:** Jaipur, India  
- **Role:** Student | Open Source Contributor  

---

### 🌟 Developer Focus

- Python Development  
- Automation Systems  
- Voice AI Applications  
- GUI Application Development  

---

### 🤝 Collaboration

Interested in:
- Contributing to HYDRA  
- Suggesting new features  
- Reporting bugs  
- Collaborating on AI / Python projects  

Feel free to open an **Issue** or **Pull Request**.

---

<div align="center">

⭐ **If you found this project useful, consider starring the repository!** ⭐  

</div>

---
