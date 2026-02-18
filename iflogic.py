# Importam clasa ConnectHandler din Netmiko pentru conectarea prin SSH.
from netmiko import ConnectHandler

# Definim parametrii de conectare pentru echipamentul nostru.
iosv_switch = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'busu',
    'password': 'cisco'
}

# Stabilim conexiunea cu echipamentul folosind detaliile din dictionar.
net_connect = ConnectHandler(**iosv_switch)

# AICI E O NOUTATE: Folosim metoda 'send_command' (nu send_config_set).
# 'send_command' este folosita strict pentru comenzi de tip "show" (privilege exec mode).
# Nu intra in 'configure terminal', ci doar citeste output-ul.
output = net_connect.send_command('show version')

# Printam in consola tot rezultatul comenzii 'show version' (care de obicei e foarte lung).
print(output)

# --- PARTEA DE LOGICA SI PARSARE DE TEXT ---

# Cautam un anumit cuvant in textul primit de la router.
# Metoda .find('vios_l2') cauta textul respectiv si returneaza POZITIA (indexul) lui in propozitie.
# Daca nu gaseste cuvantul deloc, va returna valoarea -1.
output1 = (output.find('vios_l2'))

# Verificam daca am gasit cuvantul (adica daca indexul este mai mare decat 0).
if output1 > 0:
    # Daca l-am gasit, setam variabila 'crouter' pe valoarea booleana Adevarat (True).
    crouter = True
else:
    # Daca a returnat -1 (nu a gasit), setam 'crouter' pe Fals (False).
    crouter = False

# Setam manual o alta variabila 'router' pe True (pentru scopul acestui exercitiu).
router = True


# --- NESTED IF (Conditii inlantuite) ---
# Aici verificam doua lucruri simultan, intrand "mai adanc" in logica.

# Primul IF: Se verifica daca variabila 'router' este True. (Si este, am setat-o mai sus).
if router:
    # Pentru ca primul IF este True, intram in al doilea IF (Nested IF).
    # Aici verificam rezultatul cautarii noastre in 'show version'.
    if crouter:
        # Daca ambele sunt True (e router SI am gasit cuvantul 'vios_l2' in show version):
        print ('This is a vios_l2 router')
    else:
        # Daca primul e True, dar al doilea e False (e router, dar in show version scrie altceva):
        print ('This is a router, but not a vios_l2 router')
else:
    # Acest ELSE se declanseaza DOAR DACA prima conditie (if router:) era False.
    print ('Not a router')

