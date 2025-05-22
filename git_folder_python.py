import os
import shutil

# Define the files to move
files_to_move = ["ex_4.py", "ex_4_notes.txt"]

# Define the target folder
target_folder = "ex_4_folder"

# Create the target folder if it doesn't exist
os.makedirs(target_folder, exist_ok=True)

# Move each file to the target folder
for file in files_to_move:
    if os.path.exists(file):
        shutil.move(file, os.path.join(target_folder, file))
        print(f"Moved {file} to {target_folder}/")
    else:
        print(f"File not found: {file} ")