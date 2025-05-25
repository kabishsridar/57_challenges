import os # importing os module for path function and makedirs
import shutil # importing shutil module to move the file to dedicated path

# requirement: user will give exercise name, example ex_1, the files having this name must be moved to the folder
# with the name ex_1

# Define the files to move
files1 = ["ex_15_ch.py", "ex_15_ch_notes.txt","ex_15_notes.txt", "ex_15.py"]
files2 = ["ex_16_ch_notes.txt", "ex_16_ch.py", "ex_16.py", "ex_16_notes.txt"]
lst = [files1, files2]
# Define the target folder
target_folder1 = "ex_15_folder"
target_folder2 = "ex_16_folder"
# Create the target folder if it doesn't exist
os.makedirs(target_folder1, exist_ok=True)
os.makedirs(target_folder2, exist_ok=True)
# Move each file to the target folder

for filename in lst:
    for file in filename:
        if os.path.exists(file):
            if file.startswith("ex_15"):
                shutil.move(file, os.path.join(target_folder1, file))
            elif file.startswith("ex_16"):
                shutil.move(file, os.path.join(target_folder2, file))
            print(f"Moved {file} to {target_folder1}/")
        else:
            print(f"File not found: {file} ")