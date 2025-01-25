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
    extensions = []

    os.chdir(os.getcwd())
    for f in os.listdir():
        if f.split(".")[-1] in ["py", "git", "gitattributes", "gitignore"]:
            continue
        if f.split(".")[-1] not in extensions:
            extensions.append(f.split(".")[-1])
            os.mkdir(f.split(".")[-1])
        os.rename(f, f"{f.split(".")[-1]}\\{f}")

if __name__ == "__main__":
    main()
