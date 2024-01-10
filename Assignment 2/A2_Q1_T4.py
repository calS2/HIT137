import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

# Load spaCy model
nlp_sci = spacy.load("en_core_sci_sm")

# Load BioBERT model
tokenizer_bio = AutoTokenizer.from_pretrained("cambridgeltl/BioRedditBERT-uncased")
model_bio = AutoModelForTokenClassification.from_pretrained("cambridgeltl/BioRedditBERT-uncased")

# Assuming 'text' contains the extracted text from Task 1
doc_sci = nlp_sci(text)

# Extract diseases and drugs using spaCy
diseases_spacy = [ent.text for ent in doc_sci.ents if ent.label_ == 'DISEASE']
drugs_spacy = [ent.text for ent in doc_sci.ents if ent.label_ == 'DRUG']

# Tokenize and predict with BioBERT
inputs = tokenizer_bio(text, return_tensors="pt")
outputs = model_bio(**inputs)
predictions = torch.argmax(outputs.logits, dim=2)

# Extract diseases and drugs using BioBERT
diseases_bio = [token for token, label in zip(inputs["input_ids"][0], predictions[0]) if label == 1]
drugs_bio = [token for token, label in zip(inputs["input_ids"][0], predictions[0]) if label == 2]

# Compare the results
total_entities_spacy = len(diseases_spacy) + len(drugs_spacy)
total_entities_bio = len(diseases_bio) + len(drugs_bio)
difference = abs(total_entities_spacy - total_entities_bio)

# Check most common words
common_diseases = Counter(diseases_spacy + diseases_bio).most_common()
common_drugs = Counter(drugs_spacy + drugs_bio).most_common()
