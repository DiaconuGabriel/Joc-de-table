import socket
import pickle
import pygame

SERVER = socket.gethostbyname(socket.gethostname())

tura_player=True
tura_player1=False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (SERVER, 9090)
print('starting up on {0} port {1}'.format(SERVER,9090))
sock.bind(server_address)

sock.listen(2)

player1_connection, player1_address = sock.accept()
print('player 1 connected:', player1_address)

nr_jucatori=1
nr_jucatori1=pickle.dumps(nr_jucatori)
player1_connection.send(nr_jucatori1)

player2_connection, player2_address = sock.accept()
print('player 2 connected:', player2_address)

nr_jucatori1=2
nr_jucatori2=pickle.dumps(nr_jucatori1)
player1_connection.send(nr_jucatori2)
player2_connection.send(nr_jucatori2)

if player1_address[0]!=SERVER:
    player1_connection,player2_connection=player2_connection,player1_connection
    player1_address,player2_address=player2_address,player1_address

while True:
    if tura_player==True:
        print('player')
        try:
            player1_data = player1_connection.recv(100000)
            tura_player_primit, tura_player1_primit,dictionar, n, m= pickle.loads(player1_data)
            tura_player=tura_player_primit
            tura_player1=tura_player1_primit
        except Exception as e:
            print(e)
            player2_connection.close()
            player1_connection.close()
            break
        try:
            player2_connection.send(player1_data)
            player1_connection.send(player1_data)
            pygame.time.delay(60)
        except Exception as e:
            print(e)
            player2_connection.close()
            player1_connection.close()
            break

    if tura_player1==True:
        print('player1')
        try:
            player2_data = player2_connection.recv(100000)
            tura_player_primit2, tura_player1_primit2,dictionar, n, m= pickle.loads(player2_data)
            tura_player=tura_player_primit2
            tura_player1=tura_player1_primit2
        except Exception as e:
            print(e)
            player2_connection.close()
            player1_connection.close()
            break
        try:
            player1_connection.send(player2_data)
            player2_connection.send(player2_data)
            pygame.time.delay(60)
        except Exception as e:
            print(e)
            player2_connection.close()
            player1_connection.close()
            break
       
sock.close()
print('Serverul s-a inchis')