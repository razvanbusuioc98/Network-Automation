# Importam libraria json pentru formatarea datelor colectate.
import json
# Importam functia necesara pentru a lucra cu driverele de retea din NAPALM.
from napalm import get_network_driver

# --- CONFIGURARE ---
# Definim o lista care contine adresele IP ale tuturor routerelor pe care vrem sa le verificam.
# Poti adauga oricate IP-uri aici, iar scriptul le va procesa pe rand.
bgplist = ['192.168.122.72',
           '192.168.122.71'
]

# --- PROCESUL DE AUTOMATIZARE ---
# Folosim o bucla 'for' pentru a parcurge fiecare adresa IP din lista de mai sus.
for ip_address in bgplist:
    # Afisam un mesaj in consola pentru a sti la ce echipament suntem conectati in prezent.
    print ("Connecting to " + str(ip_address))
    
    # Selectam driver-ul pentru Cisco IOS.
    driver = get_network_driver('ios')
    
    # Cream obiectul de conexiune folosind IP-ul curent din bucla si credentialele.
    iosv_router = driver(ip_address, 'busu', 'cisco')
    
    # Deschidem sesiunea SSH catre router.
    iosv_router.open()
    
    # Colectam tabela de vecini BGP. 
    # NAPALM returneaza datele intr-un format standard (dictionar), indiferent de modelul routerului.
    bgp_neighbors = iosv_router.get_bgp_neighbors()
    
    # Printam rezultatele intr-un format JSON usor de citit (pretty print).
    print (json.dumps(bgp_neighbors, indent=4))