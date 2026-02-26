# Importam functia pentru driver-ul de retea din NAPALM si libraria JSON pentru formatarea datelor.
from napalm import get_network_driver
import json

# Pasul 1: Initializam driver-ul pentru Cisco IOS.
driver = get_network_driver('ios')

# Pasul 2: Definim obiectul conexiunii cu IP-ul, user-ul si parola necesare.
iosvl2 = driver('192.168.122.72', 'busu', 'cisco')

# Pasul 3: Deschidem sesiunea SSH catre switch.
iosvl2.open()

# --- COLECTAREA DATELOR DE NIVEL 2 SI 3 (L2 & L3) ---

# 1. Extragem tabela de adrese MAC (MAC Address Table).
# Aceasta ne arata ce adrese MAC sunt invatate pe fiecare port si in ce VLAN.
ios_output = iosvl2.get_mac_address_table()
print (json.dumps(ios_output, indent=4))

# 2. Extragem tabela ARP (Address Resolution Protocol).
# Aceasta face legatura intre adresele IP si adresele MAC ale echipamentelor vecine.
ios_output = iosvl2.get_arp_table()
print (json.dumps(ios_output, indent=4))

# --- VERIFICAREA CONECTIVITATII (OPERATIONAL) ---

# 3. Comanda PING executata direct de pe switch catre o destinatie externa (google.com).
# NAPALM returneaza un dictionar cu detalii precum: pachete trimise/primite, RTT (round-trip time) minim/maxim/mediu.
ios_output = iosvl2.ping('google.com')
print (json.dumps(ios_output, indent=4))
