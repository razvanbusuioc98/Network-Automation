# Importam ConnectHandler din libraria Netmiko. 
# Aceasta este piesa centrala care ne permite sa vorbim prin SSH cu echipamentele Cisco.
from netmiko import ConnectHandler

# Definim dictionarul cu datele de acces pentru switch-ul nostru.
# In terminologia Netmiko, acesta este "dispozitivul tinta".
iosv_l2_s1 = {
    'device_type': 'cisco_ios', # Spunem librariei ca vorbim cu un sistem Cisco IOS standard.
    'ip': '192.168.122.72',      # Adresa IP de management a switch-ului.
    'username': 'busu',          # Utilizatorul configurat pe switch.
    'password': 'cisco'          # Parola de SSH.
}

# Cream obiectul 'net_connect' care deschide efectiv tunelul SSH.
# Operatorul '**' "despacheteaza" dictionarul de mai sus in argumente pe care ConnectHandler le intelege.
net_connect = ConnectHandler(**iosv_l2_s1)

# Utilizam metoda 'send_command'. 
# SPRE DEOSEBIRE de 'send_config_set', aceasta se foloseste pentru a extrage date (comenzi de tip SHOW).
# Nu intra in modul de configurare, ci doar citeste ce ii raspunde echipamentul.
output = net_connect.send_command('show ip int brief')

# Afisam in consola PC-ului rezultatul primit.
# Ar trebui sa vezi tabelul cu toate interfetele (GigabitEthernet, Vlan, etc.) si statusul lor.
print(output)

# Este elegant sa inchidem conexiunea la final pentru a nu tine sesiuni SSH ocupate pe switch.
net_connect.disconnect()