# Importam ConnectHandler pentru a gestiona conexiunile SSH catre echipamentele Cisco.
from netmiko import ConnectHandler

# Definim detaliile de conectare pentru switch-urile 4, 5 si 6.
iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.84',
    'username': 'busu',
    'password': 'cisco'
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.85',
    'username': 'busu',
    'password': 'cisco'
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.86',
    'username': 'busu',
    'password': 'cisco'
}

# --- NOUTATEA PRINCIPALA IN ACEST SCRIPT ---
# 'with open' este modul recomandat in Python de a deschide fisiere, deoarece il inchide automat la final.
with open('iosv_l2_cisco_design') as f:
    # f.read().splitlines() citeste tot continutul fisierului si creeaza o lista.
    # .splitlines() este esential aici pentru ca elimina automat caracterele de 'Enter' (\n) de la finalul fiecarei linii.
    lines = f.read().splitlines()

# Printam lista de comenzi extrasa din fisier in consola pentru a verifica daca a fost citita corect.
print (lines)

# Gruparea echipamentelor intr-o lista pentru a le putea parcurge.
all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

# Incepem bucla pentru a configura pe rand fiecare switch.
for devices in all_devices:
    # Stabilim conexiunea SSH.
    net_connect = ConnectHandler(**devices)
    
    # Metoda send_config_set primeste variabila 'lines' (care acum este o lista de string-uri cu toate comenzile din fisier).
    # Netmiko va trimite fiecare comanda pe rand, exact ca si cum le-ai scrie tu manual in CLI.
    output = net_connect.send_config_set(lines)
    
    # Afisam rezultatul pentru a ne asigura ca echipamentul a acceptat comenzile.
    print (output)
