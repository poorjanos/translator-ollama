from pathlib import Path
import os

input_directory = Path(r"C:\Users\poorj\Projects\translator-ollama\output")

phrases =["Here is the translated text:",
          "Here is the translated text",
          "Here are the translations:",
          "Here are the translations",
          "Here is the translation:",
          "Here is the translation"]


def remove_phrase_from_file(file_path, phrase):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()
        
        # Remove the specified phrase from the content
        updated_content = content.replace(phrase, "")
        
        # Open the file in write mode to save the updated content
        with open(file_path, 'w') as file:
            # Write the updated content back to the file
            file.write(updated_content)
        
        #print(f"The phrase '{phrase}' has been removed from the file.")

    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")



text_file_list = get_filenames_in_folder(input_directory)

for file_name in text_file_list:
    for phrase in phrases:
        file_path = input_directory / file_name
        remove_phrase_from_file(file_path, phrase)


