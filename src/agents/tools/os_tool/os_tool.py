"""This module provides tools for interacting with the os."""

import os

def list_directory(path: str = ".") -> str:
    """Lists files and directories in the specified path. Defaults to the current directory.

    Args:
        path: The path to the directory to list. Defaults to ".".

    Returns:
        A string containing the list of files and directories, or an error message.
    """
    try:
        entries = os.listdir(path)
        if not entries:
            return f"Directory '{path}' is empty."
        return "Contents of directory '{}':\n{}".format(path, "\n".join(entries))
    except FileNotFoundError:
        return f"Error: Directory '{path}' not found."
    except PermissionError:
        return f"Error: Permission denied to access directory '{path}'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def read_file(path: str) -> str:
    """Reads the content of the specified file.

    Args:
        path: The path to the file to read.

    Returns:
        A string containing the content of the file, or an error message.
    """
    try:
        with open(path, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{path}' not found."
    except IsADirectoryError:
        return f"Error: '{path}' is a directory, not a file."
    except PermissionError:
        return f"Error: Permission denied to read file '{path}'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def path_exists(path: str) -> bool:
    """Checks if a file or directory exists at the specified path.

    Args:
        path: The path to check.

    Returns:
        True if the path exists, False otherwise.
    """
    return os.path.exists(path)

def get_current_working_directory() -> str:
    """Returns the current working directory.

    Returns:
        A string representing the current working directory.
    """
    return os.getcwd()
