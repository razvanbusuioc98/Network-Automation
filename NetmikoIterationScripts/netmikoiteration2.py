# Importam ConnectHandler din libraria Netmiko pentru a gestiona conexiunile SSH.
from netmiko import ConnectHandler

# --- GESTIONAREA FISIERELOR EXTERNE ---
# Deschidem fisierul text care contine comenzile de configurare (ex: 'vlan 10', 'name Management').
# splitlines() transforma continutul fisierului intr-o lista de Python, eliminand caracterele de tip "new line".
with open('commands_file') as f:
    commands_to_send = f.read().splitlines()

# --- DEFINIREA ECHIPAMENTELOR ---
# Cream un dictionar cu detaliile de conectare pentru un switch Cisco.
ios_devices = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'busu',
    'password': 'cisco'
}

# Punem dictionarul intr-o lista. 
# Chiar daca avem un singur device acum, structura de tip lista ne permite sa adaugam 
# foarte usor alte zeci de echipamente in viitor.
all_devices = [ios_devices]

# --- PROCESUL DE AUTOMATIZARE ---
# Parcurgem lista de echipamente folosind o bucla 'for'.
for devices in all_devices:
    # Realizam conexiunea SSH prin despachetarea dictionarului (**devices).
    net_connect = ConnectHandler(**devices)
    
    # Utilizam metoda 'send_config_set'.
    # SPRE DEOSEBIRE de 'send_command', aceasta metoda:
    # 1. Intra automat in modul 'config terminal' (conf t).
    # 2. Trimite toata lista de comenzi pe rand.
    # 3. Iese din modul de configurare la final.
    output = net_connect.send_config_set(commands_to_send)
    
    # Afisam rezultatul primit de la echipament pentru a verifica daca au existat erori de sintaxa.
    print(output)
    
    # Inchidem sesiunea SSH.
    net_connect.disconnect()