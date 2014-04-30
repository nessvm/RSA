#!/usr/bin/python3           # This is client.py file

import socket, sys

def main():
    """Client program for the Diffie-Hellman algorithm implementation,
    takes 1 command-line argument for the IP address of the server, the
    user exponent is asked during runtime.
    """

    # Validation block
    if len(sys.argv) != 4:
        print('Invalid number of arguments\n' +
              'usage: ', sys.argv[0], ' [n] [e] [server IP address]')
        
    s = socket.socket()         # Create a socket object
    host = sys.argv[3] 
    port = 12345                # Reserve a port for your service.

    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Processing request
    s.connect((host, port))
    m = input("Message: ")

    if len(m) < 128:
        m += 'x' * ( 128 - len(m) )

    plain_ints = list(map(ord, list(m)))
    plain_bytes = bytes()

    for i in range(len(plain_ints)):
        plain_bytes += (pow(plain_ints[i], 17) % n).to_bytes(32, byteorder='little', signed=False)
        
    print( len(plain_bytes) )
    
    s.send(plain_bytes)
    
    s.close()                     # Close the socket when done

if __name__ == '__main__':
    main()
