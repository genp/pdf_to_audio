import PyPDF2
import pyttsx3

def pdf_to_audio(pdf_path, audio_path):
    """Reads a PDF file and saves it as an audio file.

    Args:
        pdf_path: Path to the PDF file.
        audio_path: Path to save the audio file.
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        print(f"Text extracted from '{pdf_path}'")
        # print a sample of text
        print(text[:100])
        engine = pyttsx3.init()
        # set the rate of speech
        engine.setProperty('rate', 150)
        # set the volume
        engine.setProperty('volume', 0.9)
        # save the text to audio
        engine.save_to_file(text, audio_path)
        # wait for the text to be saved
        print(f"Saving audio to '{audio_path}'")
        engine.runAndWait()
        print(f"PDF content saved to '{audio_path}'")

    except FileNotFoundError:
        print(f"Error: PDF file not found at '{pdf_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_file = 'example.pdf'
    audio_file = 'output.mp3'
    pdf_to_audio(pdf_file, audio_file)