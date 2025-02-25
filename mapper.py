#!/usr/bin/env python3
import sys
import re

def tokenize(text):
    # Normalize text to lowercase and replace non-alphanumeric characters with a space.
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9]+', ' ', text)
    return text.split()

def main():
    for line in sys.stdin:
        for word in tokenize(line):
            sys.stdout.write(f"{word}\t1\n")

if __name__ == "__main__":
    main()
