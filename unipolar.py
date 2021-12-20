import matplotlib.pyplot as plt
import numpy as np
H_VOLT = 1
Z_VOLT = 0
L_VOLT = -1
def unipolar(bits:list):
    res = list()
    for i in bits:
        if i==1:
            res+=[H_VOLT]
        else:
            res+=[Z_VOLT]
    res+=[res[-1]]
    return res

def draw(encoding:list , s:str ,fac):
    t = fac*np.arange(len(encoding))
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    plt.step(t , encoding,'r' , linewidth='2' ,where='post')
    plt.yticks(encoding)
    plt.xlim([0,len(encoding)*fac])
    plt.ylim([-3 , 3])
    plt.title(s)
    plt.xlabel("time")
    plt.ylabel("voltage")
    plt.grid(axis='x',linestyle='--',linewidth=0.5)
    plt.show()



def main():
    ip = input("Enter data bits : ")
    bits = list()
    for i in ip:
        bits+=[int(i)]
    print(bits)
    encoding = unipolar(bits)
    draw(encoding, "Unipolar",1 )

if __name__=="__main__":
    main()
