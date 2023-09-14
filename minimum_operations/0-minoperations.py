#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Return number of min. operations to
    copy and paste a single character 'H' to give
    the required n characters of 'H'.

    arg: `n`
    """

    if n <= 1:
        return 0

    text_file_chars = 'H'

    copied_text = text_file_chars
    op_count = 1

    # while length of text_file chars is less than n
    while len(text_file_chars) < n:
        if len(text_file_chars) != 1 and not n % len(text_file_chars):
            # if n is perfectly divisible by the len of our text char
            # copy text and append to text_file
            copied_text = text_file_chars
            op_count += 1

        # paste
        text_file_chars += copied_text
        op_count += 1

    return op_count


if __name__ == '__main__':
    res = minOperations(2147483640)
    print('minimum operations for 2147483640 chars is:', res)
