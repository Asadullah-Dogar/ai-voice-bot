import socket
import audio_utils
import os

HOST = 'localhost'
PORT = 5001

def send_audio():
    audio_utils.record_audio("input.wav")

    with socket.socket() as s:
        s.connect((HOST, PORT))

        with open("input.wav", "rb") as f:
            data = f.read()
            s.sendall(len(data).to_bytes(4, 'big') + data)

        length = int.from_bytes(s.recv(4), 'big')
        audio_data = s.recv(length)

        with open("output.wav", "wb") as f:
            f.write(audio_data)

    audio_utils.play_audio("output.wav")

if __name__ == "__main__":
    send_audio()