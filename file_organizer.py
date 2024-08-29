import os
import shutil

# Define the main folder where the files are located
source_folder = r"C:\Users\Anisha\Downloads"  # Change this to your folder path

# Define the destination folders for each file type
destinations = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg','.jfif'],
    "Documents": ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.csv'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv','.webm'],
    "Music": ['.mp3', '.wav', '.aac', '.flac'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz'],
    "Scripts": ['.py', '.js', '.html', '.css','.sql','.htm','.php','.ds'],
    "Exe": ['.exe'],
    "Others": []  # For files that don't match any above
}

def create_folders(base_folder):
    for folder_name in destinations.keys():
        folder_path = os.path.join(base_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files(source):
    for filename in os.listdir(source):
        if os.path.isdir(os.path.join(source, filename)):
            continue

        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        for folder_name, extensions in destinations.items():
            if file_extension in extensions:
                shutil.move(os.path.join(source, filename), os.path.join(source_folder, folder_name, filename))
                moved = True
                break

        if not moved:
            shutil.move(os.path.join(source, filename), os.path.join(source_folder, "Others", filename))

def refine_others_folder():
    others_folder = os.path.join(source_folder, "Others")
    move_files(others_folder)

if __name__ == "__main__":
    create_folders(source_folder)
    move_files(source_folder)
    refine_others_folder()  # Re-filter the "Others" folder
    print("Files have been organized and re-filtered successfully!")
