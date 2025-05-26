# import pyttsx3
# import tempfile
# from pydub import AudioSegment

# def text_to_wav(text, output_path="output.wav"):
#     engine = pyttsx3.init()
    
#     # Save to a temporary .wav file
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#         tmp_path = tmp_file.name
    
#     engine.save_to_file(text, tmp_path)
#     engine.runAndWait()

#     # Convert to final .wav format
#     audio = AudioSegment.from_wav(tmp_path)
#     audio.export(output_path, format="wav")




# import pyttsx3
# import tempfile
# import time
# import os
# from pydub import AudioSegment

# def text_to_wav(text, output_path="output.wav"):
#     engine = pyttsx3.init()

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#         tmp_path = tmp_file.name

#     engine.save_to_file(text, tmp_path)
#     engine.runAndWait()

#     # Wait briefly to ensure file is fully written
#     time.sleep(0.5)

#     # Load the temp wav and export to output_path
#     audio = AudioSegment.from_wav(tmp_path)
#     audio.export(output_path, format="wav")

#     # Clean up temp file
#     os.remove(tmp_path)




# import pyttsx3

# def text_to_wav(text, output_path="output.wav"):
#     """
#     Convert given text to speech and save as a WAV file.

#     Args:
#         text (str): The text to convert to speech.
#         output_path (str): The output WAV filename (default "output.wav").
#     """
#     engine = pyttsx3.init()
#     engine.save_to_file(text, output_path)
#     engine.runAndWait()
#     print(f"TTS audio saved to {output_path}")





# import pyttsx3
# import time

# def text_to_wav(text, output_path="output.wav"):
#     engine = pyttsx3.init()
#     engine.save_to_file(text, output_path)
#     engine.runAndWait()
#     time.sleep(0.5)  # small delay to ensure file write completion
#     print(f"TTS audio saved to {output_path}")

# if __name__ == "__main__":
#     text_to_wav("This is a test.", "output.wav")


# import pyttsx3

# def text_to_wav(text, output_path="output.wav"):
#     engine = pyttsx3.init()
#     engine.save_to_file(text, output_path)
#     engine.runAndWait()


# import time

# text_to_wav("Hello world", "output.wav")
# time.sleep(1)  # wait 1 second to ensure file is saved
# import os

# print(f"output.wav size: {os.path.getsize('output.wav')} bytes")








# import pyttsx3
# import tempfile
# import time
# import os
# from pydub import AudioSegment

# def text_to_wav(text, output_path="output.wav"):
#     engine = pyttsx3.init()

#     # Generate a temporary file path
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#         tmp_path = tmp_file.name

#     # Save TTS output to the temporary WAV file
#     engine.save_to_file(text, tmp_path)
#     engine.runAndWait()

#     # Ensure the file is fully written before accessing it
#     time.sleep(0.5)

#     # Convert and save the final output.wav in compatible format
#     try:
#         audio = AudioSegment.from_wav(tmp_path)
#         audio.export(output_path, format="wav")
#     finally:
#         # Clean up the temp file
#         if os.path.exists(tmp_path):
#             os.remove(tmp_path)










import pyttsx3
import tempfile
import time
import os
import wave
import shutil

def text_to_wav(text, output_path="output.wav"):
    engine = pyttsx3.init()

    # Generate a temporary filename
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_path = tmp_file.name

    engine.save_to_file(text, tmp_path)
    engine.runAndWait()

    # Wait briefly to ensure file is written
    time.sleep(0.5)

    # Ensure the WAV is valid (re-save via wave module)
    try:
        with wave.open(tmp_path, 'rb') as rf:
            params = rf.getparams()
            frames = rf.readframes(rf.getnframes())

        with wave.open(output_path, 'wb') as wf:
            wf.setparams(params)
            wf.writeframes(frames)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
