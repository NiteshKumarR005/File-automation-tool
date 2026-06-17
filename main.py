import os

print("----- File Automation Tool -----")
print("1. Rename Files")
print("2. Sort Files")
print("3. Clean Files")

choice = input("Enter your choice: ")
print("You selected: ", choice)

if choice == "1":
    folder_path = input("Enter folder name: ")
    try:
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

    except FileNotFoundError:
        print("Folder not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("Error: ", e)

else:
    print("Invalid choice.")
