import os.path


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        work_directory = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(work_directory, file_path))

        valid_target_dir = (
            os.path.commonpath([work_directory, target_path]) == work_directory
        )

        # print("Current directory:", os.getcwd())
        # print("directory:", directory)
        # print("target_path:", target_path)

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        if valid_target_dir:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, mode="w") as f:
                f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Allows a file to be written using the contents passed into it at the file path described. It will create the file and parent directories if necessary",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "A string describing the file path of the file to be written or written over",
                },
                "content": {
                    "type": "string",
                    "description": "A string that is constituted of the content to be written to the file",
                },
            },
        },
    },
}
