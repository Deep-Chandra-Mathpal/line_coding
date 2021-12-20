from unipolar import draw
import matplotlib.pyplot as plt
import numpy as np
H_VOLT = 1
Z_VOLT = 0
L_VOLT = -1
def man(bits:list):
    res = list()
    for i in bits:
        if i==1:
            res +=[L_VOLT,H_VOLT]
        else:
            res +=[H_VOLT,L_VOLT]
    res += [res[-1]]
    return res

def main():
    ip = input("enter data bits : ")
    bits = list()
    for i in ip:
        bits+=[int(i)]
    print(bits)
    encoding = man(bits)
    draw(encoding, "Manchester",0.5)

if __name__=="__main__":
    main()