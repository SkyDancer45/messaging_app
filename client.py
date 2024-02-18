import socket
import threading
answer = ''
client = socket.socket()
print('please enter the ip address of the server you want to connect to')
ip_address = str(input())
print('Please enter the port number ')
port_no = int(input())
try:
    client.connect((ip_address,port_no))
    print('successfully connected to the host server')
    welcome = client.recv(1024).decode()
    print(welcome)
except:
    pass
def talk():
    global answer
    print("Please enter what you want to say on the server or say quit to leave --- ")
    while answer != 'Quit' and answer != 'quit':
        answer = input() 
        client.send(bytes(answer,'utf-8'))
def listen():
    global answer
    while True:
        print('\n',client.recv(1024).decode(),'\n')
        if answer == 'quit':
            break
x = threading.Thread(target=talk)
y = threading.Thread(target=listen)
x.start()
y.start()

