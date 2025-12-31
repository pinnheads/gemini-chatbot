import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
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
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # check if target_file is a valid file
    if os.path.isfile(target_file) is not True:
        return f'Error: "{file_path}" does not exist or is not a regular file'

    # check if file is a valid python file
    if target_file.endswith('.py') is False:
        return f'"{file_path}" is not a Python file'

    # create command
    command = ["python", target_file]
    if args is not None:
        command.extend(args)

    try:
        result = subprocess.run(command, capture_output=True, text=True,
                                timeout=30, cwd=working_directory_abs)

        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}"
        elif result.stdout is None and result.stderr is None:
            output += "No output produced"
        else:
            output += f"STDOUT: {result.stdout} \n STDERR: {result.stderr}"

        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
