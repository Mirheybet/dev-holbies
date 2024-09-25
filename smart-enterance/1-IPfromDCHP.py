#!/usr/bin/python3
import re 

  

def get_dhcp_leases(log_file='/var/lib/dhcp/dhcpd.leases'): 

    leases = [] 

    with open(log_file, 'r') as file: 

        data = file.read() 

         

        lease_regex = re.compile(r'lease (\d+\.\d+\.\d+\.\d+) \{[\s\S]*?hardware ethernet ([0-9a-fA-F:]+);') 

        matches = lease_regex.findall(data) 

  

        for match in matches: 

            ip, mac = match 

            leases.append((ip, mac)) 

     

    return leases 

  

leases = get_dhcp_leases() 

for ip, mac in leases: 

    print(f"IP Address: {ip}, MAC Address: {mac}") 
