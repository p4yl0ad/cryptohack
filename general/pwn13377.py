#!/usr/bin/env python3
from pwn import * # pip install pwntools
import json,base64,codecs
from binascii import unhexlify


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def utf8(val):
    return ''.join(chr(i) for i in val)

def b64(val):
    return base64.b64decode(val).decode('utf-8')

def hex(val):
    _bytes = [o for o in bytes.fromhex(val)]
    return ''.join(chr(i) for i in _bytes)

def bigint(val):
    print(val)
    return unhexlify(val.replace("0x", "")).decode('utf8').replace("'", '"')

def rot13(val):
    return codecs.decode(str(val), "rot-13")


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(data):
    request = json.dumps(data).encode()
    r.sendline(request)


#print(data)
#print("Received type: ")
#print(data["type"])
#print("Received encoded value: ")
#print(data["encoded"])


for i in range(0,101):
    data = json_recv()
    if "flag" in data:
        print("Flag:{}".format(data["flag"]))
        quit()

    else:


        if data["type"] == 'utf-8':
            ret = utf8(data["encoded"])

        elif data["type"] == 'hex':
            ret = hex(data["encoded"])

        elif data["type"] == 'bigint':
            ret = bigint(data["encoded"])

        elif data["type"] == 'base64':
            ret = b64(data["encoded"])

        elif data["type"] == 'rot13':
            ret = rot13(data["encoded"])


    to_send = {
        "decoded": ret
    }

    json_send(to_send)

