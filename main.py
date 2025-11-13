from gemini import Gemini
from prompt import get_full_prompt
from screenshot import get_screenshot
from voice_recorder import record_voice
from speech_recognition import recognize_voice
# from voice_pyttsx3 import to_voice
from voice_elevenlabs import to_voice

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
    result = kara.generate_text(prompt)
    to_voice(result)
    print(result)

def voice_control_with_print():
    audio_path = record_voice()
    print(f"Audio recorded: {audio_path}")

    print("Recognizing speech...")
    user_prompt = recognize_voice(audio_path)
    print(f"User said: {user_prompt}")

    prompt = get_full_prompt(user_prompt)

    print("Generating response...")
    kara = Gemini()
    result = kara.generate_text(prompt)
    print(f"Model response:\n{result}")

    print("Playing response...")
    to_voice(result)
    print("Done.")

    return result



if __name__ == "__main__":
    voice_control_with_print()

