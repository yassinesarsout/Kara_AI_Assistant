from gemini import Gemini
from prompt import get_full_prompt
from screenshot import get_screenshot
from voice_recorder import record_voice
from speech_recognition import recognize_voice

def screen_reader():
    screenshot = get_screenshot()

def terminal():
    user_prompt = input('What is on your mind?\n')
    prompt = get_full_prompt(user_prompt)
    Kara = Gemini()
    print(Kara.generate_text(prompt))

def voice_control():
    audio_path = record_voice()
    user_prompt = recognize_voice(audio_path)
    prompt = get_full_prompt(user_prompt)
    kara = Gemini()
    print(kara.generate_text(prompt))

if __name__ == "__main__":
    voice_control()

