import os
import time
import csv
import whisper
import torch
from pathlib import Path

# -----------------------------
# CONFIGURATION SECTION
# -----------------------------

# Folder that contains your audio files (mp3, wav, m4a, etc.)
AUDIO_FOLDER = "audio"

# Models you want to test
MODELS = ["tiny", "small"]

# Where to save the timing results
OUTPUT_CSV = "results.csv"

# Automatically choose GPU if available
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(DEVICE)

# -----------------------------
# HELPER FUNCTION
# -----------------------------

def get_audio_files(folder):
    """Return a list of all supported audio files in the given folder."""
    exts = [".mp3", ".wav", ".m4a", ".flac", ".ogg", ".mp4"]
    files = [f for f in Path(folder).glob("*") if f.suffix.lower() in exts]
    return files

# -----------------------------
# MAIN SCRIPT
# -----------------------------

# Make sure the folder exists
if not os.path.exists(AUDIO_FOLDER):
    print(f"❌ Folder '{AUDIO_FOLDER}' not found.")
    exit(1)

# Get all audio files in that folder
audio_files = get_audio_files(AUDIO_FOLDER)
if not audio_files:
    print(f"❌ No audio files found in '{AUDIO_FOLDER}'.")
    exit(1)

# Prepare the CSV file to record results
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Write header line
    writer.writerow(["model", "audio_file", "elapsed_seconds", "text"])

    # Loop through each model
    for model_name in MODELS:
        print(f"\n🔹 Loading model: {model_name}")
        start_load = time.time()
        model = whisper.load_model(model_name, device=DEVICE)
        print(f"✅ Model loaded in {time.time() - start_load:.1f} seconds")

        # Loop through each audio file
        for audio_path in audio_files:
            print(f"🎧 Transcribing: {audio_path.name} with {model_name} ...")
            start_time = time.time()

            # Transcribe the file
            result = model.transcribe(str(audio_path))

            end_time = time.time()
            elapsed = end_time - start_time

            # Print the result and time
            print(f"🕒 Done in {elapsed:.2f} seconds")
            print(f"📝 Transcript (first 100 chars): {result['text'][:100]!r}\n")

            # Write data to CSV
            writer.writerow([model_name, audio_path.name, round(elapsed, 3),result["text"]])
            f.flush()  # save immediately to disk

print(f"\n✅ All tests done! Results saved to '{OUTPUT_CSV}'")
