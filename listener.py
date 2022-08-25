import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()
