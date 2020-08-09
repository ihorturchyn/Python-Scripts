#!/usr/bin/env python3  
import dns.resolver

hosts = ["oreilly.com", "yahoo.com", "google.com", "microsoft.com", "cnn.com"]
for host in hosts:
    result = dns.resolver.resolve(host, 'A')
    for ipval in result:
        print(host + ' IP ' + ipval.to_text())