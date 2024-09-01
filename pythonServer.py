import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = "192.168.4.37"
    port = 8081  # Reserve a port for your service.

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
            response = ""
            # Receive data from the client (up to 1024 bytes)
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
            action = message[0]
            message = message[1:]
            #print(message)
            #print(action)
            if action == '3':
                #print("goodbye")
                client_socket.send("goodbye".encode('utf-8'))
                break
            elif action == '1':
                #print("1")
                response = searchForCard(message)
            elif action == '2':
                #print("2")
                response = deleteCard(message)
            print(f"Received message: {message}")

            # Send a response to the client
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
def deleteCard(name):
    with open("MTG_Database.txt", "r") as file:
        lines = file.readlines()
        for index, cName in enumerate(lines):
            #print(index, cName)
            filt = cName.index("$")
            cardName = cName[0:filt]
            count = int(cName[filt+1:])
            #print(cName, cardName, count)
            if cardName.lower() == name.lower():
                #print("here")
                if count == 0:
                    lines[index] = f"{cardName}$ {count}\n"
                else:
                    count -= 1
                    lines[index] = f"{cardName}$ {count}\n"
                with open("MTG_Database.txt", "w") as outfile:
                    #print(lines)
                    for card in lines:
                        outfile.write(card)
                return f"{cardName}, {count}"
            
        return "card not found"



if __name__ == "__main__":
    start_server()

