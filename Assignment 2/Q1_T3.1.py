from collections import Counter

with open('cleaned_output_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

#Count occurrences
word_counts = Counter(text.split())

# Get the top 30 common words
top_30_words = word_counts.most_common(30)

# Store the top 30 words and their counts into a CSV file
import csv

with open('top_30_words.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Word', 'Count'])
    csv_writer.writerows(top_30_words)
