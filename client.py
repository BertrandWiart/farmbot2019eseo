#!/usr/bin/env python


from farmware_tools import device
device.log(message='import farmwareTools !', message_type='success')
'''
from settings import *
device.log(message='settings imported !', message_type='success')
import socket
device.log(message='import socket !', message_type='success')
from time import sleep

device.log(message='import time !', message_type='success')

device.log(message='starting Client !', message_type='success')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(host,port,retry=1):
    device.log(message='before connect', message_type='success')
    connected = False
    try:
        s.connect((host, port))
        device.log(message='connected !', message_type='success')
        connected = True
    except ConnectionRefusedError:
        device.log(message='connection refused !', message_type='success')
        #print("Connection refused")
        if retry<5:
            #print("Retrying (try n°{})".format(retry+1))
            sleep(1)
            connected = connect(host, port,retry+1)
            retry+=1
        else:
            #print("Le serveur distant n'est pas joignable.")
        	device.log(message='server non joignable !', message_type='success')
    finally:return connected

if __name__ == "__main__":
    run = True
    connected = connect(IP, PORT)

    #print("----"*5)

    if connected:
        while run:
            
            # send a rq_connect command
            sendMsg(s, 1, PASS)
                
            # receive the response
            run, dataBytes, order, size = receiveMsg(s)

            # display on the web app if connectSuccess is received
            if (order == 'rsp_connectSuccess'):
                #print("\nAction performed on the web App :")
                device.log(message='Connected with to the server !', message_type='success')
            else:
                #print("Received connection failed flag, Good Bye")
                device.log(message='Received connection failed flag ! ', message_type='success')
            # close the socket
            #print("\nProcess is now done, Good bye !")
            run = False
            s.close()

    #print("----"*5)
'''
