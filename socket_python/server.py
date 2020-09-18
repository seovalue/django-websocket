import socket

'''
소켓 통신에서 서버는 최초의 수신자가 되는 노드를 의미합니다.
따라서 서버는 소켓을 만들고 포트에 매핑한 다음(이를 바인딩 과정이라 함.),
바인드가 완료된 후 리스닝을 수행합니다. 클라이언트가 바인딩된 포트로 연결 할 때까지 기다리는 것가 괕습니다.
accept()는 소켓과 주소정보로 구성된 튜플을 리턴합니다.
이때, 소켓은 처음에 생성한 소켓과는 별개의 객체로 클라이언트와 연결이 구성되어 실제 데이터를 주고받을 수 있는 창구가 됩니다.
'''

def run_server(host = '127.0.0.1', port= 5000):
    # socket.socket() 을 이용해 소켓 객체를 생성합니다.
    # 기본 인자값은 socket.AF_INET, socket.SOCK_STREAM 입니다.
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(1)
        connect, addr = sock.accept()
        msg = connect.recv(1024) #소켓으로부터 데이터 읽기
        print(f'Server: {msg.decode()}')
        msg = '메롱메롱'.encode() #바이트 스트림으로 변환
        connect.sendall(msg) #소켓으로 데이터를 보내기
        connect.close()

if __name__ == '__main__':
  run_server()