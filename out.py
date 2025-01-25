"""OUT unsorts all the files that have been sorted on folders"""

import os

def main() -> None:
    """Execute unsorting functionality for all the
    files that have been sorted by the IN file"""
    unsorts_all_files()


def unsorts_all_files() -> None:
    """Remove all the folders and move the files to the root directory"""
    folders_list = os.listdir()
    for folder in folders_list:
        if folder.split(".")[-1] in ["gitattributes", "git", "gitignore", "py"]:
            continue
        for file in os.listdir(folder):
            os.rename(f"{folder}\\{file}", file)
        os.rmdir(folder)

if __name__ == "__main__":
    main()
