#!/usr/bin/env python3
import sys

# For every line in the input stream, split into word and its count.
for input_line in sys.stdin:
    parts = input_line.strip().split('\t')
    if len(parts) != 2:
        continue
    term, cnt_str = parts
    cnt = int(cnt_str)
    # Output the individual count for the term
    print(f"{term}\t{cnt}")
    # Also output the count under a special key for the total aggregation.
    print(f"__TOTAL__\t{cnt}")
