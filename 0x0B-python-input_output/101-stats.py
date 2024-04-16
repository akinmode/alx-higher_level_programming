#!/usr/bin/python3
""" A script that reads stdin line by line
    and computes metrics.
"""
import sys

def printStats(t_size, s_dict):
    """
        Outputs the formatted result
    """
    print(f"File size: {t_size}")
    for stat_code, stat_pop in s_dict.items():
        if stat_pop > 0:
            print(f"{stat_code}: {stat_pop}")

def StatInputs():
    """
        Receives line by line input from a file or stdout
        format:
        <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    total_size = 0
    line_count = 0
    stat_dict = { '200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    try:
        for inline in sys.stdin:
            line_count += 1
            parts = inline.split()

            total_size += int(parts[8])
            stat_dict[parts[7]] += 1
            if line_count % 10 == 0:
                printStats(total_size, stat_dict)

    except KeyboardInterrupt:
        printStats(total_size, stat_dict)
    

if __name__ == "__main__":
    StatInputs()
