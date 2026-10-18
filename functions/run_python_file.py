import os.path
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
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
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'

        if valid_target_dir:
            absolute_file_path = os.path.abspath(
                os.path.join(work_directory, file_path)
            )

            command = ["python", absolute_file_path]

            if args:
                command.extend(args)

            completed_process = subprocess.run(
                command, capture_output=True, timeout=30, text=True
            )

            output_string = ""

            if completed_process.returncode != 0:
                output_string += (
                    f"Process exited with code {completed_process.returncode}"
                )

            if (
                len(completed_process.stdout) == 0
                and len(completed_process.stderr) == 0
            ):
                output_string += "No output produced"

            output_string += f"""
            STDOUT:
                {completed_process.stdout}
            STDERR:
                {completed_process.stderr}
            """

            return output_string

    except Exception as e:
        print(f"Error: {e}")


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Provides ability to run python files with the relevant arguments and provides the output from that function",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path of the python program to be executed",
                },
                "args": {
                    "type": "list",
                    "description": "A list of arguments in the form of strings that should be passed to the python file being run",
                },
            },
        },
    },
}
