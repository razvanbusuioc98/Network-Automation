# Importam clasa ConnectHandler din libraria netmiko. 
# Aceasta este folosita pentru a stabili conexiunea SSH cu echipamentul de retea.
from netmiko import ConnectHandler

# Definim un dictionar care contine detaliile de conectare pentru primul echipament (switch-ul iosv_l2_s1).
iosv_l2_s1 = {
    'device_type': 'cisco_ios', # Tipul sistemului de operare (Netmiko stie cum sa gestioneze prompturile Cisco pe baza acestuia)
    'ip': '192.168.122.81',     # Adresa IP a switch-ului in topologia GNS3
    'username': 'busu',         # Numele de utilizator configurat local pe echipament
    'password': 'cisco'         # Parola asociata utilizatorului
}

# Definim al doilea echipament (switch-ul iosv_l2_s2) cu aceleasi tipuri de parametri, dar cu IP diferit.
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'busu',
    'password': 'cisco'
}

# Cream o lista care contine dictionarele celor doua switch-uri. 
# Aceasta lista ne va permite sa iteram (sa trecem prin ele) folosind o bucla 'for'.
all_devices = [iosv_l2_s1, iosv_l2_s2]

# Incepem o bucla 'for' pentru a parcurge fiecare echipament din lista 'all_devices'.
for devices in all_devices:
    # Stabilim conexiunea SSH cu echipamentul curent din iteratie.
    # **devices "despacheteaza" dictionarul, trecand parametrii (ip, username, etc.) catre ConnectHandler.
    net_connect = ConnectHandler(**devices)
    
    # Trimitem un set de comenzi de configurare catre echipament. 
    # Aici configuram un nou VLAN (vlan 2) si ii atribuim un nume (name Python_VLAN_2).
    output = net_connect.send_config_set(['vlan 2', 'name Python_VLAN_2'])
    
    # Afisam in terminal (consola Linux) rezultatul actiunii, adica ce ar returna si CLI-ul echipamentului.
    print (output)

