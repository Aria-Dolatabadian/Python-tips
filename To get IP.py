import socket

def get_ip_address():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to a remote server (doesn't matter which one)
        sock.connect(("8.8.8.8", 80))

        # Get the local IP address
        ip_address = sock.getsockname()[0]

        return ip_address
    finally:
        # Close the socket
        sock.close()

# Call the function to get the IP address
ip = get_ip_address()
print("Your IP address is:", ip)
