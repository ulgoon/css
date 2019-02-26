import socket


host = "localhost"
port = 12345
bufsiz = 2048

if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter hostname[{host}]: ".format(host=host)) or host
    port = input("Enter port number[{port}]: ".format(port=port)) or port

    addr = (host, int(port))
    client_sock.connect(addr)

    payload = "GET TIME"

    try:
        while True:
            client_sock.send(payload.encode('utf-8'))
            data = client_sock.recv(bufsiz)
            print(data.decode('utf-8'))

            more = input("Want more(y/n)? ")
            yes_list = ["y","Y","O","o","yes","YES"]
            if more in yes_list:
                payload = input("What do you want?")
            else:
                break
    except:
        print("Something wrong!")

    client_sock.close()
