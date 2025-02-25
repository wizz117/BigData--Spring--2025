#!/usr/bin/env python3
import sys

# Dictionary to hold word info by assigned ID.
id_mapping = {}
total = 0

# Process each input line.
for line in sys.stdin:
    parts = line.strip().split('\t')
    if parts[0] == "__TOTAL__":
        total = int(parts[1])
    else:
        # Expect the line format: <ID>\t<word>\t<count>
        id_num = int(parts[0])
        word = parts[1]
        count = int(parts[2])
        id_mapping[id_num] = (word, count)

# For each ID in sorted order, compute and print the probability.
for id_num in sorted(id_mapping.keys()):
    word, count = id_mapping[id_num]
    probability = count / total if total > 0 else 0
    print(f"Word #{id_num}: {word}, Probability: {probability:.6f}")
