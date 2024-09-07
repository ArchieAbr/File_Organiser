# Script to organise files based on their file extensions
import sys
import os
import shutil
import argparse
from tqdm import tqdm

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

# Dictionary to keep track of the count of each file type
file_count = {ext: 0 for exts in file_extensions.values() for ext in exts}

# Give the user a choice to organise the files or exit the program
print("Choose an option: ")
print("1. Organise files")
print("2. Exit")
choice = int(input())

if choice == 1:
    # Iterate over the directory with a progress bar
    for file in tqdm(os.listdir(directory), desc="Organising files", unit="file"):
        # Iterate over the file extensions
        for category, extensions in file_extensions.items():
            # Check if the file extension is in the list of extensions
            for extension in extensions:
                if file.endswith(extension):
                    # Create a new directory if it doesn't exist
                    if not os.path.exists(directory + "/" + category):
                        os.mkdir(directory + "/" + category)
                    # Move the file to the respective directory
                    shutil.move(directory + "/" + file, directory + "/" + category + "/" + file)
                    file_count[extension] += 1
                    break
    print("Files have been organised")
    for ext, count in file_count.items():
        if count > 0:
            print(f"{count} {ext} files moved")
    sys.exit("Exiting the program")
else:
    sys.exit("Exiting the program")
