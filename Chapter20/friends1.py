#!/usr/bin/env python
# -*- coding:utf8
# <Python 核心编程> 例20.4（P570）

import cgi
reshtml = '''Content-Type: text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo (dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML>'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print reshtml % (who, who, howmany)

