#!/usr/bin/env python
# -*- coding:utf8
# <Python 核心编程> 例19.7（P546）Tix GUI编程演示


# 程序目的：
# 初步了解Tix模块 
#
# 程序功能：
# 选择动物的数量及种类，数量为2—12间的偶数
# 用控制组件来显示总数，用组合框显示动物种类列表菜单供用户选择
#
# 
# 编程要点
# 1. Control组件（控制按钮，由一个文本组件和一对箭头按钮组合）
# 2. ComboBox组件（组合框组件，包括一个文本组件和一个下拉菜单）
# 
#
# 最后编辑：2014_07_09

from Tkinter import Label, Button, END
from Tix import Tk, Control, ComboBox

top = Tk()
top.tk.eval('package require Tix')

lb = Label(top, text = 'Animals (in pairs; min: pair, max: dozen')
lb.pack()

ct = Control(top, label = 'Number:', integer = True, 
	max = 12, min = 2, value = 4, step = 2)
ct.label.config(font = 'Helvetica -14 bold')
ct.pack()

cb = ComboBox(top, label = 'Type:', editable = True)
for animal in ('dog', 'cat', 'hamster', 'python'):
	cb.insert(END, animal)
cb.pack()

qb = Button(top, text = 'QUIT', command = top.quit, bg = 'red', fg = 'white')
qb.pack()

top.mainloop()