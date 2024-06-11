import ollama
from pathlib import Path
import os

input_directory = Path(r"C:\Users\poorj\Projects\translator-ollama\input")
output_directory = Path(r"C:\Users\poorj\Projects\translator-ollama\output")


def get_filenames_in_folder(folder_path):
    '''
    Put filenames in folder_path into a list
    '''
    # Check if the provided path is a valid directory
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"{folder_path} is not a valid directory")
    
    # List to store filenames
    filenames = []

    # Iterate through all files and directories in the provided path
    for item in os.listdir(folder_path):
        # Construct the full path
        full_path = os.path.join(folder_path, item)
        # Check if it is a file (not a directory)
        if os.path.isfile(full_path):
            filenames.append(item)
    
    return filenames



def translate_text(text):
  '''
  Translates text from hindi to english
  '''
  response_70b = ollama.chat(model='llama3:70b', messages=[
      {'role': 'system',
       'content': 'You are a hindi to english translator. Return the translated english text only without any comments or introduction!'},
      {
        'role': 'user',
        'content': text
    },
  ])

  return response_70b['message']['content']




text_file_list = get_filenames_in_folder(input_directory)


for text_file_name in text_file_list:
    with open(input_directory / text_file_name, "r", encoding='utf-8') as input_file:
        input_text = input_file.read().replace('\n', '')
        
    output_text = translate_text(input_text)

    with open(output_directory / text_file_name, "w", encoding='utf-8') as output_file:
        output_file.write(output_text)



