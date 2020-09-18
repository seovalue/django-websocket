import socket

'''
클라이언트는 바인드나 리스닝 과정이 필요없습니다.
클라이언트는 능동적으로 서버에 연결하여 연결된 소켓으로 1:1로 서버와 통신합니다. 
'''

def run_client(host='127.0.0.1', port=5000):
  with socket.socket() as sock:
    sock.connect((host, port))
    sendmsg = input('>> ') #입력된 메시지를 서버에 전송합니다.
    sock.sendall(sendmsg.encode())
    result = sock.recv(1024)
    print(f'Client: {result.decode()}')

if __name__ == '__main__':
  run_client()