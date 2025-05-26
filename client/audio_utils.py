import sounddevice as sd
import soundfile as sf

def record_audio(filename="input.wav", duration=5, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write(filename, audio, fs)
    print("Recording saved.")

def play_audio(filename="output.wav"):
    data, fs = sf.read(filename)
    sd.play(data, fs)
    sd.wait()
