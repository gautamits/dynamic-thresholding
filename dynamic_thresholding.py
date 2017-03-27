from Tkinter import *
import cv2
#import Image, ImageTk
import PIL
from PIL import Image, ImageTk
import numpy as np
import easygui
import sys
from binary import get_binary
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
thresholds=raw_input("enter names of all thresholds. eg R G B : ").split()

tk=Tk()

page1 = Frame(tk,bg="blue",width=1200,height=100)
lowers=[0]*len(thresholds)
for i in range(len(thresholds)):
	lowers[i]=Scale(page1,orient='horizontal', from_=0, to=255, command=print_value,label=thresholds[i]+"lower")
	lowers[i].set(0)
	lowers[i].pack(side=LEFT,expand=1,fill=BOTH)
page2 = Frame(tk,bg="blue",width=1200,height=100)

uppers=[0]*len(thresholds)
for i in range(len(thresholds)):
	uppers[i]=Scale(page1,orient='horizontal', from_=0, to=255, command=print_value,label=thresholds[i]+"upper")
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
