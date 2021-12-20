from unipolar import draw
import matplotlib.pyplot as plt
import numpy as np
H_VOLT = 1
Z_VOLT = 0
L_VOLT = -1 
def diff_man(bits:list):
    res = list()
    prev_lev = -1
    for i in bits:
        if i==1 and prev_lev == -1:
            res+=[1,-1]
            prev_lev = 1
        elif i==1 and prev_lev == 1:
            res+=[-1,1]
            prev_lev = -1
        elif i==0 and prev_lev == 1:
            res+=[1,-1]
        else:
            res+=[-1,1]
    res += [res[-1]]
    return res


def main():
    ip = input("enter data bits : ")
    bits = list()
    for i in ip:
        bits+=[int(i)]
    print(bits)
    encoding = diff_man(bits)
    draw(encoding, "Differential Manchester" ,0.5)

if __name__=="__main__":
    main()