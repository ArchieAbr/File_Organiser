# Script to organise files based on their file extensions
import sys
import os
import shutil
import argparse
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog, messagebox

# Directory to organise
parser = argparse.ArgumentParser(description="Organise files based on their file extensions")
parser.add_argument("directory", help="Directory to organise")
args = parser.parse_args()

# Directory to organise
directory = args.directory
# List of file extensions and their respective directories
file_extensions = {
    "images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
               ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx"],
    "archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "plain_text": [".txt", ".in", ".out"],
    "pdf": [".pdf"],
    "iso": [".iso"],
    "powerpoint": [".pptx", ".ppt"],
    "spreadsheet": [".csv", ".xls", ".xlsx"]
}

# Function to organize files
def organize_files(directory):
    file_count = {ext: 0 for exts in file_extensions.values() for ext in exts}

    # Iterate over the directory with a progress bar
    for file in tqdm(os.listdir(directory), desc="Organizing files", unit="file"):
        # Iterate over the file extensions
        for category, extensions in file_extensions.items():
            # Check if the file extension is in the list of extensions
            for extension in extensions:
                if file.endswith(extension):
                    # Create a new directory if it doesn't exist
                    if not os.path.exists(os.path.join(directory, category)):
                        os.mkdir(os.path.join(directory, category))
                    # Move the file to the respective directory
                    shutil.move(os.path.join(directory, file), os.path.join(directory, category, file))
                    file_count[extension] += 1
                    break
        # Show a message box with the results
        result_message = "Files have been organized:\n"
        for ext, count in file_count.items():
            if count > 0:
                result_message += f"{count} {ext} files moved\n"

        messagebox.showinfo("Organize Files", result_message)

# Function for directory selection
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)

# GUI
root = tk.Tk()
root.title("File Organizer")

# Select Directory Button
select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack(pady=20)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()