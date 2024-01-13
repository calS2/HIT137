from transformers import AutoTokenizer, AutoModelForTokenClassification
from collections import Counter
import csv
import torch
import psutil

# Function to get available memory in bytes
def get_available_memory():
    return psutil.virtual_memory().available

# Function to dynamically adjust chunk size based on available memory
def optimize_chunk_size():
    total_memory = psutil.virtual_memory().total
    default_chunk_size = 1000000  # You can adjust this as a starting point

    # Use a percentage of available memory for chunk size
    chunk_size_percentage = 0.1  # Adjust as needed

    available_memory = get_available_memory()
    optimized_chunk_size = min(default_chunk_size, int(total_memory * chunk_size_percentage))

    return optimized_chunk_size

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize the Auto Tokenizer with GPU support
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Initialize the Auto Model for Token Classification
model = AutoModelForTokenClassification.from_pretrained("bert-base-uncased")

# Move the model to the specified device
model.to(device)

# Path to the input text file
input_file_path = 'output_text.txt'
csv_file_path = 'top_30_tokens.csv'

# Function to tokenize and count tokens in a chunk
def process_chunk(chunk):
    # Tokenize the chunk
    encoded_inputs = tokenizer(chunk, return_tensors="pt", truncation=True, max_length=512)

    # Move the inputs to the specified device
    inputs = {key: value.to(device) for key, value in encoded_inputs.items()}

    with torch.no_grad():
        # Forward pass
        outputs = model(**inputs)

    # Process the outputs as needed
    logits = outputs.logits

    # Extract predicted labels (you might need to adjust this based on your task)
    predicted_labels = torch.argmax(logits, dim=2)

    # Convert predicted labels to tokens
    tokens = tokenizer.batch_decode(predicted_labels[0])

    return Counter(set(tokens)).most_common(30)

# Process the file in chunks
while True:
    # Dynamically adjust chunk size based on available memory
    chunk_size = optimize_chunk_size()

    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Token', 'Count'])

            while True:
                chunk = input_file.read(chunk_size)
                if not chunk:
                    break

                top_tokens = process_chunk(chunk)

                for token, count in top_tokens:
                    csv_writer.writerow([token, count])

print(f'Top 30 unique tokens and counts saved to {csv_file_path}')
