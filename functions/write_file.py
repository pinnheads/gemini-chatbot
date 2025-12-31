import os


def write_file(working_directory, file_path, content):
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
    if os.path.isdir(target_file):
        return f'Error:  Cannot write to "{file_path}" as it is a directory'

    # check if all the directories are created
    os.makedirs(file_path, exist_ok=True)

    try:
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
