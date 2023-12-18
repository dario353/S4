import socket
import concurrent.futures


def scanPort(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        status = s.connect_ex((target, port))
    return port, status


target = input("metti un ip: ")
portRange = input("metti un range di porte (ES 1-100): ")
lowPort = int(portRange.split("-")[0])
highPort = int(portRange.split("-")[1])

print("Scanning host: ", target, "da porta", lowPort, "alla", highPort)
print("Questa operazione potrebbe richiedere alcuni minuti")
with concurrent.futures.ThreadPoolExecutor(max_workers=30) as esecutore:
    result = list(esecutore.map(scanPort, range(lowPort, highPort + 1)))


PorteAperte = []
PorteChiuse = []
PorteServScono = []

for port, status in result:
    try:
        if status == 0:
            nomeServ = socket.getservbyport(port)
            PorteAperte.append((port, nomeServ))
        else:
            PorteChiuse.append(port)
    except OSError:
        PorteServScono.append(port)


print("-----------------CHIUSE----------------")
print(PorteChiuse)
print("-----------------PORTE NOME?----------------")
print(PorteServScono)
print("-----------------APERTE----------------")
for porta, servizio in PorteAperte:
    print(f"Porta: {porta} -- Servizio: {servizio}")
