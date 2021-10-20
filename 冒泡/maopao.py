# -*- coding: utf-8 -*-

def maopao(a):
    for i in range(len(a)-1):
        for j in range(0,len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

    print(a)


if __name__ == "__main__":
    a=[5,20,10,1,6]
    maopao(a)