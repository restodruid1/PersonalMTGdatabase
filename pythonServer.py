import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = ""
    port = 8084  # Reserve a port for your service.

    # Bind to the port
    server_socket.bind((host, port))

    # Listen for incoming connections (1 connection at a time)
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")
    try: 
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")
        while True:
            # Receive data from the client (up to 1024 bytes)
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'q':
                print("goodbye")
                client_socket.send("goodbye".encode('utf-8'))
                break
            print(f"Received message: {message}")

            # Send a response to the client
            response = searchForCard(message)
            #response = "Thank you for connecting"
            client_socket.send(response.encode('utf-8'))

        #client_socket.send("goodbye".encode('utf-8'))
    finally:
        # Close the connection with the client
        client_socket.close()
        server_socket.close()
    client_socket.close()
    server_socket.close()
def searchForCard(name):
    with open("MTG_Database.txt", "r") as file:
        for card in file:
            index = card.index("$")
            cardName = card[0:index]
            count = card[index+1:]
            #print(count)
            print(f"{cardName}, {count}")
            if name.lower() == cardName.lower():
                print("CARD FOUND!")
                return f"{cardName}, {count}"
            
        print("CARD NOT FOUND :(")
        return "Card not found"

if __name__ == "__main__":
    start_server()

