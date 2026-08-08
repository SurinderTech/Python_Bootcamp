models = [
    "gpt-4.1",
    "gpt-5.5",
    "claude"
]

print("llama" not in models)
print("claude" not in models)

filename = "growthos.py"

print(".js" not in filename)
print(".py" not in filename)

config = {
    "model": "gpt-5.5",
    "temperature": 0.7
}

print("memory" not in config)
print("model" not in config)

print(0.7 not in config)
print("gpt-5.5" not in config)