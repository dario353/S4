import socket

target = input("metti un ip: ")
portRange = input("metti un range di porte: ")

lowPort = int(portRange.split("-")[0])
highPort = int(portRange.split("-")[1])

print("Scanning host: ", target, "da porta", lowPort, "alla", highPort)

for port in range(lowPort, highPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    status = s.connect_ex((target, port))
    if status == 0:
        print("porta", port, "aperta")
    else:
        print("porta ", port, "chiusa")
    s.close
