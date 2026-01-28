import pyttsx3
import speech_recognition as sr
import datetime
import random
import webbrowser

# ================== TEXT TO SPEECH ==================
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ================== SPEECH TO TEXT ==================
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        speak("Sorry, please say that again.")
        return ""

# ================== RANDOM MUSIC ==================
def play_random_music():
    songs = [
        "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "https://www.youtube.com/watch?v=3tmd-ClpJxA",
        "https://www.youtube.com/watch?v=l482T0yNkeo"
    ]
    webbrowser.open(random.choice(songs))

# ================== MAIN ==================
def main_process():
    speak("Hello, I am Jarvis. How can I help you?")

    while True:
        request = take_command()

        if request == "":
            continue

        if "new task" in request:
            task = request.replace("new task", "").strip()

            if task != "":
                speak("Your new task is " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")
            else:
                speak("Please say the task clearly.")

        elif "time" in request:
            now = datetime.datetime.now()
            speak("The current time is " + now.strftime("%I %M %p"))

        elif "play music" in request:
            speak("Playing music")
            play_random_music()

        elif "open youtube" in request:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "exit" in request or "stop" in request:
            speak("Goodbye")
            break

        else:
            speak("I heard you say " + request)

# ================== START ==================
if __name__ == "__main__":
    main_process()
