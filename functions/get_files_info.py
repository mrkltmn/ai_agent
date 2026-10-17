import os.path


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        work_directory = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(work_directory, directory))

        valid_target_dir = (
            os.path.commonpath([work_directory, target_path]) == work_directory
        )

        # print("Current directory:", os.getcwd())
        # print("directory:", directory)
        # print("target_path:", target_path)

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'

        if valid_target_dir:
            items_in_directory = os.listdir(target_path)
            list_of_items_and_information = []
            list_of_strings_of_information = [f"Result for '{directory}' directory:"]

            for item in items_in_directory:
                try:
                    information = []
                    item_path = os.path.join(target_path, item)
                    file_size = os.path.getsize(item_path)
                    is_directory = os.path.isdir(item_path)
                    item_name = item
                    information.append(item_name)
                    information.append(file_size)
                    information.append(is_directory)
                    list_of_items_and_information.append(information)
                except Exception as e:
                    print(f"Error: {e}")

            for list in list_of_items_and_information:
                item_sentence = f"- {list[0]}: file_size={list[1]}, is_dir={list[2]}"
                list_of_strings_of_information.append(item_sentence)

            return "\n".join(list_of_strings_of_information)

            return f'Success: "{directory}" is within the working directory'

    except Exception as e:
        print(f"Error: {e}")
