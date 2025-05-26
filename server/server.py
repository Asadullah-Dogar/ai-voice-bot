import socket
import whisper

from inference_utils import load_model, generate_response



from tts_utils import text_to_wav
import os

HOST = 'localhost'
PORT = 5001

# Load models
print("Loading models...")
tokenizer, model = load_model()
stt_model = whisper.load_model("base")
print("Models loaded. Server is starting...")

# Start server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            # Receive audio length
            length_bytes = conn.recv(4)
            if not length_bytes:
                continue
            length = int.from_bytes(length_bytes, 'big')

            # Receive audio data
            data = b""
            while len(data) < length:
                packet = conn.recv(4096)
                if not packet:
                    break
                data += packet

            with open("received.wav", "wb") as f:
                f.write(data)

            # Transcribe audio
            result = stt_model.transcribe("received.wav")
            user_input = result['text']
            print("User said:", user_input)

            # Generate LLM response
            response = generate_response(tokenizer, model, user_input)
            print("Bot replied:", response)

            # Convert response to speech
            text_to_wav(response, "output.wav")

            # Send back audio response
            with open("output.wav", "rb") as f:
                out_data = f.read()
                conn.sendall(len(out_data).to_bytes(4, 'big') + out_data)

            # Cleanup
            os.remove("received.wav")
            os.remove("output.wav")
