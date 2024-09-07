# Script to organise files based on their file extensions
import sys
import os
import shutil
import customtkinter as ctk

# List of file extensions and their respective directories
file_extensions = {
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
               ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Plain_Text": [".txt", ".in", ".out"],
    "pdf": [".pdf"],
    "iso": [".iso"],
    "PowerPoint": [".pptx", ".ppt"],
    "Spreadsheet": [".csv", ".xls", ".xlsx"]
}

# Function to organize files
def organize_files(directory, result_label):
    file_count = {ext: 0 for exts in file_extensions.values() for ext in exts}

    # Iterate over the directory to organize files
    for file in os.listdir(directory):
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

    # Prepare the result message
    result_message = "Files have been organized:\n"
    for ext, count in file_count.items():
        if count > 0:
            result_message += f"{count} {ext} files moved\n"

    # Update the label with the result message
    result_label.configure(text=result_message)

# GUI class using customtkinter
class FileOrganizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("File Organizer")
        self.geometry("500x400")

        # Set the appearance mode ("System", "Dark", "Light")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Create and configure widgets
        self.directory_entry = ctk.CTkEntry(self, width=300, font=("Arial", 14))
        self.directory_entry.pack(pady=20)

        self.browse_button = ctk.CTkButton(
            self, text="Browse", command=self.browse_directory, width=100, height=30, font=("Arial", 12)
        )
        self.browse_button.pack(pady=10)

        self.select_button = ctk.CTkButton(
            self, text="Organize Files", command=self.organize_files_button, width=200, height=50, font=("Arial", 16)
        )
        self.select_button.pack(pady=20)

        self.exit_button = ctk.CTkButton(
            self, text="Exit", command=self.quit, width=200, height=50, font=("Arial", 16),
            fg_color="gray", hover_color="red"
        )
        self.exit_button.pack(pady=10)

        # Label to display results
        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14), wraplength=350)
        self.result_label.pack(pady=20)

    def browse_directory(self):
        # Open a native file dialog to choose a directory
        directory = ctk.filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, ctk.END)  # Clear the entry
            self.directory_entry.insert(0, directory)  # Insert selected path

    def organize_files_button(self):
        directory = self.directory_entry.get()
        if os.path.isdir(directory):  # Check if the directory is valid
            organize_files(directory, self.result_label)
        else:
            self.result_label.configure(text="Please enter a valid directory path!")

# Main function to run the application
if __name__ == "__main__":
    app = FileOrganizerApp()
    app.mainloop()


