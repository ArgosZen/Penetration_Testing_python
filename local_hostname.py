#!/usr/bin/env python

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s " % host_name)
    print("IP address: %s" % ip_address)

if __name__ == 'name':
    print_machine_info()

print(print_machine_info())