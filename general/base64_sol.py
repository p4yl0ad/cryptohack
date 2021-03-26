#!/usr/bin/env python3
from binascii import unhexlify, b2a_base64
import base64




hex_str = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
b64 = 'ZWd5cHRpYW5fY2x1Yl9zb2xhcg=='


result = b2a_base64(bytes.fromhex(hex_str))
#result2 = b2a_base64(b64)




base64_bytes = b64.encode('ascii') 
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')
print(message)


#print(result)
#print(result2)
