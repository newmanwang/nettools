#!/usr/bin/python

import sys

file_path = "/proc/net/netstat"

file_handle = {}

file_lines = []
with open(file_path) as f:
    for line in f:
        file_lines.append(line)

tcp_ext_titles = file_lines[0]
tcp_ext = file_lines[1]

tcp_ext_title_parts = tcp_ext_titles.split(' ')
tcp_ext_parts = tcp_ext.split(' ')

if len(tcp_ext_title_parts) != len(tcp_ext_parts):
    print("tcp exe title len != value len")
    sys.exit(1)

stat_length = len(tcp_ext_title_parts)
tcp_exe_title_parts_strip = tcp_ext_title_parts[1:stat_length]
tcp_exe_parts_strip = tcp_ext_parts[1:stat_length]

for i in range(0, stat_length - 1):
    print('%-50s%-20s' % (tcp_exe_title_parts_strip[i], tcp_exe_parts_strip[i]))
