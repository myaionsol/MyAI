import speech_recognition as sr
import pyttsx3

def recognize_speech():
    """
    Captures audio from the microphone and converts it into text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def speak_response(response_text):
    """
    Converts text into speech for a more natural interaction.
    """
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()

if __name__ == "__main__":
    # Example of voice interaction
    user_input = recognize_speech()
    if user_input:
        # Simulating response from the AI agent
        response = f"You said '{user_input}', let me process that."
        print(response)
        speak_response(response)
