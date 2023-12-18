import http.client

host = input("Metti l'IP: ")
port = input("Metti la porta: ")

if port == "":
    port = 80

try:
    connection = http.client.HTTPConnection(host, port, timeout=5)
    metodi = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"]
    metodi_SUPP = []

    for metodo in metodi:
        try:
            connection.request(metodo, "/")
            response = connection.getresponse()
            if response.status == 200:
                metodi_SUPP.append(metodo)
        except ConnectionRefusedError:
            print(f"Connessione fallita per il metodo {metodo}")
        except http.client.HTTPException as e:
            print(f"Errore HTTP durante la richiesta {metodo}: {e}")

    connection.close()


except ConnectionRefusedError:
    print("Connessione fallita")
except Exception as e:
    print(f"Errore generico: {e}")
print("Metodi supportati:", metodi_SUPP)
