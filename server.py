#!/usr/bin/python3           # This is server.py file

import socket               # Import socket module
import sys

def main():
    """Server program for the RSA algorithm imlpementation, this program
    takes 4 command-line arguments for parameter generation in order:
    python3 server.py [p] [q] [e] [d] [local IP].

    From which n is calculated and subsequent messages are ciphered or
    deciphered
    """
    
    # Validation block
    # p and q must be prime, gcd(e and phi(n)) must be 1, and d must be
    # e's inverse modulo phi(n)
    # 1 Checking number of arguments
    if len(sys.argv) != 4:
            print('Invalid number of console arguments\n' +
                  '%s [n] [d] [local IP]' % sys.argv[0])
            sys.exit(2)
    else:
            n = int(sys.argv[1])
            d = int(sys.argv[2])
            host = sys.argv[3]

    # Hybrid socket creation
    # This program is called 'server' just because it waits for the
    # first connection, from there on it's really an hybrid socket for
    # sending and receiving data
    
    s = socket.socket()      # Create a socket object       
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))    # Bind to the port for listening

    s.listen(5)                 # Now wait for 'client' connection.
    
    # Main program functionality
    # For more details see 'Diffie-Hellman algorithm'
    
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from ', addr)
    
    ciphertext = c.recv(4096)

    cipher_list = [ ciphertext[i : i+32] for i in range (0, 4096, 32) ]
    cipher_int_list = [ ]
    plain_int_list = [ ]
    plaintext = ''

    for cipher in cipher_list:
        cipher_int_list.append( int.from_bytes(cipher, byteorder='little', signed=False) )
        plain_int_list.append( pow(cipher_int_list[-1], d) % n)
        plaintext += chr(plain_int_list[-1])

    print(plaintext)
       
    c.close() # Close the connection

if __name__ == '__main__':
    main()
