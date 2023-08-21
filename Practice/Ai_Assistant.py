import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                return command.strip()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return ""

def run_alexa():
    while True:
        command = take_command()
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)
            break  # Exit the loop after showing the result
        elif 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
            break  # Exit the loop after showing the result
        elif 'tell me about' in command:
            look_for = command.replace('tell me about', '')
            info = wikipedia.summary(look_for, 1)
            print(info)
            talk(info)
            break  # Exit the loop after showing the result
        elif 'joke' in command:
            talk(pyjokes.get_joke())
            break  # Exit the loop after showing the result
        elif 'date' in command:
            talk("Sorry, I am not available for that.")
            break  # Exit the loop after showing the result
        else:
            talk("I am going to search it for you.")
            pywhatkit.search(command)
            break  # Exit the loop after showing the result

run_alexa()
