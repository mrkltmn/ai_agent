import os.path

from config import READ_LIMIT


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        work_directory = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(work_directory, file_path))

        valid_target_dir = (
            os.path.commonpath([work_directory, target_path]) == work_directory
        )

        # print("Current directory:", os.getcwd())
        # print("directory:", file_path)
        # print("target_path:", target_path)
        # print("valid_target_dir:", valid_target_dir)

        if not valid_target_dir:
            # print("valid directory test firing")
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        if valid_target_dir:
            try:
                with open(target_path) as f:
                    content = f.read(READ_LIMIT)
                    if f.read(1):
                        content += f'[...File "{file_path}" truncated at {READ_LIMIT} characters'

                return content

            except Exception as e:
                print(f"Error: {e}")

        else:
            return "something odd has happened"

    except Exception as e:
        print(f"Error: {e}")


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Provides the contents of a file in a string to be read and analyzed",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "This is the filepath of the file that is to be read, relative to the working directory",
                },
            },
        },
    },
}
