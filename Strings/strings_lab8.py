model = "gpt-5.5"
temperature = 0.73482
accuracy = 0.94731
tokens = 1250340


message = f"""Model: {model}
temperature:{temperature:.2f}
Accuracy:{accuracy:.2%}
Tokens:{tokens:,}
"""
print(message)