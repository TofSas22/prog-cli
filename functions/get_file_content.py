import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.join(abs_path, file_path)

    if not target_dir.startswith(abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            next_char = f.read(1)
            if next_char:
                file_content_string += f"[...File '{file_path}' truncated at 10000 characters]"
    
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
