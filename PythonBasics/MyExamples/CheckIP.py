#!/usr/bin/env python3

import re

try:
    ipaddr = input("Enter Ip addr: ")
    comp = re.match('^(\d{1,3}\.){3}(\d{1,3})$',ipaddr)
    if comp:
        if 0 <= int(comp.group(1).split('.')[0]) <=256 and 0 <= int(comp.group(2).split('.')[0]) <=256:
            print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")
except Exception as e:
    print("Invalid IP addr \n{}".format(e))
