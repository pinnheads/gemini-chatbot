import os


def get_files_info(working_directory, directory="."):

    # get absolute path of the working directory
    working_directory_abs = os.path.abspath(working_directory)

    # Construct full path to the target directory
    # normalize path name to replace aliases
    target_dir = os.path.normpath(
        os.path.join(working_directory_abs, directory)
    )

    # Check if the target dir falls within the absoulut path
    valid_target_dir = os.path.commonpath(
        [working_directory_abs, target_dir]) == working_directory_abs
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # check if directory is a valid directory
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    target_dir_contents = os.listdir(target_dir)
    try:
        result = ""
        for entry in target_dir_contents:
            path = os.path.join(target_dir, entry)
            is_dir = os.path.isdir(path)
            file_size = os.path.getsize(
                path) if is_dir is False else get_dir_size(path)
            result += f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}\n"
        return result
    except Exception as e:
        return f"Error: {e}"


def get_dir_size(dir):
    total = 0
    try:
        for entry in os.listdir(dir):
            path = os.path.join(dir, entry)
            is_dir = os.path.isdir(path)
            if is_dir is True:
                sub_dir_size = get_dir_size(os.path.join(dir, path))
                total += sub_dir_size
            else:
                total += os.path.getsize(path)
        return total
    except Exception as e:
        raise Exception(
            f"Error: {e}")
