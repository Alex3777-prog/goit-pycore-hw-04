import sys
from pathlib import Path
from colorama import Fore, Style


INDENT = '    '


def display_directory(directory: Path, level: int = 1) -> None:
    """
    Recursively display the contents of a directory as a colored tree.

    Args:
        directory (Path): Path to the directory to explore.
        level (int): Current indentation level. Defaults to 1.
    """
    try:
        for entry in directory.iterdir():
            if entry.is_dir():
                print(f"{INDENT * level}📁 {Fore.BLUE}{entry.name}/{Style.RESET_ALL}")
                display_directory(entry, level + 1)
            else:
                print(f"{INDENT * level}📄 {Fore.GREEN}{entry.name}{Style.RESET_ALL}")
    except OSError as error:
        print(f"Error: {error}")


if len(sys.argv) > 1:
    directory = Path(sys.argv[1])
    if directory.exists() and directory.is_dir():
        print(f"📁 {Fore.BLUE}{directory.resolve().name}/{Style.RESET_ALL}")
        display_directory(directory)
    else:
        print("Error: Directory not found or path is not a directory.")
else:
    print("Error: Please provide a directory path.")