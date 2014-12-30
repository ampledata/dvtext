#!/usr/bin/python -u

import sys
import time

if len(sys.argv) > 1:
    if sys.argv[1] == "-":
        fh = sys.stdout
    else:
        fh = open(sys.argv[1],"w")
else:
    sys.stderr.write("Please specify output device\n")
    sys.exit(1)

while True:
    inbytes = sys.stdin.read(56)
    # TNCs really like CR rather than LF
    outstr = inbytes.encode("base64").rstrip("\n")+'\r'
    fh.write(outstr)
    fh.flush()
    # We seem to need this to keep the serial buffer from overflowing.
    # At least during tests where an input file was provided. Since
    # realtime sampling would be at 320ms, this probably isn't an issue.
    time.sleep(0.25)

