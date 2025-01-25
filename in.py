"""IN is a module that will sort every file in you 
desktop into different folders categorized by their extensions."""

# Author: Luca Bendasoli

import os

def main():
    """Main function that initiates the sorting functionality 
    in the current directory based on their file extensions.
    """
    sort_files()

def sort_files():
    """Sorts all files in the current directory into folders based on their file extensions.
    Files with extensions 'py', 'git', 'gitattributes', and 'gitignore' are ignored.."""
    full_list = os.listdir(os.getcwd())
    files_list = [
        f for f in full_list
        if os.path.isfile(f)
        and ".py" not in f
        and ".gitignore" not in f
        and ".gitattributes" not in f
    ]
    types = list(set([f.split(".")[1] for f in files_list]))
    for file_type in types:
        os.mkdir(file_type)
    for file in files_list:
        from_path = os.path.join(os.getcwd(), file)
        to_path = os.path.join(os.getcwd(), file.split(".")[-1], file)
        os.replace(from_path, to_path)

if __name__ == "__main__":
    main()
