# Importam utilitarele pentru securitatea parolelor si logica SSH.
from getpass import getpass
from netmiko import ConnectHandler

# Importam exceptiile specifice pentru a putea gestiona erorile fara a opri scriptul.
from netmiko.ssh_exception import NetmikoTimeoutException, AuthenticationException
from paramiko.ssh_exception import SSHException

# --- ETAPA DE CONFIGURARE INITIALA ---

# Cerem credentialele utilizatorului.
username = input('Enter your SSH username: ')
password = getpass()

# Incarcam listele de comenzi si dispozitive din fisiere externe.
with open('commands_file') as f:
    commands_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

# --- PROCESUL DE AUTOMATIZARE CU GESTIONAREA ERORILOR ---

for devices in devices_list:
    if devices:  # Ignoram liniile goale din fisier.
        print('\n--- Connecting to device: ' + devices + ' ---')
        ip_address_of_device = devices
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': username,
            'password': password
        }

        # Folosim blocul 'try' pentru a incerca conexiunea. 
        # Daca apare o eroare, scriptul nu se va bloca ("crash").
        try:
            # Incercam stabilirea conexiunii SSH.
            net_connect = ConnectHandler(**ios_device)

            # Daca am ajuns aici, inseamna ca suntem conectati cu succes.
            # Trimitem lista de comenzi.
            output = net_connect.send_config_set(commands_list)
            print(output)

            # Inchidem conexiunea inainte de a trece la urmatorul device.
            net_connect.disconnect()

        # --- SECTIUNEA DE EXCEPTII (CE FACEM DACA CEVA NU MERGE) ---
        
        except (AuthenticationException):
            print('Authentication failure: ' + ip_address_of_device)
            continue  # Sari peste acest device si treci la urmatorul din lista.

        except (NetmikoTimeoutException):
            print('Timeout to device: ' + ip_address_of_device)
            continue

        except (EOFError):
            print('End of file while attempting device ' + ip_address_of_device)
            continue

        except (SSHException):
            print('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
            continue

        except Exception as unknown_error:
            # Prindem orice alta eroare neprevazuta si o afisam.
            print('Some other error: ' + str(unknown_error))
            continue