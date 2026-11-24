import os

LINE = "Thank you for your email. I am drowning. Please stop watering me. I will reply as soon as I can breathe again."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod("/output/entry.txt", 0o644)
