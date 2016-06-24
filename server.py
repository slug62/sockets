from socket import socket
import logging
import polynomials as poly

__author__ = 'peter'


def server_port():
    return 12321


encoding = 'UTF-8'


def binom(n,m):
    b = 1
    for i in range(0,m):
        b = b * (n-i) // (i+1)
    return b

if __name__ == "__main__":

    logging.basicConfig(filename='example.log', level=logging.INFO)

    # setting up a listener socket
    sock = socket()  # this is how you create a new object,
    sock.bind(('', server_port()))
    #  ('', server_port())  is the socket 'address'
    # ''  is the host, which is all possible addresses
    # server_port() is the port number, 12345
    sock.listen(0)  # 0 backlog of connections

    while True:
        (conn, address) = sock.accept()
        logging.info("connection made {}".format(conn))
        logging.info(str(address))

        # conn is a socket that will be used to communicate with the client

        # get data from client (request)
        data_string = ""
        bytes = conn.recv(2048)
        while len(bytes) > 0:
            # we actually got data from the client
            bytes_str = bytes.decode(encoding)
            logging.info("data received: |{}|".format(bytes_str))
            data_string += bytes_str
            bytes = conn.recv(2048)

        logging.info("all data received: " + data_string)

        # (n,m) = data_string.split(' ')
        # print("n is {} and m is {}".format(n,m))

        response = 'response was not properly set'

        values = data_string.split(' ')
        logging.info("values: {}".format(values))
        if len(values) != 2:
            n = 0
            m = 0
            logging.error("Invalid request syntax |{}|".format(data_string))
            response = 'Invalid request syntax'
        else:
            n = values[0]
            m = values[1]

            logging.info("n is {} and m is {}".format(n, m))

            try:
                n = int(n)  # check this for errors!
                m = int(m)  # check for errors

                if m < 0 or n < m:
                    response = 'm should be between 0 and n inclusive'
                    logging.error("m out of proper range m = {}  n = {}".format(m, n))
                else:
                    # compute
                    b = binom(n, m)
                    response = str(b)
            except:
                response = 'invalid numeric format'

        # send result to client (response)
        conn.sendall(response.encode(encoding))
        conn.shutdown(1)  ## shutdown the sending side

        conn.close()
        logging.info("connection closed")
