#IGMP and ICMP
import socket
import threading
server = socket.socket()
client_list = []
try:
    server.bind(('localhost',8080))
except:
    print('ERROR BINDING FAILED')
server.listen(5)
def client_handler(client):
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            last_text = data.decode()
            for x in client_list:
                x.send(bytes(last_text,'utf8')) 
    except Exception as e:
        print(f"Error in cliemt handler {e}")
    finally:
        client_list.remove(client)
        client.close()

def main():
    while True:
        client , address = server.accept()
        print(client,'has joined the server from',address[0],address[1])
        client_list.append(client)
        client.send(bytes('wlcome to the server pal','utf8'))
        t1 = threading.Thread(target=client_handler,args=(client,))
        t1.start()

main()
