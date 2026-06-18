import os
import shutil
import logging


# Configure logging
logging.basicConfig(filename="operations.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")


# Function to rename files in a folder
def rename_files(folder_name):
    files = os.listdir(folder_name)
    count = 1
    
    for file in files:
        old_path = os.path.join(folder_name, file)
        
        if os.path.isfile(old_path):
            extension = os.path.splitext(file)[1]
            
            new_name = "file_" + str(count) + extension
            new_path = os.path.join(folder_name, new_name)
            
            os.replace(old_path, new_path)
            print(f"{file} -> {new_name}")
            
            count += 1
            logging.info(f"Renamed {file} to {new_name}")
    print("\nFile renamed successfully!") 


# Function to sort files in a folder
def sort_files(folder_name):
    image_extensions = [".png", ".jpg", ".jpeg"]
    document_extensions = [".txt", ".pdf", ".docx"]
    video_extensions = [".mp4", ".mkv"]
    
    image_folder = "Images"
    document_folder = "Documents"
    video_folder = "Videos"

    files = os.listdir(folder_name)
    
    for file in files:
        full_path = os.path.join(folder_name, file)
        extension = os.path.splitext(file)[1]
        
        if extension in image_extensions:       # Extension check
            if not os.path.exists(image_folder):
                os.mkdir(image_folder)
                logging.info(f"Created folder: {image_folder}")
                
            else:
                print("Folder already exists.")
            shutil.move(full_path, image_folder)    # Move file to folder
            logging.info(f"Moved {file} to {image_folder}")
            print(f"{file} moved to {image_folder}")
            
        elif extension in document_extensions:  # Extension check
            if not os.path.exists(document_folder):
                os.mkdir(document_folder)
                logging.info(f"Created folder: {document_folder}")
                
            else:
                print("Folder already exists.")
            shutil.move(full_path, document_folder)    # Move file to folder
            logging.info(f"Moved {file} to {document_folder}")
            print(f"{file} moved to {document_folder}")
            
        elif extension in video_extensions:     # Extension check
            if not os.path.exists(video_folder):
                os.mkdir(video_folder)
                logging.info(f"Created folder: {video_folder}")
                
            else:
                print("Folder already exists.")
            shutil.move(full_path, video_folder)    # Move file to folder
            logging.info(f"Moved {file} to {video_folder}")
            print(f"{file} moved to {video_folder}")
            
        else:
            print("File type not supported.")
    print("\nFiles sorted successfully!")


# Function to clean up files in a folder
def cleanup_files(folder_name):
    cleanup_extensions = [".tmp", ".bak"]
    
    files = os.listdir(folder_name)
    
    for file in files:
        full_path = os.path.join(folder_name, file)
        extensions = os.path.splitext(file)[1]
        
        if extensions in cleanup_extensions:    # Extension check
            os.remove(full_path)
            print(file + " deleted.")
            logging.info(f"Deleted {file}")
        else:
            logging.info(f"No cleanup needed for: {folder_name}")
            print("File not necessary for cleanup.")
    print("\nCleanup completed successfully!")


# Function to display the menu options
def display():
    print("----- File Automation Tool -----")
    print("1. Rename Files")
    print("2. Sort Files")
    print("3. Clean Files")

# Main program execution
try:
    display()       # Display menu options
    choice = input("Enter your choice: ")
    print("You selected: ", choice)
    
    if choice == "1":
        folder_name = input("Enter folder name: ")
        if not os.listdir(folder_name) == []:       # Folder check
            rename_files(folder_name)
        else:
            print("Folder is empty.")
    
    elif choice == "2":
        folder_name = input("Enter folder name: ")
        if not os.listdir(folder_name) == []:       # Folder check
            sort_files(folder_name)
        else:
            print("Folder is empty.")

    elif choice == "3":
        folder_name = input("Enter folder name: ")
        if not os.listdir(folder_name) == []:       # Folder check
            cleanup_files(folder_name)
        else:
            print("Folder is empty.")
    
    else:
        print("Invalid choice.")
                

# Exception handling for file operations                
except FileNotFoundError:
    print("Folder not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("Error: ", e)
