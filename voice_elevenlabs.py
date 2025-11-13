import os
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from dotenv import load_dotenv
load_dotenv()
elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)


def to_voice(text):
    audio = elevenlabs.text_to_speech.convert(
    text=text,
    voice_id="21m00Tcm4TlvDq8ikWAM",
    model_id="eleven_flash_v2_5",
    output_format="mp3_44100_128",
)
    play(audio)
    return


if __name__ == "__main__":
    text = "this a placeholder text just to test the voice of the AI"
    to_voice(text)