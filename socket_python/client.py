'''echo_client1.py'''
import socket

def run_client(host='127.0.0.1', port=5000):
  with socket.socket() as sock:
    sock.connect((host, port))
    sendmsg = input('input msg --> ')
    sock.sendall(sendmsg.encode())
    result = sock.recv(1024)
    print(f'{result.decode()}')

if __name__ == '__main__':
  run_client()