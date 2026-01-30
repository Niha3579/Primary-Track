import os
import shutil

# Source folder (where mixed files exist)
source_folder = "C:/Users/Anjali/Downloads"

# Main destination folder
main_folder = "C:/Users/Anjali/Downloads/Organized_Files"

# Sub folders
folders = {
    "PDFs": [".pdf"],
    "Word_Documents": [".doc", ".docx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"]
}

# Create main folder
os.makedirs(main_folder, exist_ok=True)

# Create subfolders
for folder in folders:
    os.makedirs(os.path.join(main_folder, folder), exist_ok=True)

# Organize files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in folders.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(
                    file_path,
                    os.path.join(main_folder, folder, file)
                )

print("Files organized successfully")