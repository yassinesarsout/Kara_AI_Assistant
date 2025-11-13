import wave
import sys
import datetime


import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 22050
RECORD_SECONDS = 5

def record_voice():
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    audio_path = f'audio/audio_prompt_{timestamp}.wav'
    with wave.open(audio_path, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
            wf.writeframes(stream.read(CHUNK))
        print('Done')

        stream.close()
        p.terminate()
    
    return audio_path