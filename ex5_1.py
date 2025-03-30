"""

Resultados:

Registros A:
    23.215.0.133
    96.7.128.192
    23.215.0.132
    96.7.128.186
Registros MX:
    0
Registros NS:
    a.iana-servers.net.
    b.iana-servers.net.

"""

import dns.resolver

link = "example.org"

print("Registros A:")
answers = dns.resolver.resolve(link, 'A')
for rdata in answers:
    print("\t" + rdata.to_text())

print("Registros MX:")
answers = dns.resolver.resolve(link, 'MX')
for rdata in answers:
    print("\t" + str(rdata.preference))

print("Registros NS:")
answers = dns.resolver.resolve(link, 'NS')
for rdata in answers:
    print("\t" + rdata.to_text())