# test_file_utils.py

# Importing functions from the file_utils module
from file_utils import read_file, write_file, append_to_file

# Define the file path
file_path = "example.txt"

# Step 1: Write data to the file
content_to_write = "This is the initial content of the file.\n"
write_file(file_path, content_to_write)

# Step 2: Read and display the file content
print("File content after writing:")
print(read_file(file_path))

# Step 3: Append new data to the file
content_to_append = "This is the new appended content.\n"
append_to_file(file_path, content_to_append)

# Step 4: Read and display the updated content
print("File content after appending:")
print(read_file(file_path))
