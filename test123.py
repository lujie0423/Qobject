# -*- coding: utf-8 -*-
import easygui

def easy():
    #os.system("E:\写一个脚本\ARUTest.air\Character.air\Character.py")
    print("UItest")

message = 'ok'
message2 = 'no'
message3 = 'fine'
message4 = 'easyui'

def uiShow(message):
    #while(1):
    Yes_or_No = easygui.buttonbox(title = "test",msg = message,choices = ['1','2','3'])
    print("1111111111111111111111111")
    if Yes_or_No == '1':
        # easy()
        uiShow(message)
    elif Yes_or_No == '2':
        uiShow(message2)
    elif Yes_or_No == '3':
        uiShow(message4)
    else:
        sys.exit()



if __name__ == '__main__':
    uiShow(message)
    sys.exit()