import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# Group by date
date_groups = df.groupby('Date')['Product'].apply(list)

pair_count = Counter()

# Count pairs per date
for products in date_groups:
    pairs = combinations(sorted(set(products)), 2)
    pair_count.update(pairs)

# Find max frequency
max_count = max(pair_count.values())

# Get all most frequent pairs
most_frequent_pairs = [pair for pair, count in pair_count.items() if count == max_count]

# Print in required format
for pair in most_frequent_pairs:
    print(f"{pair[0]} and {pair[1]}: {max_count} times")
