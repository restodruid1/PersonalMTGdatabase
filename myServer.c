#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};
    const char *hello = "Hello from server";
    FILE *file_pointer;

    // Open the file "example.txt" in read mode
    file_pointer = fopen("MTG_Database.txt", "r");

   




    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Binding the socket to the address and port
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // Listening for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("listen failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    printf("Server is listening on port %d\n", PORT);

    // Accepting an incoming connection
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
        perror("accept failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // Reading the data sent by the client
    int valread = read(new_socket, buffer, BUFFER_SIZE);
    printf("Received: %s\n", buffer);

    // Check if the file was opened successfully
    if (file_pointer == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Read and process the file (example: print its content)
    char line[100];
    while (fgets(line, sizeof(line), file_pointer)) {
        printf("%s", line);
        if (line == buffer) {
           printf("CARDFOUND");
        }
        else {
           printf("NOTFOUND"); 
        }
    }


    // Sending a response back to the client
    send(new_socket, hello, strlen(hello), 0);
    printf("Hello message sent\n");

    // Closing the socket
    close(new_socket);
    close(server_fd);

    return 0;
}
