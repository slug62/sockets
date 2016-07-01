from socket import socket
from server import server_port, encoding


__author__ = 'student'


def sendtoserver(host, port, str):
    sock = socket()
    sock.connect((host, port))
    nencoded = str.encode(encoding)         # Encode string
    sock.sendall(nencoded)                  # Send enconded string
    sock.shutdown(1)                        # Shutdown the sending side of the socket
    response = getserverresponse(sock)      # Get the response from the server
    sock.close()                            # Close the socket
    return response


def getserverresponse(sock):
    response_str = ""
    bytes = sock.recv(2048)
    while len(bytes) > 0:
        response_str += bytes.decode(encoding)
        bytes = sock.recv(2048)
    return response_str


def buildrequest(type, content):
    request = ""
    if type == 'E':
        request += type + str(content[0])
        for c in content[1]:
            request += ' ' + str(c)
    elif type == 'S':
        request += type + str(content[0]) + ' ' + str(content[1])
        for c in content[2]:
            request += ' ' + str(c)
        request += ' ' + str(content[3])
    else:
        print("You specified an incorrect reqeust type.")
    #print(request)
    return request

if __name__ == "__main__":
    a = 0
    b = 2
    poly = [-945, 1689, -950, 230, -25, 1]
    tol = 1e-15
    BISECTION = 'S'
    EVALUATE = 'E'

    bisection_result = sendtoserver('127.0.0.1', server_port(), buildrequest(BISECTION, [a, b, poly, tol]))
    # Bisection result will be the server response which will include a successful 'S' so my request below removes that
    # from the buildrequest
    evaluate_result = sendtoserver('127.0.0.1', server_port(), buildrequest(EVALUATE, [bisection_result[1:], poly]))

    print(bisection_result)
    print(evaluate_result)
