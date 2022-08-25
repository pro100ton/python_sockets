import socket

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            print("An error occured!")
            client.close()
            break


def write(message: str) -> None:
    message = message
    client.send(message.encode('ascii'))


write("Settings changed\n")
write("Get status")
