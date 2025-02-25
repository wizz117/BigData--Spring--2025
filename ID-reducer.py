#!/usr/bin/env python3
import sys

def main():
    current_index = 0
    # Process each incoming line that should contain the inverted key and the word.
    for raw_line in sys.stdin:
        stripped_line = raw_line.strip()
        if not stripped_line:
            continue
        try:
            # We don't actually use the inverted key here.
            _, token = stripped_line.split('\t', 1)
        except Exception:
            continue
        current_index += 1
        # Output the new ID followed by the word.
        print(f"{current_index}\t{token}")

if __name__ == "__main__":
    main()
