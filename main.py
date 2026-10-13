from checker import (
    SITES,
    build_url,
    is_https,
    show_response,
    check_site,
    scan_sites,
    check_headers,
    retry_check,
)


print("\nPARTEA 1")

# Extragem numele site-ului din prima adresa.
host = SITES[0].split("://")[1]

print("Adresa cu login:", build_url(host, "login"))
print("Adresa cu /login:", build_url(host, "/login"))

print("Verificare HTTPS:", is_https(SITES[0]))
print("Verificare HTTP:", is_https(SITES[9]))


print("\nPARTEA 2")

print("Pagina obisnuita:", SITES[0])
show_response(SITES[0])

print("Pagina cu eroare 404:", SITES[6])
show_response(SITES[6])

print("Site inexistent:", SITES[9])
show_response(SITES[9])


print("\nPARTEA 3")

for url in SITES:
    rezultat = check_site(url)
    print("Verificare site:", url)
    print("Rezultat:", rezultat)


print("\nPARTEA 4")

scan_sites()


print("\nPARTEA 5")

print("Antete pentru primul site:")
print(check_headers(SITES[0]))

print("Antete pentru pagina cu doua antete de securitate:")
print(check_headers(SITES[10]))

print("Antet scris cu litere mici:")
print(check_headers(SITES[11]))

print("Antete pentru site inexistent:")
print(check_headers(SITES[9]))


print("\nPARTEA 6")

print("pass")

print("\nVerificare terminata")