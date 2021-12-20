from unipolar import draw
import matplotlib.pyplot as plt
import numpy as np
H_VOLT = 1
Z_VOLT = 0
L_VOLT = -1 
def nrz_l(bits:list):
    res = list()
    for i in bits:
        if i==0:
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
    encoding = nrz_l(bits)
    draw(encoding, "NRZ-L" ,1)

if __name__=="__main__":
    main()