import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = '192.168.4.37' #socket.gethostname()
    port = 8081  # Server port

    try:
        # Connection to hostname on the port.
        client_socket.connect((host, port))

        # Send a message to the server
        #message = "Hello, Server!"
        while True:
            message = ""
            action = int(input("Search or Delete Card? Enter 1 for search or 2 for delete or 3 to quit: "))
            if action == 1:
                message = "1"
                message += input("Search for a card: ")
            elif action == 2:
                message = "2"
                message += input("Delete a card: ")
            elif action == 3:
                message = "3q"
            else:
                continue
            client_socket.send(message.encode('utf-8'))

            # Receive response from the server
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received response: {response}")
            if action == 3:
                break
    except:
        print("error")
    finally:
        # Close the connection
        client_socket.close()
    client_socket.close()

if __name__ == "__main__":
    start_client()
