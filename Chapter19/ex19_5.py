#!/usr/bin/env python
# -*- coding:utf8
# <Python 核心编程> 例19.5（P539）


# 程序目的：按照指示类型创建适当前景、背景色的路灯指示牌
# 使用PFA帮助“模板化”常用GUI参数
#
# 程序功能：显示出五个带有信息的按钮，按下后分别显示相应信息
# 编程要点
# 1. PFA偏函数应用
# 2. lambda 函数
# 
# 程序中未掌握的Python知识：
# 1. eval()
# 2. 字典

# import 相应的偏函数包
from functools import partial as pto 
from Tkinter import Tk, Button, X
from tkMessageBox import showinfo, showwarning, showerror

# 定义三个字符串，功能类似于C语言中的宏
WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

# Pyhon中的映射类型，字典
SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'merging traffic': WARN,
    'one way': REGU,
}

# lambda 函数
critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed')
infoCB = lambda: showinfo('Info', 'Info Button Pressed')

top = Tk()		# 创建根窗口
top.title('Road Signs')	# 给窗口命名
Button(top, text = 'QUIT', command = top.quit, bg = 'red', fg = 'white').pack() 
# 设置第一个按钮“退出”，点击则退出程序，背景色为红色，显示字体为白色

# 
MyButton = pto(Button, top)
CritButton = pto(MyButton, command = critCB, bg = 'white', fg = 'red')
WarnButton = pto(MyButton, command = warnCB, bg = 'goldenrod1')
ReguButton = pto(MyButton, command = infoCB, bg = 'white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text = %r%s).pack(fill = X, expand = True)' % (
        signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
    eval(cmd) 

top.mainloop()