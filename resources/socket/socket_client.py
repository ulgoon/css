import socket


host = 'localhost'
port = 12345
buffer_size = 1024
addr = (host, port)

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)

    payload = 'GET TIME'
    while True:
        try:
            client_socket.send(payload.encode('utf-8'))
            data = client_socket.recv(buffer_size)
            print(data)
            more = input("Want another one?(y/n) ")
            if more == 'y':
                payload = input("What do you want? ")
            elif more == 'n':
                break
            else:
                break
        except:
            pass
    client_socket.close()
