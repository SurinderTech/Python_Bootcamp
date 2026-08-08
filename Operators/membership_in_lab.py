models = [
    "gpt-4.1",
    "gpt-5.5",
    "claude"
]

print("gpt-5.5" in models)
print("llama" in models)

filename = "growthos.py"

print(".py" in filename)
print(".js" in filename)

config = {
    "model": "gpt-5.5",
    "temperature": 0.7
}

print("model" in config)
print("temperature" in config)

print("gpt-5.5" in config)
print(0.7 in config)