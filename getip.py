#coding=utf-8
import socket
import time
import platform
from tkinter import *
from datetime import datetime

def UsePlatform():
  sysstr = platform.system()
  if(sysstr =="Windows"):
    return 1
  elif(sysstr == "Linux"):
    return 2
  else:
    return 3#other system



root = Tk()
root.resizable(height=False,width=False)
root.title(string=u'Info')
if 1 == UsePlatform():
	root.attributes("-toolwindow", 1)#Toolbar style，this Property is only for windows，linux can not use
root.attributes("-topmost", 1)#top
root.attributes("-alpha",1)#transparency
def RefreshIP():
	localIP = socket.gethostbyname(socket.gethostname())#Get local ip
	#get pc's hostname and ip lists
	ipList = socket.gethostbyname_ex(socket.gethostname())
	Currtime = time.strftime("%H:%M:%S")
	date = time.strftime('%Y.%m.%d %a %b(%j)')
	IP_list=ipList[2]
	var_ip.set(str(IP_list[0]))
	var_date.set(str(date))
	var_curtime.set(str(Currtime))
	var_hostname.set(str(socket.gethostname()))
	label_IP_disp.after(500, RefreshIP)

label_date=Label(root,text=u'Date:',width=10,height=2,bg='red',relief=GROOVE)
label_date.grid(row=1,column=1)
var_date = StringVar()
label_date_disp = Label(root,textvariable=var_date, width=25, height=2,bg='red',anchor ='w',relief=GROOVE)
label_date_disp.grid(row=1,column=2)

label_time=Label(root,text=u'Time:',width=10,height=2,bg='light blue',relief=GROOVE)
label_time.grid(row=2,column=1)
var_curtime = StringVar()
label_time_disp = Label(root,textvariable=var_curtime, width=25, height=2,bg='light blue',anchor ='w',relief=GROOVE)
label_time_disp.grid(row=2,column=2)

label_IP=Label(root,text=u'IP:',width=10,height=2,bg='yellow',relief=GROOVE)
label_IP.grid(row=3,column=1)
var_ip = StringVar()
label_IP_disp = Label(root,textvariable=var_ip, width=25, height=2,bg='yellow',anchor ='w',relief=GROOVE)
label_IP_disp.grid(row=3,column=2)

label_hostname=Label(root,text=u'hostname:',width=10,height=2,bg='pink',relief=GROOVE)
label_hostname.grid(row=4,column=1)
var_hostname = StringVar()
label_hostnameDisp = Label(root,textvariable=var_hostname, width=25, height=2,bg='pink',anchor ='w',relief=GROOVE)
label_hostnameDisp.grid(row=4,column=2)
RefreshIP()

root.mainloop()
