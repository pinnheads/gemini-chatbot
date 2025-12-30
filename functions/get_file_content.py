import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):

    # get absolute path of the working directory
    working_directory_abs = os.path.abspath(working_directory)

    # Construct full path to the target file
    # normalize path name to replace aliases
    target_file = os.path.normpath(
        os.path.join(working_directory_abs, file_path)
    )

    # Check if the target file falls within the absolute path
    valid_target_dir = os.path.commonpath(
        [working_directory_abs, target_file]) == working_directory_abs
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # check if directory is a valid directory
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        content = ""
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            content += file_content_string
            if f.read(1):
                content += f'[...File "{file_path} truncated at {MAX_CHARS} characters"]'
        return content
    except Exception as e:
        return f"Error: {e}"
