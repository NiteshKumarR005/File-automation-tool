import os
import shutil

def rename_files(folder_path):
    files = os.listdir(folder_path)
    count = 1
    
    for file in files:
        old_path = os.path.join(folder_path, file)
        
        if os.path.isfile(old_path):
            extension = os.path.splitext(file)[1]
            
            new_name = "file_" + str(count) + extension
            new_path = os.path.join(folder_path, new_name)
            
            os.rename(old_path, new_path)
            print(f"{file} -> {new_name}")
            
            count += 1
    print("\nFile renamed successfully!") 


def sort_files(folder_path):
    image_folder = "Images"
    document_folder = "Documents"
        
    files = os.listdir(folder_path)
    for file in files:
        full_path = os.path.join(folder_path, file)
        extension = os.path.splitext(file)[1]
        
        if extension == ".png":
            if not os.path.exists(image_folder):
                os.mkdir(image_folder)
            else:
                print("Folder already exists.")
            shutil.move(full_path, image_folder)
            print(f"{file} moved to {image_folder}")
        elif extension == ".txt":
            if not os.path.exists(document_folder):
                os.mkdir(document_folder)
            else:
                print("Folder already exists.")
            shutil.move(full_path, document_folder)
            print(f"{file} moved to {document_folder}")
        else:
            print("File type not supported.")


print("----- File Automation Tool -----")
print("1. Rename Files")
print("2. Sort Files")
print("3. Clean Files")

try:
    choice = input("Enter your choice: ")
    print("You selected: ", choice)


    if choice == "1":
        folder_path = input("Enter folder name: ")
        rename_files(folder_path)
    
    elif choice == "2":
        folder_path = input("Enter folder name: ")
        sort_files(folder_path)

    else:
        print("Invalid choice.")
                
                
except FileNotFoundError:
    print("Folder not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("Error: ", e)
