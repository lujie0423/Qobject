# -*- coding: utf-8 -*-
# pip install easygui

import easygui as g

str1 = g.fileopenbox()
# g.msgbox(str1)

print(str1)