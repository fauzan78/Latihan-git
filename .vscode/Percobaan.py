import pyttsx3
import speech_recognition as sr
import os
import subprocess
import openai
from AppOpener import open, close
# Set OpenAI API key
openai.api_key = "0"


engine = pyttsx3.init()
engine.setProperty("rate", 150)  #speed
engine.setProperty("volume", 0.9) #volume


stop_speaking = False

def chatbot_response(prompt):
    """Get response from OpenAI GPT."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def speak(text):
    """Speak the provided text."""
    global stop_speaking
    stop_speaking = False

    def on_word(name, location, length):
        """Callback for each word spoken."""
        if stop_speaking:
            engine.stop()

    engine.connect("started-word", on_word)
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Recognize speech from the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10)
            command = recognizer.recognize_google(audio, language="id-ID")
            return command.lower()
        except sr.UnknownValueError:
            return "Saya tidak mendengar dengan jelas."
        except sr.RequestError as e:
            return f"Kesalahan layanan pengenalan suara: {str(e)}"

def handle_command(command):
    """Handle specific commands."""
    global stop_speaking

    if "stop" in command:
        stop_speaking = True
        speak("Baik, saya berhenti.")
    elif "open" in command:
        appname = command.replace("lexa open", "").strip()
        open(app_name, match_closest=True)
    elif "close" in command:
        appname = command.replace("lexa close", "").strip()
        close(app_name, match_closest=True)
    elif "keluar" in command:
        speak("Sampai jumpa!")
        exit(0)
    else:
        prompt = command.replace("lexa", "").strip()
        response = chatbot_response(prompt)
        speak(response)

def main():
    """Main function to handle commands."""
    speak("Lexa siap mendengarkan. Katakan 'Lexa' diikuti dengan perintah Anda.")
    while True:
        command = recognize_speech()
        if "lexa" in command:
            handle_command(command)
        else:
            print("Kata kunci 'Lexa' tidak terdeteksi. Mengabaikan input.")

if __name__ == "__main__":
    main()