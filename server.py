import socket

# Server firewall rules
ALLOWED_IPS = ["127.0.0.1"]

def server_firewall(ip):
    if ip not in ALLOWED_IPS:
        print("Blocked IP:", ip)
        return False
    return True

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("127.0.0.1", 8888))
        server_socket.listen()

        print("Server is listening for connections...")
        conn, addr = server_socket.accept()
        print("Connected to client:", addr)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            client_ip = addr[0]
            if not server_firewall(client_ip):
                continue
            print("Received from client:", data.decode())
            response = input("Enter a message to send back: ")
            conn.send(response.encode())

if __name__ == "__main__":
    start_server()
