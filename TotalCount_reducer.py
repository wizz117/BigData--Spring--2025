#!/usr/bin/env python3
import sys

aggregate_total = 0
counts_per_word = {}

# Process each line from standard input.
for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) != 2:
        continue
    key, value_str = fields
    value = int(value_str)
    
    if key == "__TOTAL__":
        aggregate_total += value
    else:
        if key in counts_per_word:
            counts_per_word[key] += value
        else:
            counts_per_word[key] = value

# Emit the computed grand total.
print(f"__TOTAL__\t{aggregate_total}")

# Emit each word along with its summed count.
for term, total in counts_per_word.items():
    print(f"{term}\t{total}")
