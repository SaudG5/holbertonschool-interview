#!/usr/bin/python3
"""Reads log lines from stdin and prints file size and status code stats."""
import sys


def print_stats(total_size, status_counts):
    """Print the total file size and the count of each status code."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin line by line and print stats every 10 lines."""
    total_size = 0
    line_count = 0
    status_counts = {"200": 0, "301": 0, "400": 0, "401": 0,
                     "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in status_counts:
                    status_counts[parts[-2]] += 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()