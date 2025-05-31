# requirement: user will give exercise name, example ex_1, the files having this name must be moved to the folder
# with the name ex_1
# get the folder name as an input and store as target folder
# assign files1, files2, etc as the file names
# make those as a list
# define a function named move_folder
# use the input given by the user and search for the files starting with the target folder
# if the target folder already exists, add the file to the respective folder, else create a new folder and add the files to it.
# use os module to find whether the file exists or not
# move the file to respective folder using shutil

import os # importing os module for path function and makedirs
import shutil # importing shutil module to move the file to dedicated path

#target_folder = input("Enter the folder name: ")



# print(os.listdir("."))

# Move each file to the target folder
# dict1 = {"name":"os", "functions": []}
# print(f"list names: {list_filenames}")

def move_file_to_folder(foldername):
    list_filenames = os.listdir(".") # it will include also the folders
    os.mkdir(foldername)
    for fname in list_filenames:
        if os.path.isfile(fname):
            if fname.startswith(foldername):
                # print(f"the file name is {fname} and folder is {foldername}")
                shutil.move(fname, os.path.join(foldername, fname))
                print(f"Moved {fname} to {foldername}/")
        else:
            print(f"{fname} is a folder , not moving")

# move_file_to_folder("ex_18")

if __name__ == "__main__":
    for folder in range(4):
        foldername = f"ex_{folder+43}"
        print(foldername)
        move_file_to_folder(foldername)