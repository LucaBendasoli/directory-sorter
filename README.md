
# Directory Sorter

Directory Sorter is a Python project that helps you organize and manage files on your desktop by sorting them into folders based on their file extensions. It also provides functionality to unsort the files, moving them back to the root directory.
This project was sugested by the Python Basics module of an AI and ML course I'm taking, the goal was to practice the OS built-in library functionalities that Python provides.

## Project Structure

- `in.py`: Contains sorting functionality.
- `out.py`: Contains unsorting functionality.
- `.files`: Files that are going to be sorted/unsorted.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/LucaBendasoli/directory-sorter.git
    ```
2. Navigate to the project directory:
    ```sh
    cd directory-sorter
    ```
    
## Features

- **Sort Files**: Sorts files into folders based on their extensions.
- **Unsort Files**: Moves files back to the root directory and removes the created folders.
- **Ignore Specific Files**: Ignores files with extensions 'py', 'git', 'gitattributes', and 'gitignore'.

## Usage

### Sorting Files

To sort files into folders based on their extensions, run the `in.py` script:

```sh
python in.py
```

### Unsorting Files

To move files back to the root directory and remove the created folders, run the `out.py` script:

```sh
python out.py
```

## Contribution

1. Fork the project.
2. Create a new branch: `git checkout -b my-new-feature`
3. Make your changes and commit: `git commit -m 'feat: add new functionality'`
4. Push to the remote repository: `git push origin my-new-feature`
5. Open a pull request.
