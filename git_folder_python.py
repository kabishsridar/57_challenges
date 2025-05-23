import os # importing os module for path function and makedirs
import shutil # importing shutil module to move the file to dedicated path

# Define the files to move
files1 = ["ex_9_ch1.py", "ex_9_ch1_notes.txt"]
files2 = ["ex_10_ch_notes.txt", "ex_10_ch.py", "ex_10.py", "ex_10_notes.txt"]
lst = [files1, files2]
# Define the target folder
target_folder1 = "ex_9_folder"
target_folder2 = "ex_10_folder"
# Create the target folder if it doesn't exist
os.makedirs(target_folder1, exist_ok=True)
os.makedirs(target_folder2, exist_ok=True)
# Move each file to the target folder

for filename in lst:
    for file in filename:
        if os.path.exists(file):
            if file.startswith("ex_9"):
                shutil.move(file, os.path.join(target_folder1, file))
            elif file.startswith("ex_10"):
                shutil.move(file, os.path.join(target_folder2, file))
            print(f"Moved {file} to {target_folder1}/")
        else:
            print(f"File not found: {file} ")