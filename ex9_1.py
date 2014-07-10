#!/usr/bin/env python
# -*- coding:utf8
# <Python 核心编程> 例9.1（P223）os 和 os.path模块例子


# 程序目的：
#
# 程序功能：
#
# 
# 编程要点
# 
#
# 最后编辑：2014_07_10

import os
for tmpdir in ('/tmp', r'c:/temp'):
	if os.path.isdir(tmpdir):
		break
	else:
		print 'no temp directory available'
		tmpdir = ''

if tmpdir:
	os.chdir(tmpdir)
	cwd = os.getcwd()
	print '*** current temporary directory'
	print cwd

	print '*** creatring example directory...'
	os.mkdir('example')
	os.chdir('example')
	cwd = os.getcwd()
	print '*** new working directory: '
	print cwd
	print '*** original directory listing: '
	print os.listdir(cwd)
	print '*** creating test file...'
	fobj = open('test', 'w')
	fobj.write('foo\n')
	fobj.write('bar\n')
	fobj.close()
	print '*** updated directory listing: '