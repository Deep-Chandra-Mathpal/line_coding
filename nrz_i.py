from unipolar import draw
import matplotlib.pyplot as plt
import numpy as np
H_VOLT = 1
Z_VOLT = 0
L_VOLT = -1 
def nrz_i(bits:list):
    res = list()
    prev = -1
    for i in bits:
        if i==1 and prev==-1:
            res+=[H_VOLT]
            prev=1
        elif i==1 and prev ==1:
            res+=[L_VOLT]
            prev=-1
        elif i==0 and prev ==1:
            res+=[H_VOLT]
        else: 
            res+=[L_VOLT]
    res+=[res[-1]]
    return res


def main():
    ip = input("enter data bits : ")
    bits = list()
    for i in ip:
        bits+=[int(i)]
    print(bits)
    encoding = nrz_i(bits)
    draw(encoding, "NRZ-I",1 )

if __name__=="__main__":
    main()