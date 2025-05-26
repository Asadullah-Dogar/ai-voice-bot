# server/inference_utils.py

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "gpt2"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model():
    print("[Inference] Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    print("[Inference] Loading model...")
    model = AutoModelForCausalLM.from_pretrained(model_id).to(device)
    print("[Inference] Model loaded successfully.")
    return tokenizer, model

def generate_response(prompt, tokenizer, model):
    print(f"[Inference] Generating response for prompt: {prompt}")
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_length=100, do_sample=True, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response



from server.inference_utils import load_model, generate_response
print(load_model)
print(generate_response)
