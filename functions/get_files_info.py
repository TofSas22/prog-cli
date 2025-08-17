import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    target_abs = os.path.abspath(full_path)
    working_dir_abs = os.path.abspath(working_directory)
    is_dir = os.path.isdir(full_path)

    if not target_abs.startswith(working_dir_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'        
    if not is_dir:
        return f'Error: "{directory}" is not a directory'

    result = f'- {directory}: file_size={os.path.getsize(full_path)} bytes, is_dir={is_dir}'

