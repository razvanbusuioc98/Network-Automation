# Importam functia principala din libraria NAPALM.
# NAPALM este folosit pentru a abstractiza interactiunea cu echipamentele (comenzi universale pentru vendori diferiti).
from napalm import get_network_driver
# Importam libraria json pentru a afisa datele colectate intr-un format usor de citit (pretty print).
import json

# Pasul 1: Selectam "driver-ul" corespunzator sistemului de operare al echipamentului.
# In cazul nostru, 'ios' pentru Cisco IOS.
driver = get_network_driver('ios')

# Pasul 2: Definim detaliile de conectare (IP, utilizator, parola).
# Cream un obiect numit 'iosvl2' care reprezinta conexiunea noastra.
iosvl2 = driver('192.168.122.72', 'busu', 'cisco')

# Pasul 3: Deschidem efectiv conexiunea SSH catre echipament.
iosvl2.open()

# --- COLECTAREA DATELOR (GETTERS) ---

# 1. Colectam informatii generale despre echipament (hostname, model, serial number, versiune OS).
# Metoda get_facts() returneaza un dictionar Python.
ios_output = iosvl2.get_facts()
# Folosim json.dumps cu indent=4 pentru a printa rezultatul structurat, nu totul pe o singura linie.
print (json.dumps(ios_output, indent=4))

# 2. Colectam starea tuturor interfetelor (daca sunt pornite/oprite, descriere, viteza, mac address).
ios_output = iosvl2.get_interfaces()
print (json.dumps(ios_output, indent=4))

# 3. Colectam contoarele de trafic pentru interfete (pachete primite/trimise, erori, etc.).
ios_output = iosvl2.get_interfaces_counters()
# sort_keys=True va aranja cheile dictionarului in ordine alfabetica.
print (json.dumps(ios_output, sort_keys=True, indent=4))



