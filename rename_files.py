# Program to rename files

# Import os
import os
# Import tkinter
from tkinter import *
from tkinter import filedialog

# Set up the main application window
root = Tk()
# Hide the main window
root.withdraw()


# Get path to the old file
old_file_path = filedialog.askopenfilename(
    title="Select a file to rename",
    filetypes=(("Text Files","*.txt"),("All Files","*.*"))
)
# Get old file name
old_file_name = os.path.basename(old_file_path)

print("Old file path: ", old_file_path)
print("Old file name: ", old_file_name)


# Set path to the new file
new_file_path = filedialog.asksaveasfilename(
    title="Save me...",
    filetypes=(("Text Files","*.txt"),("All Files","*.*"))
)
# Get new file name
new_file_name = os.path.basename(new_file_path)

print("New file path: ", new_file_path)
print("New file name: ", new_file_name)


# Rename file
os.rename(old_file_path,new_file_path)
