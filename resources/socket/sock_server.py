import socket
from time import ctime


host = "localhost"
port = 12345
bufsiz = 1024
addr = (host, port)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addr)
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        print("Socket Server is Listening on {host}:{port}".format(host=host, port=port))
        client_sock, client_addr = server_socket.accept()
        print("Client Connected from: {addr}".format(addr=client_addr))

        while True:
            data = client_sock.recv(bufsiz)
            if not data or data == "END":
                break
            #elif data == "GET TIME":
            print("received data: {data}".format(data=data.decode('utf-8')))
            to_send = ctime()
            print("sending server time: {}".format(to_send))
            try:
                client_sock.send(to_send.encode('utf-8'))
            except:
                print("Failed")

        client_sock.close()
    server_socket.close()
