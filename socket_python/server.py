import socket

def run_server(host = '127.0.0.1', port= 5000):
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(1)
        connect, addr = sock.accept()
        msg = connect.recv(1024)
        print(f'Receive Message: {msg.decode()}')
        connect.sendall(msg)
        connect.close()

if __name__ == '__main__':
  run_server()