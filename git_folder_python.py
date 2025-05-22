import os # importing os module for path function and makedirs
import shutil # importing shutil module to move the file to dedicated path

# Define the files to move
files1 = ["ex_8_notes.txt", "ex_8.py", "ex_8_ch1.py","ex_8_ch1_notes.txt", "ex_8_ch2.py", "ex_8_ch", "ex_8_ch2_notes.txt", ""]

# Define the target folder
target_folder2 = "ex_8_folder"
# Create the target folder if it doesn't exist
os.makedirs(target_folder2, exist_ok=True)
# Move each file to the target folder

for file in files1:
    if os.path.exists(file):
        shutil.move(file, os.path.join(target_folder2, file))
        print(f"Moved {file} to {target_folder2}/")
    else:
        print(f"File not found: {file} ")
