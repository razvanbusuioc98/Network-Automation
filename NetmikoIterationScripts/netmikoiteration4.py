# Importam utilitarul getpass pentru a introduce parola in siguranta.
from getpass import getpass
# Importam piesa centrala pentru SSH: ConnectHandler din Netmiko.
from netmiko import ConnectHandler

# --- INTERACTIUNEA SECURIZATA CU UTILIZATORUL ---
# Citim user-ul de la tastatura. Folosim input() pentru compatibilitate cu Python 3.
username = input('Enter your SSH username: ')

# getpass() permite introducerea parolei fara ca aceasta sa apara pe ecran (shoulder surfing protection).
# Parola este stocata doar in RAM pe durata executiei scriptului.
password = getpass()

# --- PREGATIREA DATELOR DIN FISIERE EXTERNE ---
# Citim setul de comenzi de configurare dintr-un fisier text dedicat.
with open('commands_file') as f:
    commands_list = f.read().splitlines()

# Citim lista de IP-uri ale dispozitivelor tinta.
with open ('devices_file') as f:
    devices_list = f.read().splitlines()

# --- LOOP-UL DE EXECUTIE ---
for devices in devices_list:
    # Verificam daca linia curenta contine o adresa IP valida (ignoram liniile goale).
    if devices:
        print('Connecting to device: ' + devices)
        ip_address_of_device = devices
        
        # Construim dinamic dictionarul de conexiune pentru fiecare echipament in parte.
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': username,
            'password': password
        }

        # Initiem conexiunea SSH catre switch/router.
        net_connect = ConnectHandler(**ios_device)
        
        # Metoda send_config_set() gestioneaza automat trecerea in modul 'conf t'.
        output = net_connect.send_config_set(commands_list)
        
        # Afisam rezultatul executiei pentru a monitoriza statusul schimbarilor.
        print(output)
        
        # Inchidem sesiunea SSH pentru a elibera resursele (VTY lines) pe echipament.
        net_connect.disconnect()