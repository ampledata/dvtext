#!/usr/bin/python -u

import sys

def print_error(errstr):
    sys.stderr.write(errstr)
    sys.stderr.write('\n')

while True:
    inline = sys.stdin.readline()

    if inline == '':
        print_error("NULL read. EOF?")
        break

    result = inline.split(':')
    if len(result) < 2:
        payload = result[0]
    elif len(result) == 2:
        header,payload = result
    else:
        print_error("badly formatted packet")
        continue

    try:
        sys.stdout.write(payload.decode("base64"))
    except:
        print_error(inline)
        print_error("base64 decode failure")

