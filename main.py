import torch
import pyttsx3
import speech_recognition as sr
from transformers import AutoModelForCausalLM, AutoTokenizer
import tkinter as tk
from threading import Thread

# === Monkeypatch for torch.get_default_device (for compatibility with Transformers) ===
if not hasattr(torch, "get_default_device"):
    def get_default_device():
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    torch.get_default_device = get_default_device

# === Setup ===
model_id = "gpt2"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# === Load Tokenizer and Model ===
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_id)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32).to(device)
print("Model loaded successfully.")

# === Initialize TTS engine ===
engine = pyttsx3.init()

# === Initialize Speech Recognizer ===
recognizer = sr.Recognizer()
mic = sr.Microphone()

# === Functions ===
def speak(text):
    text_output.insert(tk.END, f"Bot: {text}\n")
    text_output.see(tk.END)
    engine.say(text)
    engine.runAndWait()

def listen():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        text_output.insert(tk.END, "Listening...\n")
        text_output.see(tk.END)
        try:
            audio = recognizer.listen(source, timeout=5)
            text_output.insert(tk.END, "Recognizing...\n")
            query = recognizer.recognize_google(audio)
            text_output.insert(tk.END, f"You: {query}\n")
            text_output.see(tk.END)
            return query
        except sr.WaitTimeoutError:
            text_output.insert(tk.END, "Timeout. Please speak again.\n")
        except sr.UnknownValueError:
            text_output.insert(tk.END, "Sorry, I didn't catch that.\n")
        except sr.RequestError:
            text_output.insert(tk.END, "Speech Recognition API unavailable.\n")
        return None

def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    output = model.generate(input_ids, max_length=100, do_sample=True, top_p=0.95, top_k=60)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response[len(prompt):].strip()

def start_voice_thread():
    thread = Thread(target=voice_interaction)
    thread.start()

def voice_interaction():
    user_input = listen()
    if user_input:
        if user_input.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            root.quit()
        else:
            reply = generate_response(user_input)
            speak(reply)

# === GUI ===
root = tk.Tk()
root.title("AI Voice Bot")
root.geometry("500x400")

text_output = tk.Text(root, wrap=tk.WORD)
text_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

start_button = tk.Button(root, text="🎤 Start Talking", command=start_voice_thread)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="❌ Exit", command=root.quit)
stop_button.pack(pady=5)

speak("Hello! Click the button and talk to me.")
root.mainloop()













# import torch
# import pyttsx3
# import speech_recognition as sr
# from transformers import AutoModelForCausalLM, AutoTokenizer

# # === Monkeypatch for torch.get_default_device (for compatibility with Transformers) ===
# if not hasattr(torch, "get_default_device"):
#     def get_default_device():
#         return torch.device("cuda" if torch.cuda.is_available() else "cpu")
#     torch.get_default_device = get_default_device

# # === Setup ===
# model_id = "gpt2"
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# print(f"Using device: {device}")

# # === Load Tokenizer and Model ===
# print("Loading tokenizer...")
# tokenizer = AutoTokenizer.from_pretrained(model_id)

# print("Loading model...")
# model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32).to(device)
# print("Model loaded successfully.")

# # === Initialize TTS engine ===
# engine = pyttsx3.init()

# # === Initialize Speech Recognizer ===
# recognizer = sr.Recognizer()
# mic = sr.Microphone()

# def speak(text):
#     print(f"Bot: {text}")
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     with mic as source:
#         recognizer.adjust_for_ambient_noise(source)
#         print("Listening...")
#         try:
#             audio = recognizer.listen(source, timeout=5)
#             print("Recognizing...")
#             query = recognizer.recognize_google(audio)
#             print(f"You: {query}")
#             return query
#         except sr.WaitTimeoutError:
#             print("Timeout. Please speak again.")
#         except sr.UnknownValueError:
#             print("Sorry, I didn't catch that.")
#         except sr.RequestError:
#             print("Speech Recognition API unavailable.")
#         return None

# def generate_response(prompt):
#     input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
#     output = model.generate(input_ids, max_length=100, do_sample=True, top_p=0.95, top_k=60)
#     response = tokenizer.decode(output[0], skip_special_tokens=True)
#     return response[len(prompt):].strip()

# # === Main Loop ===
# speak("Hello! How can I help you today?")
# while True:
#     user_input = listen()
#     if user_input:
#         if user_input.lower() in ["exit", "quit", "stop"]:
#             speak("Goodbye!")
#             break
#         reply = generate_response(user_input)
#         speak(reply)
