"""Directory Sorter is a code that will sort every file in you 
desktop into different folders categorized by their extensions."""

# Author: Luca Bendasoli

import os

extensions = []
main_folder = False 

os.chdir(os.getcwd())
for f in os.listdir():
    if f.split(".")[-1] == "py":
        continue
    if f not in extensions:
        extensions.append(f.split(".")[-1])
        os.mkdir(f.split(".")[-1])
    os.rename(f, f"{f.split(".")[-1]}\\{f}")