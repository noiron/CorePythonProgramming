#!/usr/bin/env python
# -*- coding:utf8
# <Python 核心编程> 例18.2（P518）


# 程序目的：
#
# 程序功能：
#
# 
# 编程要点
# 
#
# 最后编辑：2014_07_10


import thread
from time import sleep, ctime

def loop0():
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'loop 0 done at:', ctime()

def loop1():
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 done at:', ctime()

def main():
    print 'starting at:', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all Done at: ', ctime()

if __name__ == '__main__':
    main()