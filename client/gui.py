# from client_core import send_audio
# import tkinter as tk

# def run_bot():
#     send_audio()

# root = tk.Tk()
# root.title("AI Voice Bot")

# btn = tk.Button(root, text="Talk to Bot", command=run_bot, padx=20, pady=10)
# btn.pack(pady=20)

# root.mainloop()



import tkinter as tk
from client_core import send_audio

def run_bot():
    response = send_audio()
    result_label.config(text="Bot: " + response)

root = tk.Tk()
root.title("AI Voice Bot")

record_button = tk.Button(root, text="Talk to Bot", command=run_bot)
record_button.pack(pady=20)

result_label = tk.Label(root, text="", wraplength=300, justify="left")
result_label.pack(padx=10, pady=10)

root.mainloop()

