import json


def get_personal_data():
    file_path = "./src/config/personal_data.json"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file at {file_path} is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
