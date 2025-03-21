from pdf_to_audio import pdf_to_audio

# Input PDF path
pdf_path = "/Users/gen/Downloads/Anytime Continual Learning for Open Vocabulary Classification.pdf"

# Output audio path (same name and location as PDF but with .mp3 extension)
audio_path = pdf_path.rsplit('.', 1)[0] + '.mp3'

# Convert PDF to audio
pdf_to_audio(pdf_path, audio_path)
