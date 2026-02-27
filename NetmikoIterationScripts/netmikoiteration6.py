# Importam utilitarele pentru securitate, conectivitate SSH si gestionarea erorilor.
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException, AuthenticationException
from paramiko.ssh_exception import SSHException

# --- ETAPA 1: INTERACTIUNEA CU UTILIZATORUL SI SECURITATE ---
# Cerem credentialele; parola ramane mascata in terminal pentru protectie maxima.
username = input('Enter your SSH username: ')
password = getpass()

# --- ETAPA 2: MANAGEMENTUL RESURSELOR EXTERNE ---
# Incarcam fisierele de comenzi. Aceasta structura modulara permite actualizarea 
# configuratiilor fara a modifica scriptul principal.
with open('commands_file') as f:
    commands_list = f.read().splitlines() # Comenzi comune pentru toate device-urile
with open('commands_file_switch') as f:
    commands_list_switch = f.read().splitlines() # Specifice pentru Switch-uri (L2)
with open('commands_file_router') as f:
    commands_list_router = f.read().splitlines() # Specifice pentru Routere (L3)
with open('devices_file') as f:
    devices_list = f.read().splitlines() # Lista de IP-uri tinta

# --- ETAPA 3: LOGICA DE AUTOMATIZARE SI FINGERPRINTING ---
for devices in devices_list:
    if not devices: continue  # Ignoram eventualele linii goale din fisier.

    print('\n' + '=' * 30)
    print(f'Connecting to device: {devices}')

    ios_device = {
        'device_type': 'cisco_ios',
        'ip': devices,
        'username': username,
        'password': password
    }

    try:
        # Initializam conexiunea intr-un bloc try-except pentru rezilienta.
        net_connect = ConnectHandler(**ios_device)

        # 1. Aplicam configuratiile generale (Baseline Configuration)
        print("Sending general commands...")
        output = net_connect.send_config_set(commands_list)
        print(output)

        # 2. Identificarea tipului de echipament (Software Check)
        # Definim o lista de versiuni software pe care vrem sa le recunoastem.
        list_versions = [
            'vios_l2-ADVENTERPRISEK9-M',
            'VIOS-ADVENTERPRISEK9-M',
            'C1900-UNIVERSALK9-M',
            'C3750-ADVIPSERVICESK9-M'
        ]

        # Interogam echipamentul pentru a extrage informatiile despre OS.
        output_version = net_connect.send_command('show version')
        found_software = None

        for software_ver in list_versions:
            # Daca identificam unul dintre string-urile din lista in 'show version'.
            if output_version.find(software_ver) >= 0:
                print(f'Software version found: {software_ver}')
                found_software = software_ver
                break

        # 3. Aplicarea logicii conditionale
        # In functie de software-ul detectat, decidem ce set suplimentar de comenzi trimitem.
        if found_software == 'vios_l2-ADVENTERPRISEK9-M':
            print('Running Switch-specific commands...')
            output = net_connect.send_config_set(commands_list_switch)
            print(output)
        elif found_software == 'VIOS-ADVENTERPRISEK9-M':
            print('Running Router-specific commands...')
            output = net_connect.send_config_set(commands_list_router)
            print(output)
        else:
            print('No specific software matches found for extra commands.')

        # 4. Finalizarea sesiunii
        # Inchidem conexiunea doar dupa ce toate verificarile si configurarile sunt gata.
        net_connect.disconnect()

    # --- GESTIONAREA EXCEPTIILOR (RELIABILITY) ---
    except (AuthenticationException):
        print(f'Authentication failure: {devices}')
    except (NetmikoTimeoutException):
        print(f'Timeout to device: {devices}')
    except (SSHException) as e:
        print(f'SSH Issue on {devices}: {e}')
    except Exception as unknown_error:
        print(f'Some other error on {devices}: {unknown_error}')