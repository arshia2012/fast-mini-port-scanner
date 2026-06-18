import socket
import threading

def socketRadar(listResult, IP, port):
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.settimeout(0.5)
    result = sok.connect_ex((IP, port))
    if result == 0:
        listResult.append(port)

trueResultList = []
threads = []

print("PORT SCANNER MADE BY aCoDeR RUNNING WITH SET TIMEOUT OF 0.5 SECOND")
print("UNDER MIT LIECENCE")

host = input("HOST IP ADDRESS: ")

for thePort in range(1, 1024):
    t = threading.Thread(target=socketRadar, args=(trueResultList, host, thePort))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(trueResultList)

if len(trueResultList) == 0:
    print("NO PORT FOUND")
