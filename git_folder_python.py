import os # importing os module for path function and makedirs
import shutil # importing shutil module to move the file to dedicated path

# Define the files to move
files1 = ["ex_13_ch1.py", "ex_13_ch2.py", "ex_13_ch2_notes.txt","ex_13_notes.txt", "ex_13.py"]
files2 = ["ex_14_ch_notes.txt", "ex_14_ch.py", "ex_14.py", "ex_14_notes.txt"]
lst = [files1, files2]
# Define the target folder
target_folder1 = "ex_13_folder"
target_folder2 = "ex_14_folder"
# Create the target folder if it doesn't exist
os.makedirs(target_folder1, exist_ok=True)
os.makedirs(target_folder2, exist_ok=True)
# Move each file to the target folder

for filename in lst:
    for file in filename:
        if os.path.exists(file):
            if file.startswith("ex_13"):
                shutil.move(file, os.path.join(target_folder1, file))
            elif file.startswith("ex_14"):
                shutil.move(file, os.path.join(target_folder2, file))
            print(f"Moved {file} to {target_folder1}/")
        else:
            print(f"File not found: {file} ")