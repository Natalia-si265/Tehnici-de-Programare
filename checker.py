import requests

SITES = [
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def build_url(host, path):
    return "https://" + host.rstrip("/") + "/" + path.lstrip("/")


def is_https(url):
    return url.startswith("https://")


def show_response(url):
    try:
        r = requests.get(url, timeout=5)
        print("Status:", r.status_code)
        print("Content-Type:", r.headers.get("Content-Type", "unknown"))

    except requests.RequestException:
        print("Eroare: cererea nu a putut fi finalizata")


def check_site(url):
    try:
        r = requests.get(url, timeout=5)

        return {
            "status": r.status_code,
            "content_type": r.headers.get("Content-Type", "unknown"),
            "length": len(r.content),
            "server": r.headers.get("Server", "unknown"),
        }

    except requests.RequestException:
        return {
            "status": None,
            "error": "Cererea nu a putut fi finalizata",
        }


# Functie ajutatoare pentru sortare.
def lungime(rezultat):
    return rezultat["length"]


def scan_sites():
    rezultate = []

    for url in SITES:
        rezultat = check_site(url)
        rezultat["url"] = url
        rezultate.append(rezultat)

    reusite = []
    esuate = 0

    for rezultat in rezultate:
        if rezultat["status"] == 200:
            reusite.append(rezultat)
        else:
            esuate += 1

    reusite.sort(key=lungime, reverse=True)

    for rezultat in reusite:
        print(
            rezultat["url"],
            "-> 200,",
            rezultat["length"],
            "octeti"
        )

    print("Reusite:", len(reusite), "| Esuate:", esuate)


def check_headers(url):
    try:
        r = requests.get(url, timeout=5)

        present = []
        missing = []

        # Numele anteturilor sunt comparate indiferent de majuscule.
        for header in SECURITY_HEADERS:
            if header in r.headers:
                present.append(header)
            else:
                missing.append(header)

        score = int(len(present) * 100 / len(SECURITY_HEADERS))

        return {
            "present": present,
            "missing": missing,
            "score": score,
        }

    except requests.RequestException:
        return {
            "status": None,
            "error": "Cererea nu a putut fi finalizata",
        }


def retry_check():
       pass