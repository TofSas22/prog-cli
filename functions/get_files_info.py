import os


def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        dir_list = os.listdir(target_dir)
        dir_content = []
        for content in dir_list:
            dir_content.append(
                f"- {content}: file_size={os.path.getsize(os.path.join(target_dir, content))}, is_dir={os.path.isdir(os.path.join(target_dir, content))}"
            )
        result = "\n".join(dir_content)
        return result
    except Exception as e:
        return f"Error: {e}"
