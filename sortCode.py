import os

file_type_dict = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"]
}

test_path = "E:/My Personal Folder-Jeremy Ducon"

extra_text = " Files"

def get_file_type(extension):
    for file_type, extensions in file_type_dict.items():
        if extension.lower() in extensions:
            return file_type
    return "Other"

def create_folders(path):
    for f in os.listdir(path): # i think its common to use f cuz it stands for file or folder
        if os.path.isfile(os.path.join(path, f)):
            root, ext = os.path.splitext(f) #root is the name of the file, ext is the extension (like png or txt)
            file_type = get_file_type(ext)
            
            parent_path = os.path.join(path, file_type, ext.upper()[1:] + extra_text)

            if os.path.isdir(parent_path):
                print("Existing group")
            else:
                os.makedirs(parent_path) #this makes a new folder with the name of the extension
                print("New group created")
            
            os.rename(os.path.join(path, f), os.path.join(parent_path, f)) #this moves the file to the new folder

def sort_file(path):
    create_folders(path)

sort_file(test_path)