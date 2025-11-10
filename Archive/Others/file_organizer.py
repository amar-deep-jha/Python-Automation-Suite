# File organizer script
import os, shutil, json

# Load configuration
with open("config.json") as f:
    config = json.load(f)
src = config["paths"]["downloads"]
dst = config["paths"]["target_archive"]

print("Loaded config:", config)

# Ensure destination folder exists
os.makedirs(dst, exist_ok=True)

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"],
    "Others": []
}

# Create subfolders
for folder in file_types.keys():
    os.makedirs(os.path.join(dst, folder), exist_ok=True)

# Organize files
for file in os.listdir(src):
    path = os.path.join(src, file)
    if os.path.isfile(path):
        moved = False
        for folder, exts in file_types.items():
            if any(file.lower().endswith(ext) for ext in exts):
                shutil.move(path, os.path.join(dst, folder, file))
                print(f"Moved: {file} → {folder}")
                moved = True
                break
        if not moved:
            shutil.move(path, os.path.join(dst, "Others", file))
            print(f"Moved: {file} → Others")

print("\n✅ File organization complete!")
