import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak a response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def recognize_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen to the user's voice
        try:
            command = recognizer.recognize_google(audio).lower()  # Recognize the voice command
            print("You said: " + command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            command = ""
        except sr.RequestError as e:
            print("Could not request results; check your network connection.")
            command = ""
        return command

# Main function to handle voice commands
def main():
    speak("Hello! How can I assist you?")
    while True:
        command = recognize_command()
        if "what is your name" in command:
            speak("I am your voice assistant.")
        elif "what time is it" in command:
            current_time = datetime.datetime.now().strftime("%H:%M %p")
            speak("The current time is " + current_time)
        elif "exit" in command or "quit" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    main()
