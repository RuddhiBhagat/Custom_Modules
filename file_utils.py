# file_utils.py

def read_file(file_path):
    """
    Reads the content of a file and returns it.
    """
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """
    Writes the given content to a file, overwriting any existing content.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def append_to_file(file_path, content):
    """
    Appends the given content to the file.
    """
    with open(file_path, 'a') as file:
        file.write(content)
