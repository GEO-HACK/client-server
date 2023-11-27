import socket

# Client firewall rules
ALLOWED_IPS = ["127.0.0.1"]

def client_firewall(ip):
    if ip not in ALLOWED_IPS:
        print("Blocked IP:", ip)
        return False
    return True

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("127.0.0.1", 8888))
        print("Connected to the server.")

        while True:
            message = input("Enter a message to send to the server (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            client_ip = client_socket.getpeername()[0]
            if not client_firewall(client_ip):
                print("Connection blocked by client firewall.")
                break

            client_socket.send(message.encode())
            response = client_socket.recv(1024)
            print("Received from server:", response.decode())

if __name__ == "__main__":
    start_client()
