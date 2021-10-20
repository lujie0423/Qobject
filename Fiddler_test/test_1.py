# -*- coding: utf-8 -*-
import easygui as g

def a(name,age):
    print(name + age,'11111111111111')
    str1 = g.fileopenbox()
    print(str1)

if __name__ == '__main__':
    print(a('1121','1212121'))