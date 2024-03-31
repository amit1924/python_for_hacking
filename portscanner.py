import socket
import subprocess
from datetime import datetime  # Correct import statement for datetime module

target = input("Enter the target IP address: ")


def port_scan(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"Scanning the target IP address {ip}")

        print("Time Started: ", datetime.now())  # Correct usage of datetime.now()

        for port in range(20, 91):  # Adjusted range to include port 90
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))  # Corrected usage of connect_ex
            if result == 0:
                print("Port {} : Open".format(port))
            sock.close()

    except socket.gaierror:
        print("Hostname can't be resolved")

    except socket.error:
        print("Couldn't connect to server")


port_scan(target)
