import pandas as pd
import os
import zipfile
import re

# Specify relative path to the zipped folder containing assignment CSV files
folder_path = 'Assignment 2.zip'

# Extract all CSV files from the zipped folder
with zipfile.ZipFile(folder_path, 'r') as zip_ref:
    zip_ref.extractall('extracted_folder')

# Dictionary to identify column names you want to copy in each file
column_mapping = {
    'CSV1.csv': 'SHORT-TEXT',
    'CSV2.csv': 'TEXT',
    'CSV3.csv': 'TEXT',
    'CSV4.csv': 'TEXT'
}

# Create a list to store text from all CSV files
combine_texts = []

# Loop through each CSV file in the extracted folder
for filename, column_name in column_mapping.items():
    file_path = os.path.join('extracted_folder', filename)
    
    # Read the CSV file using pandas
    df = pd.read_csv(file_path)
    
    # Extract text from the specified column
    texts = df[column_name].tolist()
    
    # Copy the text to the list
    combine_texts.extend(texts)

# Join all texts into a single string
combine_texts_final = '\n'.join(combine_texts)

# Define a function to remove numbers, and symbols and convert the text to lowercase for tokenizer efficiency
def clean_and_lower(text):
    # Remove symbols and integers using regex and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    return cleaned_text

# Action "Clean and convert the combined text to lowercase"
combine_texts_cleaned = clean_and_lower(combine_texts_final)

# Write the cleaned text to a new .txt file
cleaned_output_file_path = 'cleaned_output_text.txt'
with open(cleaned_output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(combine_texts_cleaned)

print(f'Cleaned and lowercase text extracted and stored in {cleaned_output_file_path}')
