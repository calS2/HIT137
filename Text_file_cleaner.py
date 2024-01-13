import re

def clean_text(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    # Remove symbols and integers
    cleaned_text = re.sub('[^a-zA-Z\s]', '', text)

    with open(output_file, 'w') as file:
        file.write(cleaned_text)

clean_text('combined_output_text.txt', 'cleaned_output_text.txt')