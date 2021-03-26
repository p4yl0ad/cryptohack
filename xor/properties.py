#!/usr/bin/env python3
from pwn import xor

"""
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0 
"""

k1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
k2_k1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
k2_k3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flag_k1_k3_k2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'


k1_ord = [o for o in bytes.fromhex(k1)]
#print(k1_ord)

k2_k1_ord = [o for o in bytes.fromhex(k2_k1)]
#print(k2_k1_ord)

k2_k3_ord = [o for o in bytes.fromhex(k2_k3)]
#print(k2_k3_ord)

flag_k1_k3_k2_ord = [o for o in bytes.fromhex(flag_k1_k3_k2)]
#print(flag_k1_k3_k2_ord)


# k2_ord 
    # for (ord in k1_ord),(ord in k2_k1_ord) in zip(list1, list2):
        # 

#k2_ord = [i_in_k1_ord ^ i_in_k2_k1 for (i_in_k1_ord, i_in_k2_k1) in zip(k1_ord,k2_k1_ord)]
#print(k2_ord)

#test for k2 ord
#test_k2_k1_ord = [i_in_k2_ord ^ i_in_k1_ord for (i_in_k2_ord, i_in_k1_ord) in zip(k2_ord,k1_ord)]
#print(test_k2_k1_ord)

#k3_ord = [i_in_k2_ord ^ i_in_k2_k3 for (i_in_k2_ord, i_in_k2_k3) in zip(k2_ord,k2_k3_ord)]
#print(k3_ord)


flag_k1_k3_k2_ord = [o for o in bytes.fromhex(flag_k1_k3_k2)]
print(flag_k1_k3_k2_ord)


flag_k1_ord = [i_in_flag_k1_k3_k2_ord ^ i_in_k2_k3 for (i_in_flag_k1_k3_k2_ord, i_in_k2_k3) in zip(flag_k1_k3_k2_ord, k2_k3_ord)]

print(flag_k1_ord)



flag_ord = [i_in_flag_k1_ord ^ i_in_k1_ord for (i_in_flag_k1_ord, i_in_k1_ord) in zip(k1_ord, flag_k1_ord)]
flag = "".join(chr(o) for o in flag_ord)
print(flag)
