import os.path


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        work_directory = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(work_directory, directory))

        valid_target_dir = (
            os.path.commonpath([work_directory, target_path]) == work_directory
        )

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'

        if valid_target_dir:
            return f'Success: "{directory}" is within the working directory'

    except Exception as e:
        print(f"Error: {e}")
