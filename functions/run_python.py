import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    abs_path = os.path.abspath(working_directory)
    target_file_path = os.path.join(abs_path, file_path)
    directory_part = os.path.exists(target_file_path)

    if not os.path.abspath(target_file_path).startswith(abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not directory_part:
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python", file_path] + args,
            cwd=abs_path,
            capture_output=True,
            text=True,
            timeout=30,
        )
        out = result.stdout
        err = result.stderr
        rtcode = result.returncode
        output_parts = []

        if out:
            output_parts.append(f"STDOUT:\n{result.stdout}\n")

        if err:
            output_parts.append(f"STDERR:\n{result.stderr}\n")

        if rtcode != 0:
            output_parts.append(f"Process exited with code {rtcode}")

        if not output_parts:
            return "No output produced."

        return "\n".join(output_parts)
    except Exception as e:
        return f"Error: executing Python file: {e}"
