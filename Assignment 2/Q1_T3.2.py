import csv
from collections import Counter
from transformers import AutoTokenizer
from tqdm import tqdm

file_path = 'cleaned_output_text.txt'
model_name = 'bert-base-uncased'  
output_csv = 'Bert_tokenizer_Top30_Results.csv'  

def count_and_get_top_words(file_path, model_name, output_csv, max_chunk_length=512, overlap=50, top_n=30):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Read the text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into smaller overlapping chunks (512 character chunks for bert and then add in an overlap to make sure words arent split)
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length - overlap)]

    # Initialize a counter for token counts
    total_token_counts = Counter()

    # Tokenize each chunk and update the counter
    for chunk in tqdm(chunks, desc="Tokenizing", unit="chunk"):
        # Use encode_plus for tokenization
        encoding = tokenizer.encode_plus(
            text=chunk,
            add_special_tokens=False,
            return_tensors='pt',
            truncation=True
        )
        # Extract tokens from the tensor
        tokens = tokenizer.convert_ids_to_tokens(encoding['input_ids'][0].tolist())
        total_token_counts.update(tokens)

    # Get the top N tokens
    top_tokens = total_token_counts.most_common(top_n)

    # Save results to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Token', 'Count'])
        csv_writer.writerows(top_tokens)


count_and_get_top_words(file_path, model_name, output_csv)
print("https://github.com/calS2/HIT137")
