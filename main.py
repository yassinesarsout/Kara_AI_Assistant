from gemini import Gemini
from prompt import get_full_prompt
from screenshot import get_screenshot

def screen_reader():
    screenshot = get_screenshot()

user_prompt = input('What is on your mind?\n')
prompt = get_full_prompt(user_prompt)
Kara = Gemini()
print(Kara.generate_text(prompt))

