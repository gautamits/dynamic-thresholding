import cv2
def get_binary((gray,lower,upper)):
	#print val
	#lower=np.array([lr.get(),lg.get(),lb.get()],dtype="uint8")
	#print lower,upper
	#mask = cv2.inRange(img,lower,upper)
	#thresh,binary = cv2.threshold(gray,lower,upper,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	#binary = cv2.threshold(gray, lower, upper, cv2.THRESH_BINARY)[1]
	binary = cv2.inRange(gray,lower,upper)
	#grad=calcgrad(mask)
	#grad=grad*4
	return binary
	#im = PIL.Image.fromarray(binary)
	#imgtk = PIL.ImageTk.PhotoImage(image=im)
	#l1.configure(image=imgtk)
	#l1.image=imgtk