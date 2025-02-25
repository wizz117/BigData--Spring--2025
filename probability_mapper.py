#!/usr/bin/env python3
import sys

# Initialize total word count and a list to store (word, count) pairs.
grand_total = 0
entries = []

# Read each line from standard input.
for line in sys.stdin:
    tokens = line.strip().split('\t')
    # If the line indicates the total count, record it.
    if tokens[0] == "__TOTAL__":
        grand_total = int(tokens[1])
    else:
        # Otherwise, save the word and its count.
        entries.append((tokens[0], int(tokens[1])))

# Sort entries by count in descending order.
sorted_entries = sorted(entries, key=lambda pair: pair[1], reverse=True)

# Output the grand total.
print(f"__TOTAL__\t{grand_total}")
# If we have at least 15 words, output the 10th and 15th most frequent.
if len(sorted_entries) >= 15:
    tenth_word, tenth_count = sorted_entries[9]   # 10th element (index 9)
    fifteenth_word, fifteenth_count = sorted_entries[14]  # 15th element (index 14)
    print(f"10\t{tenth_word}\t{tenth_count}")
    print(f"15\t{fifteenth_word}\t{fifteenth_count}")
