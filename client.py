from socket import socket
from server import server_port, encoding

__author__ = 'student'

if __name__ == "__main__":
    sock = socket()
    sock.connect(('127.0.0.1', server_port()))
    print("Connection made")

    n = '3021'
    m = '3000'

    nstr = str(n) + ' ' + str(m)
    nencoded = nstr.encode(encoding)  # this is a byte string
    sock.sendall(nencoded)

    sock.shutdown(1)   # shutdown the sending side of the socket

    response_str = ""
    bytes = sock.recv(2048)
    while len(bytes) > 0:
        response_str += bytes.decode(encoding)
        #print("response str", response_str)
        bytes = sock.recv(2048)

    print("Response: ", response_str)

    sock.close()