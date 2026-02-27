
# Importam ConnectHandler pentru a gestiona conexiunile SSH catre echipamentele Cisco.
from netmiko import ConnectHandler

# --- INCARCAREA DATELOR DIN EXTERIOR ---

# Citim fisierul 'commands_file' care contine lista de configurari (ex: vlan 10, description, etc.).
# Metoda splitlines() elimina caracterele invizibile de tip "linie noua" (\n).
with open('commands_file') as f:
    commands_list = f.read().splitlines()

# Citim fisierul 'devices_file' care contine lista cu adresele IP ale echipamentelor.
with open ('devices_file') as f:
    devices_list = f.read().splitlines()

# --- PROCESUL DE AUTOMATIZARE ---

# Parcurgem fiecare IP gasit in fisierul de dispozitive.
for devices in devices_list:
    # Verificam daca linia curenta are text (pentru a evita erorile daca exista linii goale in fisier).
    if devices:
        print('Connecting to device: ' + devices)
        ip_address_of_device = devices
        
        # Construim dictionarul de conexiune. 
        # Datele de login raman constante, dar IP-ul se schimba la fiecare iteratie a buclei.
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': 'busu',
            'password': 'cisco',
        }

        # Realizam conexiunea SSH catre echipamentul curent.
        net_connect = ConnectHandler(**ios_device)
        
        # Metoda send_config_set intra automat in modul 'conf t', 
        # trimite toate comenzile din lista si apoi iese la final.
        output = net_connect.send_config_set(commands_list)
        
        # Afisam output-ul pentru a confirma aplicarea configuratiilor.
        print(output)
        
        # Inchidem conexiunea inainte de a trece la urmatorul IP din lista.
        net_connect.disconnect()

