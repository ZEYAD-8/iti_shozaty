import os

def change_file_extensions(folder_path, old_ext, new_ext):
    if not os.path.isdir(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    for filename in os.listdir(folder_path):
        if filename.endswith(old_ext):
            new_filename = filename.rsplit('.', 1)[0] + new_ext
            
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)

            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    
    folder_path = "shoe_images/" 
    old_ext = ".jpeg"   
    new_ext = ".png"   

    change_file_extensions(folder_path, old_ext, new_ext)
