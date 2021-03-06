#!/usr/bin/env python
"""Reads current data from a monitoring socket."""

import socket
import sys

if len(sys.argv) != 2:
    sys.stderr.write('Invalid arguments.\n')
    sys.stdout.write('Format is:\n\t%s PATH\n' % sys.argv[0])
    sys.exit(1)

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(sys.argv[1])
while True:
    buf = s.recv(4096)
    if buf == '':
        break
    sys.stdout.write(buf)
