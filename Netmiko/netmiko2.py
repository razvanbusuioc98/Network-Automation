# Importam clasa ConnectHandler din libraria netmiko pentru a realiza conexiunea SSH.
from netmiko import ConnectHandler

# Definim detaliile de conectare pentru primele 3 switch-uri din topologia noastra.
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'busu',
    'password': 'cisco'
}

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

# Cream o lista centralizatoare cu toate echipamentele pe care vrem sa aplicam configurarile.
all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

# Bucla principala (Outer Loop): Parcurgem fiecare switch din lista.
for devices in all_devices:
    # Ne conectam la switch-ul curent din iteratie.
    net_connect = ConnectHandler(**devices)
    
    # Bucla secundara (Inner Loop): Generam numerele pentru VLAN-uri.
    # Functia range(2, 21) va genera numere incepand cu 2 si terminand cu 20.
    for n in range (2,21):
        # Printam in consola PC-ului nostru ce VLAN se creeaza pentru a urmari progresul scriptului.
        print("Creating VLAN " + str(n))
        
        # Construim lista de comenzi specifice acestui VLAN din iteratie.
        # Folosim str(n) pentru a converti numarul intr-un sir de caractere (string) ca sa il putem concatena.
        config_command = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        
        # Trimitem comenzile catre echipament. Metoda send_config_set intra automat in modul 'configure terminal'.
        output = net_connect.send_config_set(config_command)
        
        # Afisam output-ul primit de la switch pentru a ne asigura ca setarile au fost aplicate fara erori.
        print(output)

