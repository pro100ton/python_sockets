from main import broadcast
import socket

def socket_callbac():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.listen()

if __name__ == '__main__':
    socket_callbac()
