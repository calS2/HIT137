import pandas as pd
import os
import zipfile

# Step 1: Specify the path to the zipped folder containing CSV files
folder_path = r'C:\Users\corey\Documents\Electrical Engineering\HIT137\Assignment 2.zip'

# Step 2: Extract all CSV files from the zipped folder
with zipfile.ZipFile(folder_path, 'r') as zip_ref:
    zip_ref.extractall('extracted_folder')

# Step 3: Create a dictionary mapping filenames to column names
column_mapping = {
    'CSV1.csv': 'SHORT-TEXT',
    'CSV2.csv': 'TEXT',
    'CSV3.csv': 'TEXT',
    'CSV4.csv': 'TEXT'
}

# Step 4: Create a list to store text from all CSV files
combine_texts = []

# Step 5: Loop through all CSV files in the extracted folder
for filename, column_name in column_mapping.items():
    file_path = os.path.join('extracted_folder', filename)
    
    # Step 6: Read the CSV file using pandas
    df = pd.read_csv(file_path)
    
    # Step 7: Extract text from the specified column
    texts = df[column_name].tolist()
    
    # Step 8: Copy the text to the list
    combine_texts.extend(texts)

# Step 9: Join all texts into a single string
combine_texts_final = '\n'.join(combine_texts)

# Step 10: Write the combined text to a new .txt file
output_file_path = 'output_text.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(combine_texts_final)

print(f'Text extracted and stored in {output_file_path}')
