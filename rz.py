from unipolar import draw
import matplotlib.pyplot as plt
import numpy as np
H_VOLT = 1
Z_VOLT = 0
L_VOLT = -1
def rz(bits:list):
    res = list()
    for i in bits:
        if i == 0:
            res += [L_VOLT,Z_VOLT]
        else:
            res += [H_VOLT,Z_VOLT]
    res += [Z_VOLT]
    return res

def main():
    ip = input("Enter data bits : ")
    bits = list()
    for i in ip:
        bits+=[int(i)]
    print(bits)
    encoding = rz(bits)
    draw(encoding, "RZ" ,0.5 )

if __name__=="__main__":
    main()