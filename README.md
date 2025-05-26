# 🤖 AI Voice Bot

A real-time **AI Voice Bot** that supports:

- 📧 **Client-Server Architecture** — for modular, networked speech interaction
- 🖥️ **Standalone Local GUI Bot (`main.py`)** — for offline testing on a single machine

---

## 📁 Project Structure

```text
ai-voice-bot/
│
├── client/
│   ├── client_core.py       # Handles network communication
│   ├── audio_utils.py       # Audio recording and playback
│   ├── gui.py               # GUI for user interaction
│
├── server/
│   ├── server.py            # Receives audio, processes it with STT + LLM + TTS
│   ├── inference_utils.py   # GPT-based response generation
│   ├── tts_utils.py         # Text-to-speech functionality
│
├── main.py                 # Standalone local voice bot with GUI
├── requirements.txt        # Python dependencies
├── .gitignore              # Files/directories to ignore in version control
└── README.md               # Project documentation
```

---

## ⚙️ Prerequisites

- Python 3.8+
- Virtual environment recommended

Install dependencies:

```bash
pip install -r requirements.txt
```
Or manually:

```bash
pip install torch transformers pyttsx3 SpeechRecognition pydub sounddevice soundfile openai-whisper
```

---

## 🧠 About `main.py`

`main.py` is a standalone, fully offline AI voice bot. It features:

- **Speech-to-Text**: Uses `speech_recognition` with Google API
- **Response Generation**: Uses GPT-2 via Hugging Face
- **Text-to-Speech**: Uses `pyttsx3` for local audio output
- **GUI**: Built with `Tkinter`

📌 Ideal for quick testing or demos without launching a server.

---

## 🚀 How to Run

### 1. Run the Server (for client-server mode)
```bash
cd server
python server.py
```
The server loads Whisper STT, your local GPT model, and TTS engine. It listens for audio, processes it, and responds with speech.

### 2. Run the Client
```bash
cd client
python gui.py
```
The client records your voice, sends it to the server, and plays back the response. The GUI displays both your input and the bot's reply.

### 3. Run the Standalone Bot
```bash
python main.py
```
A local GUI window opens. Click "Start Talking," speak, and the bot responds with speech.

✅ No internet or server required.

---

## 📝 Notes

- Ensure microphone and speaker access is enabled
- Start the server before the client in client-server mode
- First-time use may trigger model downloads (Whisper, GPT-2)
- You can tweak timeouts, sample rates, or model settings in the code

---

## 𞷾️ Sample `.gitignore`
```text
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
*.wav
*.mp3
*.ogg
*.flac
output.wav
received.wav
input.wav
```

---

## 📬 Contact
**Asadullah Dogar**  
📧 Email: dogarasad277@gmail.com
