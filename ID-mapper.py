import sys

# A constant value assumed to exceed any word count encountered.
TOTAL_MAX = 10**9

def process_line(line):
    line = line.strip()
    if not line:
        return None
    try:
        token, cnt_str = line.split('\t', 1)
        cnt = int(cnt_str)
    except Exception:
        return None
    # Invert the count using the constant so that larger counts yield lower keys.
    inverted_key = TOTAL_MAX - cnt
    return f"{inverted_key:010d}\t{token}"

def main():
    for raw_line in sys.stdin:
        result = process_line(raw_line)
        if result:
            sys.stdout.write(result + "\n")

if __name__ == "__main__":
    main()
