from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import csv
from collections import Counter
from tqdm import tqdm

# Load BioBERT model and tokenizer
model_name = "dmis-lab/biobert-base-cased-v1.2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Path to the cleaned text file
cleaned_text_file_path = 'cleaned_output_text_small.txt'

# Chunk size for processing data
chunk_size = 1000000

# Read the text from the cleaned text file
with open(cleaned_text_file_path, 'r', encoding='utf-8') as text_file:
    input_text = text_file.read()

# Tokenize and process data in chunks
total_chunks = (len(input_text) // chunk_size) + 1
with tqdm(total=total_chunks, desc="Processing Chunks") as pbar:
    entities = []
    for i in range(0, len(input_text), chunk_size):
        chunk = input_text[i:i + chunk_size]

        # Tokenize input text
        tokens = tokenizer(chunk, return_tensors="pt", truncation=True, max_length=512)

        # Forward pass through the model
        with torch.no_grad():
            outputs = model(**tokens)

        # Extract predicted labels
        predicted_labels = torch.argmax(outputs.logits, dim=2)

        # Convert predicted labels to tokens
        predicted_tokens = tokenizer.batch_decode(predicted_labels[0])

        # Extract entities
        current_entity = ''
        for token, label in zip(predicted_tokens, predicted_labels[0]):
            if label != 0:
                current_entity += token + ' '
            elif current_entity:
                entities.append(current_entity.strip())
                current_entity = ''

        # Print entities for debugging
        print(entities)

        pbar.update(1)

# Count the occurrences of each entity
entity_counts = Counter(entities)

# Save results to a CSV file
csv_file_path = 'bio_entities_debug.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Entity', 'Count'])

    for entity, count in entity_counts.items():
        csv_writer.writerow([entity, count])

print(f'Results saved to {csv_file_path}')
print("https://github.com/calS2/HIT137")