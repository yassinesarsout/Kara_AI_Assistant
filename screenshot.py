import os 
import datetime
from mss import mss

def get_screenshot():
    if not os.path.exists('screenshots'):
        os.mkdir('screenshots')
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f'screenshots/monitor1-{timestamp}.png'
    with mss() as sct:
        sct.shot(output=filename)
    return filename

if __name__ == "__main__":
    get_screenshot()
    