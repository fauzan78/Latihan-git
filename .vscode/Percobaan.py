import pyttsx3
import speech_recognition as sr
import os
import subprocess
import openai

# API Key OpenAI (ganti dengan kunci Anda)
openai.api_key = "0"

# Inisialisasi Pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Kecepatan bicara
engine.setProperty("volume", 0.9)  # Volume
app_paths = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "valorant": r"C:\Riot Games\Riot Client\RiotClientServices.exe",
    "notepad": r"C:\Windows\System32\notepad.exe",
    "discord": r"C:\Users\Ozann\Desktop\Discord.lnk",
    "spotify": r"C:\Users\Ozann\Desktop\Spotify.lnk",
    "visual studio code": r"C:\Users\Ozann\Desktop\Visual Studio Code.lnk",
    "letsvpn": r"C:\Users\Ozann\Desktop\LetsVPN.lnk",
    "macro recorder": r"C:\Users\Public\Desktop\Macro Recorder.lnk",
    "tencent meeting": r"C:\Users\Public\Desktop\Tencent Meeting.lnk",
    "nvidia": r"C:\Users\Public\Desktop\NVIDIA.lnk",
    "meta editor 5": r"C:\Users\Public\Desktop\MetaEditor 5.lnk",
    "meta trader 5": r"C:\Users\Public\Desktop\MetaTrader 5.lnk",
    "microsoft edge": r"C:\Users\Public\Desktop\Microsoft Edge.lnk",
    "obs studio": r"C:\Users\Public\Desktop\OBS Studio.lnk",
    "riot client": r"C:\Users\Public\Desktop\Riot Client.lnk",
    "we chat": r"C:\Users\Public\Desktop\WeChat.lnk",
    "a space for the unbound": r"C:\Users\Ozann\Desktop\A Space for the Unbound",
    "bigbear win": r"C:\Users\Ozann\Desktop\bigbear-win",
    "capcut": r"C:\Users\Ozann\Desktop\CapCut.lnk",
    "internet download manager": r"C:\Users\Ozann\Desktop\Internet Download Manager.lnk",
    "memu": r"C:\Users\Ozann\Desktop\MEmu.lnk",
    "multi memu": r"C:\Users\Ozann\Desktop\Multi-MEmu.lnk",
    "notion": r"C:\Users\Ozann\Desktop\Notion.lnk",
    "person 1 chrome": r"C:\Users\Ozann\Desktop\Person 1 - Chrome.lnk",
    "roblox player": r"C:\Users\Ozann\Desktop\Roblox Player.lnk",
    "roblox studio": r"C:\Users\Ozann\Desktop\Roblox Studio.lnk",
    # Menambahkan aplikasi lain sesuai kebutuhan
}
stop_speaking = False  # Global flag untuk menghentikan bicara


def chatbot_response(prompt):
    """Mendapatkan respons dari OpenAI GPT."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def open_application(command):
    """Open application based on the command."""
    app_name = command.strip().lower()
    if app_name in app_paths:
        try:
            print(f"Membuka aplikasi {app_name}...")
            os.startfile(app_paths[app_name])
            speak(f"Membuka {app_name}.")
        except Exception as e:
            speak(f"Gagal membuka {app_name}: {str(e)}")
    else:
        speak(f"Aplikasi {app_name} tidak ditemukan dalam daftar.")
def speak(text):
    """Fungsi berbicara menggunakan pyttsx3."""
    global stop_speaking
    stop_speaking = False  # Reset flag sebelum berbicara

    def on_word(name, location, length):
        """Callback untuk memeriksa apakah harus berhenti."""
        if stop_speaking:
            engine.stop()

    engine.connect("started-word", on_word)  # Hubungkan callback
    engine.say(text)
    engine.runAndWait()


def recognize_speech():
    """Mengenali perintah suara dari mikrofon."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = recognizer.recognize_google(audio, language="id-ID")
            return command.lower()
        except sr.UnknownValueError:
            return "Saya tidak mendengar dengan jelas."
        except sr.RequestError as e:
            return f"Kesalahan layanan pengenalan suara: {str(e)}"


def handle_command(command):
    """Menangani perintah dari pengguna."""
    global stop_speaking

    if "berhenti" in command:
        stop_speaking = True
        print("Berhenti berbicara...")
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_application(app_name)
    elif "close" in command:
        app_name = command.replace("close", "").strip()
        speak(f"Menutup {app_name}.")
    elif "keluar" in command:
        speak("Sampai jumpa!")
        exit(0)
    elif "who am i" in command or "siapa aku" in command or "siapa fauzan" in command:
        speak("Fauzan adalah pemilik robot Lexa.")
    elif "who are you" in command or "siapa kamu" in command:
        speak("Lexa adalah robot yang dibuat oleh Fauzan Fajar Pratama.")
    else:
        # OpenAI GPT untuk perintah lainnya
        prompt = command.replace("lexa", "").strip()
        response = chatbot_response(prompt)
        speak(response)


def main():
    """Fungsi utama untuk menangani perintah."""
    speak("Lexa siap mendengarkan. Katakan 'Lexa' diikuti dengan perintah Anda.")
    while True:
        global stop_speaking
        command = recognize_speech()
        if "lexa" in command:
            handle_command(command)
        elif "berhenti" in command:
            stop_speaking = True
            print("Berhenti berbicara...")
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            open_application(app_name)
        elif "close" in command:
            app_name = command.replace("close", "").strip()
            speak(f"Menutup {app_name}.")
        elif "keluar" in command:
            speak("Sampai jumpa!")
            exit(0)
        elif "who am i" in command or "siapa aku" in command or "siapa fauzan" in command:
            speak("Fauzan adalah pemilik robot Lexa.")
        elif "who are you" in command or "siapa kamu" in command:
            speak("Lexa adalah robot yang dibuat oleh Fauzan Fajar Pratama.")
        else:
            print("Kata kunci 'Lexa' tidak terdeteksi. Mengabaikan input.")


if __name__ == "__main__":
    main()
