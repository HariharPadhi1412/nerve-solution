import socket

def create_socket():
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('localhost', 8888) 
    new_socket.connect(address)
    return new_socket

def start_client():
    sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('localhost', 8888)

    print(f"Connecting to {address}")
    sockets.connect(address)

    try:
        while True:
            message = input("Enter a message || type 'exit' to close conn: ")
            sockets.sendall(message.encode())

            if message.lower() == 'exit':
                break

            while True:
                data = sockets.recv(1024)
                if not data:
                    break
                print(f"Received from server: {data.decode()}")
            sockets = create_socket()
 
    finally:
        sockets.close()
        print("Connection closed")

if __name__ == "__main__":
    start_client()
