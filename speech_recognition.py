import torch, whisper
MODEL = "small"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def recognize_voice(audio_path):
    model = whisper.load_model(MODEL, device=DEVICE)
    result = model.transcribe(str(audio_path))
    return result["text"]