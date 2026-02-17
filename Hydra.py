import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import datetime
import time
import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import os

# TTS Engine
print("=== HYDRA WITH WAKE WORD ===")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)
    print(f"✅ Voice: {voices[0].name}")
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

output_callback = None
assistant_running = False
listening_for_wake_word = True
waiting_for_command = False

def set_output_callback(callback):
    global output_callback
    output_callback = callback

def speak(text):
    print(f"🔊 Speaking: {text}")
    if output_callback:
        output_callback(f"🤖 {text}")
    try:
        engine.say(text)
        engine.runAndWait()
        print("✅ Speech completed")
    except Exception as e:
        print(f"❌ Speech error: {e}")
    time.sleep(0.3)

def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=0.5)
            if output_callback:
                if waiting_for_command:
                    output_callback("🎤 Listening for command...")
                else:
                    output_callback("👂 Listening for 'Hey Hydra'...")
            audio = listener.listen(source, timeout=3, phrase_time_limit=3)
    except Exception as e:
        return "none"
    
    try:
        command = listener.recognize_google(audio).lower()
        if output_callback:
            output_callback(f"👤 Heard: {command}")
        print(f"🎤 Recognized: {command}")
        return command
    except:
        return "none"

def process_command(command):
    global waiting_for_command
    waiting_for_command = False
    
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        
    elif 'date' in command:
        today = datetime.date.today()
        speak(f"Today's date is {today.strftime('%B %d, 2026')}")
        
    elif 'play' in command:
        song = command.replace('play', '').strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
        
    elif 'who is' in command or 'what is' in command:
        try:
            info = wikipedia.summary(command, sentences=2)
            speak(info)
        except Exception:
            speak("Sorry, I couldn't fetch that information.")
            
    elif 'open google' in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
        
    elif 'open youtube' in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
        
    elif 'game' in command or 'games' in command:
        webbrowser.open("https://poki.com")
        speak("Opening games website")
        
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
        
    elif 'search' in command:
        search_term = command.replace('search', '').strip()
        pywhatkit.search(search_term)
        speak(f"Searching for {search_term}")
        
    elif 'stop' in command or 'exit' in command:
        speak("Goodbye Master! Shutting down.")
        return False
        
    else:
        speak("Try time, date, play music, joke, or stop.")
    
    return True

def run_assistant():
    global assistant_running, listening_for_wake_word, waiting_for_command
    
    speak("Hey Hydra is online! Say 'Hey Hydra' to activate me.")
    
    while assistant_running:
        command = listen()
        
        if command == "none":
            continue
            
        # Wake word detection
        if "hey hydra" in command and listening_for_wake_word:
            speak("Yes Master?")
            listening_for_wake_word = False
            waiting_for_command = True
            
            # Listen for actual command
            command = listen()
            if command != "none":
                if not process_command(command):
                    assistant_running = False
                listening_for_wake_word = True  # Back to wake word listening
            else:
                listening_for_wake_word = True
                
        # Handle commands when already active
        elif waiting_for_command:
            if not process_command(command):
                assistant_running = False
            listening_for_wake_word = True
            waiting_for_command = False

# GUI Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("HYDRA - Wake Word Edition 🚀")
app.geometry("750x750")

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=20, fill="both", expand=True)

title_label = ctk.CTkLabel(frame, text="🗣️ HYDRA", font=("Consolas", 28, "bold"))
title_label.pack(pady=(20, 10))

subtitle_label = ctk.CTkLabel(frame, text="Wake Word: 'HEY HYDRA' | Say to activate!", 
                             font=("Consolas", 16))
subtitle_label.pack(pady=(0, 20))

status_label = ctk.CTkLabel(frame, text="👂 Status: Listening for 'Hey Hydra'...", 
                           font=("Consolas", 14))
status_label.pack(pady=(0, 10))

chat_box = ctk.CTkTextbox(frame, width=680, height=320, font=("Consolas", 11))
chat_box.pack(pady=10)
chat_box.insert("end", "=== HYDRA WAKE WORD EDITION ===\n")
chat_box.insert("end", "✅ Speech engine ready!\n")
chat_box.insert("end", "🎙️ Say 'HEY HYDRA' then any command\n")
chat_box.insert("end", "Examples: 'Hey Hydra time', 'Hey Hydra joke'\n")
chat_box.configure(state="disabled")

def add_message(message):
    chat_box.configure(state="normal")
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    chat_box.insert("end", f"[{timestamp}] {message}\n")
    chat_box.configure(state="disabled")
    chat_box.see("end")

set_output_callback(add_message)

button_frame = ctk.CTkFrame(frame)
button_frame.pack(pady=15)

def start_hydra():
    global assistant_running
    if assistant_running:
        add_message("⚙️ HYDRA already running!")
        return
    assistant_running = True
    status_label.configure(text="🟢 Status: Active - Listening for 'Hey Hydra'")
    add_message("🚀 HYDRA activated! Say 'Hey Hydra'...")
    threading.Thread(target=run_assistant, daemon=True).start()

def stop_hydra():
    global assistant_running
    assistant_running = False
    status_label.configure(text="🔴 Status: Stopped")
    add_message("⏹️ HYDRA stopped.")

def save_logs():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Save HYDRA Logs"
    )
    if file_path:
        try:
            logs = chat_box.get("1.0", "end")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(logs)
            add_message("💾 Logs saved!")
        except Exception as e:
            add_message(f"❌ Save error: {e}")

# Clean buttons - TEST REMOVED
start_btn = ctk.CTkButton(button_frame, text="🚀 START HYDRA", command=start_hydra, 
                         width=150, height=50, font=("Consolas", 13, "bold"), fg_color="#1f6aa5")
stop_btn = ctk.CTkButton(button_frame, text="⏹️ STOP", command=stop_hydra, 
                        width=130, height=50, fg_color="#6a1f44")
save_btn = ctk.CTkButton(button_frame, text="💾 SAVE LOGS", command=save_logs, 
                        width=150, height=50)

start_btn.grid(row=0, column=0, padx=15, pady=10)
stop_btn.grid(row=0, column=1, padx=15, pady=10)
save_btn.grid(row=0, column=2, padx=15, pady=10)

footer = ctk.CTkLabel(app, text="Made by Yash | Wake Word: HEY HYDRA | Feb 2026", 
                     font=("Arial", 11))
footer.pack(pady=15)



app.mainloop()
