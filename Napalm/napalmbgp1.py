# Update repository description.
# Importam libraria json pentru a afisa datele colectate intr-un format structurat si usor de citit.
import json
# Importam functia get_network_driver din libraria NAPALM pentru a interactiona cu diverse sisteme de operare de retea.
from napalm import get_network_driver

# Pasul 1: Specificam driver-ul pentru sistemul de operare tinta (Cisco IOS).
driver = get_network_driver('ios')

# Pasul 2: Initializam conexiunea catre echipament folosind IP-ul, user-ul si parola.
# In acest caz, ne conectam la router-ul cu IP-ul 192.168.122.72.
iosvl2 = driver('192.168.122.72', 'busu', 'cisco')

# Pasul 3: Deschidem sesiunea SSH catre dispozitiv.
iosvl2.open()

# --- COLECTAREA DATELOR BGP ---

# Utilizam getter-ul specific NAPALM 'get_bgp_neighbors()'.
# Aceasta metoda este foarte puternica deoarece extrage starea vecinilor BGP, 
# uptime-ul sesiunilor si numarul de prefixe primite/trimise fara a fi nevoie sa parsam manual output-ul CLI.
bgp_neighbors = iosvl2.get_bgp_neighbors()

# Afisam rezultatul in format JSON formatat (indent=4) pentru o vizualizare clara in consola.
# Aceasta structura de date (dictionar) poate fi usor exportata ulterior catre o baza de date sau un dashboard.
print (json.dumps(bgp_neighbors, indent=4))

# Pasul 4: Inchidem conexiunea SSH pentru a asigura managementul corect al resurselor de pe router.
iosvl2.close()