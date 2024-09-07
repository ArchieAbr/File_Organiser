# script to generate 10 random numbers and write them to a file
# Script will create 100 csv, txt, docx, and pdf files with random numbers
import random
import os
import shutil

# Directory to write the files
directory = "test_data"
# List of file extensions
file_extensions = {
    "csv": ".csv",
    "txt": ".txt",
    "docx": ".docx",
    "pdf": ".pdf"
}

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.mkdir(directory)

# Generate 10 random numbers and write them to a file
def generate_random_numbers(file, count):
    with open(file, "w") as f:
        for _ in range(count):
            f.write(str(random.randint(1, 100)) + "\n")

# Generate 100 files with random numbers
for i in range(1, 101):
    for category, extension in file_extensions.items():
        file = f"{directory}/{category}_{i}{extension}"
        generate_random_numbers(file, 10)

print("Files have been generated")


