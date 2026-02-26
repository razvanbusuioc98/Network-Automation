# Definim o variabila numita 'device' si ii atribuim valoarea text (string) 'router'.
# In scripturile reale din productie, aceasta valoare nu va fi scrisa manual de tine, 
# ci va fi extrasa automat din echipament (de ex: scriptul se conecteaza si citeste hostname-ul).
device = 'router'

# Prima verificare (IF): Python verifica daca valoarea variabilei este exact 'router'.
# Atentie: Se foloseste dublu egal (==) pentru a face o comparatie.
if device == 'router':
    # Daca afirmatia este Adevarata (True), scriptul executa actiunea de mai jos si se opreste din cautat.
    print ('Router found')

# Alternativele (ELIF - Else If): Aceste blocuri sunt evaluate DOAR DACA verificarile anterioare au fost False.
# Daca la inceput puneam device = 'switch', Python ignora primul IF si intra direct aici.
# Dar pentru ca a gasit deja 'router'-ul mai sus, Python va ignora complet toate liniile ELIF de mai jos.
elif device == 'switch':
    print ('Switch found')

elif device == 'load balancer':
    print ('Load balancer found')

elif device == 'firewall':
    print('firewall found')

# Cazul de rezerva (ELSE): Acest bloc nu are o conditie si se executa STRICT in cazul in care 
# absolut niciuna dintre variantele IF sau ELIF de mai sus nu a fost intalnita 
# (de ex: daca la inceput defineam device = 'server').
else:
    print ('No device found')
