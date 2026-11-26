import os

LINE = "Every time you type 'gas', I pretend I was ready all along. Really, I'd been staring at the wall for an hour, waiting for those three letters."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
