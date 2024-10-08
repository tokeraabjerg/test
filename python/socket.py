import socket
import time

# Scanner's IP address and UDP port
scanner_ip = '192.168.100.1'
port = 33001  # The UDP port to test

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout for receiving data (e.g., 5 seconds)
sock.settimeout(5)

# Message to send (a simple "ping" message, can be adjusted based on protocol)
message = b"Hello Scanner"

try:
    # Send the message to the scanner
    print(f"Sending message to {scanner_ip}:{port}")
    sock.sendto(message, (scanner_ip, port))
    
    # Try to receive a response
    print("Waiting for a response...")
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received response from {addr}: {data}")

except socket.timeout:
    print(f"No response from {scanner_ip} on UDP port {port}.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the socket
    sock.close()
