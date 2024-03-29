#!/usr/bin/python3
'''Reads stdin line by line and parses http request logs'''
import sys
import re


def initialize_log():
    '''
    Creates a dictionary that stores file size and counts of HTTP status codes
    '''
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    log = {'file_size': 0, 'code_list': {
        str(code): 0 for code in status_codes}}
    return log


def parse_line(line, regex, log):
    '''
    Processes the log by using regular expressions to find a match.
    updates the log dict file
    '''
    match = regex.fullmatch(line)

    if match:
        status_code, file_size = match.group(1, 2)

        log['file_size'] += int(file_size)

        if status_code.isdecimal():
            log['code_list'][status_code] += 1

    return log


def print_codes(log):
    '''prints out the file size and status codes in the required format'''
    print("File size: {}".format(log['file_size']))

    sorted_status_codes = sorted(log['code_list'])

    for code in sorted_status_codes:
        if log['code_list'][code]:
            print(f"{code}: {log['code_list'][code]}")


def main():
    '''entry point'''
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
        r'\[\d{4}-\d{2}-\d{2} '
        r'\d{2}:\d{2}:\d{2}\.\d+\] '
        r'"GET /projects/260 HTTP/1.1" '
        r'(.{3}) '
        r'(\d+)'
    )

    log = initialize_log()

    line_count = 0

    for line in sys.stdin:
        line = line.strip()

        line_count += 1

        parsed_log = parse_line(line, regex, log)

        if line_count % 10 == 0:
            print_codes(parsed_log)


if __name__ == '__main__':
    main()
