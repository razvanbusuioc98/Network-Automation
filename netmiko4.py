# Importam clasa ConnectHandler din Netmiko
from netmiko import ConnectHandler

# Definim detaliile de conectare pentru un grup mai mare de switch-uri (S2 pana la S6)
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'busu',
    'password': 'cisco'
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': 'busu',
    'password': 'cisco'
}

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

# --- PARTEA 1: CONFIGURAREA GRUPULUI 1 (Switch-urile 4, 5 si 6) ---

# Deschidem primul fisier cu comenzi (ex: configurari pentru switch-uri de Access)
with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()

# Afisam comenzile in consola pentru debugging
print ("\n--- Se aplica iosv_l2_cisco_design ---")
print (lines)

# Definim primul grup de echipamente tinta
all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

# Parcurgem grupul 1 si aplicam comenzile din primul fisier
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)


# --- PARTEA 2: CONFIGURAREA GRUPULUI 2 (Toate switch-urile de la 2 la 6) ---

# Refolosim variabila 'lines' si o suprascriem cu continutul celui de-al doilea fisier (ex: configurari de Core)
with open('iosv_l2_core') as f:
    lines = f.read().splitlines()

print ("\n--- Se aplica iosv_l2_core ---")
print (lines)

# Refolosim variabila 'all_devices' si o suprascriem cu un nou grup (de data asta includem si S2, S3)
all_devices = [iosv_l2_s6, iosv_l2_s5, iosv_l2_s4, iosv_l2_s3, iosv_l2_s2]

# Parcurgem noul grup si aplicam comenzile din fisierul 'iosv_l2_core'
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)