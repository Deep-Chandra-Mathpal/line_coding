from unipolar import draw
import matplotlib.pyplot as plt
import numpy as np
H_VOLT = 1
Z_VOLT = 0
L_VOLT = -1
def ami(bits:list):
    res = list()
    prev = -1
    for i in bits:
        if i==1 and prev==-1:
            res+=[H_VOLT]
            prev =1 
        elif i==1 and prev==1:
            res+=[L_VOLT]
            prev = -1
        else:
            res+=[Z_VOLT]
    res+=[res[-1]]
    return res

def main():
    ip = input("Enter data bits : ")
    bits = list()
    for i in ip:
        bits+=[int(i)]
    print(bits)
    encoding = ami(bits)
    draw(encoding, "Alternate mark inversion" ,1)

if __name__=="__main__":
    main()