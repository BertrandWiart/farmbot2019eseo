commands = {
    'rq_connect' : 1,
    'rsp_connectSuccess' : 2,
    'rsp_connectFail' : 3
}

IP = "localhost"
#IP = "172.14.1.10"
PORT = 36100
PASS = "farmbot"


def sendMsg(socket, order, msg="", encoding="utf-8"):
    device.log(message='Setting sending message !', message_type='success')
    #print("==== SENDING MSG ====")
    #print("Sending {} message".format(getDictKey(order)))
    size = len(msg)
    byte_size = size.to_bytes(3, byteorder="big", signed=False)
    header = bytearray(4)
    header[0] = order
    for i in range(3):
        header[i+1] = byte_size[i]

    if encoding == "bytes":
        msgBytes = msg
    else:
        msgBytes = bytearray(msg, encoding)

    sendData = header + msgBytes
    #print("Message sent : {}".format(sendData))
    #print("=====================")

    socket.send(sendData)

def getDictKey(value):
    for key, val in commands.items():
        if val == value:
            return key
    return None


def receiveHeader(socket):
    try :
        headerBytes = bytearray(socket.recv(4))
        #print("Header : {}".format(headerBytes))
        device.log(message='Setting receiveHEader !', message_type='success')

        order, size = None, None
        if len(headerBytes) > 0:
            order = getDictKey(headerBytes[0])
            #print("::::::::::\nSIZE : {}".format(headerBytes[1:]))
            headerBytes[0] = 0
            size = int.from_bytes(headerBytes, byteorder='big')
            #print("Order : {}".format(order))
            #print("Size  : {}\n::::::::::".format(size))
    except ConnectionResetError:
        #print("Connection reset by peer")
        order = 0
        size = 0


    return order, size


def receiveMsg(socket, side="client"):
    #print("==== RECEIVING MSG ====")
        device.log(message='Settings ReceiveMEssage !', message_type='success')
    order, size = receiveHeader(socket)
    if order == None:
        #print("[ERROR] Order = None")
        return False, None


    dataBytes = bytearray()

    if (size>0):
        dataBytes = socket.recv(size)

    if side == "server":
        if order == "rq_connect":
            #print("Password received : {}".format(dataBytes.decode()))
            if (dataBytes.decode() == PASS):
                #print("Good password !")
                sendMsg(socket, commands["rsp_connectSuccess"])
                return True, None
            else:
                #print("Bad password !")
                sendMsg(socket, commands["rsp_connectFail"])
                return False, None

        else:
            #print("[ERROR] Received a message destinated to a client, but i'm a server")
            return False, None

    else:

        if order == "rsp_connectSuccess":
            #print("Connection success !")
            return True, None, order, size

        elif order == "rsp_connectFail":
            #print("Connection failed !")
            return False, None, order, size

        else:
            #print("[ERROR] Received a message destinated to a server, but i'm a client")
            return False, None, order, size
    
    #print("=======================")
