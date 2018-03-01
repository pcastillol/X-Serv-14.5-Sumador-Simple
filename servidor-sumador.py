#!/usr/bin/python3

import socket
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind((socket.gethostbyname('localhost'), 1234)) #gethostbyname: Translate a host name to IPv4 address format

mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        request = str(recvSocket.recv(2048), 'utf-8') #Petición leída de recvSocket
        print('request es: \n' + request)
        resource = request.split()[1]
        print('resource es: \n' + resource)
        _, oper1, operacion, oper2 = resource.split('/')

        num1 = int(oper1)
        num2 = int(oper2)
        html_answer = calculadora.funciones[operacion](num1, num2)

        #Respuesta
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + str(num1) + " " + operacion + " " + str(num2) + " = " + str(html_answer) + '\r\n','utf-8'))
        recvSocket.close()

except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
