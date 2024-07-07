import os
from pathlib import Path
from docx import Document


def concatenate_text_files_to_word(folder_path, output_file):
    # Create a new Document object
    doc = Document()
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a text file
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            
            # Open the text file and read its content
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Add the content to the Word document
            doc.add_paragraph(content)
            # Optionally, add a page break after each file's content
            doc.add_page_break()
    
    # Save the Document
    doc.save(output_file)
    print(f"All text files have been concatenated and saved to {output_file}")

# Example usage
folder_path = Path(r"C:\Users\poorj\Projects\translator-ollama\output")
output_file = 'output.docx'
concatenate_text_files_to_word(folder_path, output_file)