import pyttsx3

engine =pyttsx3.init()

def to_voice(text):
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    text = "this a placeholder text just to test the voice of the ai"
    to_voice(text)