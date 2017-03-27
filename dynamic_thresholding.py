from Tkinter import *
import cv2
#import Image, ImageTk
import PIL
from PIL import Image, ImageTk
import numpy as np
import easygui
import sys
def print_value(val):
	l=[]
	for i in lowers:
		l.append(i.get())
	u=[]
	for i in uppers:
		u.append(i.get())
	binary=get_binary((gray,l[0],u[0]))
	im = PIL.Image.fromarray(binary)
	imgtk = PIL.ImageTk.PhotoImage(image=im)
	l1.configure(image=imgtk)
	l1.image=imgtk

img = cv2.imread(sys.argv[1])
height,width=img.shape[:2]
ratio=float(700)/height
img=cv2.resize(img,(int(ratio*width),int(ratio*height)))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Rearrang the color channel
#b,g,r = cv2.split(hsv)
#img = cv2.merge((r,g,b))
thresholds=raw_input("enter names of all thresholds. eg R G B ").split()
from binary import get_binary
tk=Tk()

page1 = Frame(tk,bg="blue",width=1200,height=100)
#lr = Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
#lg = Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
#lb = Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
#lr.set(40)
#lg.set(0)
#lb.set(0)
#lr.pack(side=LEFT,expand=1,fill=BOTH)
#lg.pack(side=LEFT,expand=1,fill=BOTH)
#lb.pack(side=LEFT,expand=1,fill=BOTH)
lowers=[0]*len(thresholds)
for i in range(len(thresholds)):
	lowers[i]=Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
	lowers[i].set(0)
	lowers[i].pack(side=LEFT,expand=1,fill=BOTH)

page2 = Frame(tk,bg="blue",width=1200,height=100)
#hr = Scale(page2,orient='horizontal', from_=0, to=255, command=print_value)
#hg = Scale(page2,orient='horizontal', from_=0, to=255, command=print_value)
#hb = Scale(page2,orient='horizontal', from_=0, to=255, command=print_value)
#hr.set(255)
#hg.set(40)
#hb.set(255)
#hr.pack(side=LEFT,expand=1,fill=BOTH)
#hg.pack(side=LEFT,expand=1,fill=BOTH)
#hb.pack(side=LEFT,expand=1,fill=BOTH)
uppers=[0]*len(thresholds)
for i in range(len(thresholds)):
	uppers[i]=Scale(page1,orient='horizontal', from_=0, to=255, command=print_value)
	uppers[i].set(255)
	uppers[i].pack(side=LEFT,expand=1,fill=BOTH)

page3 = Frame(tk,bg="blue",width=1200,height=700)
im = PIL.Image.fromarray(gray)
imgtk = PIL.ImageTk.PhotoImage(image=im)
# Put it in the display window
l1=Label(page3, image=imgtk)
l1.pack()


page1.pack(expand=1,fill=BOTH)
page2.pack(expand=1,fill=BOTH)
page3.pack(side = "bottom", fill = "both", expand = "yes")
tk.mainloop()
#cv2.imwrite("testing.jpg",cv2.inRange(img,lower,upper))