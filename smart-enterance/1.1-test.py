#!/usr/bin/python3
import subprocess

def get_dhcp_lease_list():
    result = subprocess.run(['sudo', 'dhcp-lease-list'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return output

lease_list = get_dhcp_lease_list()
print(lease_list)

