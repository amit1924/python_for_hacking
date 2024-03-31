import socket  # Import the socket module for low-level networking operations

# from scapy.all import *  # Import all symbols from the scapy module
from scapy.all import Ether  # Import all symbols from the scapy module

# Create a socket object for sniffing packets
# AF_PACKET indicates that this socket will work at the network layer
# SOCK_RAW specifies that the socket will receive raw packets
# ntohs(3) converts the protocol number 3 (which represents IPv4) to network byte order
sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

# Specify the network interface to sniff on (e.g., "eth0" for Ethernet interface)
interface = "Wi-Fi"

# Bind the socket to the specified network interface
sniffer_socket.bind((interface, 0))

try:
    while True:
        # Receive raw packet data and the address from which it was received
        raw_data, addr = sniffer_socket.recvfrom(65535)

        # Parse the raw packet data into a Scapy packet object
        packet = Ether(raw_data)

        # Print a summary of the packet (e.g., source and destination MAC addresses)
        print(packet.summary())

except KeyboardInterrupt:
    # Close the socket when the user interrupts the program (e.g., with Ctrl+C)
    sniffer_socket.close()
