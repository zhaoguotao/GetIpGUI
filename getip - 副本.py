#coding=utf-8
import socket
import time
from tkinter import *
from datetime import datetime

root = Tk()
root.resizable(height=False,width=False)
root.title(string=u'Info')
# root.attributes("-toolwindow", 1)#工具栏样式，该属性只在windows系统生效，linux系统会报错，默认注释
root.attributes("-topmost", 1)#置顶
root.attributes("-alpha",1)#透明度
def RefreshIP():
	localIP = socket.gethostbyname(socket.gethostname())#得到本地ip
# 	print(socket.gethostname())
	#get pc's hostname and ip lists
	ipList = socket.gethostbyname_ex(socket.gethostname())
# 	print(ipList)
	Currtime = time.strftime("%H:%M:%S")
	#~ CurrDayofYear = time.strftime("%j")
	#~ print(CurrDayofYear)
	date = time.strftime('%Y.%m.%d %a %b(%j)')
	IP_list=ipList[2]
	#~ var_ip.set(str(localIP))
	var_ip.set(str(IP_list[0]))
	var_date.set(str(date))
	var_curtime.set(str(Currtime))
	var_hostname.set(str(socket.gethostname()))
	label_IP_disp.after(500, RefreshIP)

label_date=Label(root,text=u'Date:',width=10,height=2,bg='red')
label_date.grid(row=1,column=1)
var_date = StringVar()
label_date_disp = Label(root,textvariable=var_date, width=25, height=2,bg='red',anchor ='w')
label_date_disp.grid(row=1,column=2)

label_time=Label(root,text=u'Time:',width=10,height=2,bg='blue')
label_time.grid(row=2,column=1)
var_curtime = StringVar()
label_time_disp = Label(root,textvariable=var_curtime, width=25, height=2,bg='white',anchor ='w')
label_time_disp.grid(row=2,column=2)

label_IP=Label(root,text=u'IP:',width=10,height=2,bg='yellow')
label_IP.grid(row=3,column=1)
var_ip = StringVar()
label_IP_disp = Label(root,textvariable=var_ip, width=25, height=2,bg='yellow',anchor ='w')
label_IP_disp.grid(row=3,column=2)

label_hostname=Label(root,text=u'hostname:',width=10,height=2,bg='pink')
label_hostname.grid(row=4,column=1)
var_hostname = StringVar()
label_hostnameDisp = Label(root,textvariable=var_hostname, width=25, height=2,bg='pink',anchor ='w')
label_hostnameDisp.grid(row=4,column=2)
RefreshIP()

root.mainloop()
