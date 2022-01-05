#!/bin/python3
#from subprocess import Popen, PIPE
import sys
#sys.path.append("..")
from pyFunc import moduleSys

print('filename: ' + __file__)

#moduleSys.getCpuMips()
#print(n)
#!/usr/bin/python
import libtmux
server = libtmux.Server()
session = server.find_where({"session_name": "session_test"})

session = server.new_session(session_name="session_test", kill_session=True, attach=False)
window = session.new_window(attach=True, window_name="session_test")
pane1 = window.attached_panepane2 = window.split_window(vertical=False)
pane2 = window.split_window(vertical=False)
window.select_layout('even-horizontal')
pane1.send_keys('ls -al')
pane2.send_keys('ls -al')

server.attach_session(target_session="session_test")

