from tkinter import *
from PIL import Image,ImageTk




class SecondOption:
	def __init__(self,root):
		self.root = root
		self.root.title("Log Details For 192.168.41.75")
		self.root.geometry("1135x570+232+165")

		#================================ right side img ==================================
		img3 = Image.open(r"/home/justdial/Preparation/SystemDesign/Log_View_System/images/just2.jpg")
		img3 = img3.resize((400,400),Image.Resampling.LANCZOS)
		self.photoimg3 = ImageTk.PhotoImage(img3)

		lblimg3 = Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
		lblimg3.place(x=350,y=100,width=400,height=400)

		'''
		#================================ title ====================================
		lbl_title = Label(self.root,text = "LOG VIEW SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
		lbl_title.place(x=0,y=0,width=1550,height=100)

		#================================ logo ====================================
		img = Image.open(r"/home/justdial/Preparation/SystemDesign/Log_View_System/images/logo1.png")
		img = img.resize((320,100),Image.Resampling.LANCZOS)
		self.photoimg = ImageTk.PhotoImage(img)

		lblimg = Label(self.root,image=self.photoimg,bd=4,relief=RIDGE)
		lblimg.place(x=0,y=0,width=320,height=100)

		#================================ main frame ==================================
		main_frame = Frame(self.root,bd=4,relief=RIDGE)
		main_frame.place(x=0,y=100,width=1550,height=700)

		#================================ menu ====================================
		lbl_menu = Label(main_frame,text = "SERVER",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
		lbl_menu.place(x=0,y=0,width=230)

		#================================ btn frame ==================================
		btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
		btn_frame.place(x=0,y=35,width=228,height=700)
	
		cust_btn = Button(btn_frame,text="192.168.24.132",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
		cust_btn.grid(row=0,column=0,pady=1)

		room_btn = Button(btn_frame,text="192.168.41.75",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
		room_btn.grid(row=1,column=0,pady=1)

		detail_btn = Button(btn_frame,text="192.168.42.27",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
		detail_btn.grid(row=2,column=0,pady=1)

		#================================ right side img ==================================
		img3 = Image.open(r"/home/justdial/Preparation/SystemDesign/Log_View_System/images/just1.jpg")
		img3 = img3.resize((300,300),Image.Resampling.LANCZOS)
		self.photoimg3 = ImageTk.PhotoImage(img3)

		lblimg3 = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
		lblimg3.place(x=225,y=0,width=300,height=300)
		
		#================================ left side img ==================================
		img4 = Image.open(r"/home/justdial/Preparation/SystemDesign/Log_View_System/images/just2.jpg")
		img4 = img4.resize((300,300),Image.Resampling.LANCZOS)
		self.photoimg4 = ImageTk.PhotoImage(img4)

		lblimg4 = Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
		lblimg4.place(x=525,y=0,width=300,height=300)

		#================================ left side img ==================================
		img5 = Image.open(r"/home/justdial/Preparation/SystemDesign/Log_View_System/images/just3.jpg")
		img5 = img5.resize((300,300),Image.Resampling.LANCZOS)
		self.photoimg5 = ImageTk.PhotoImage(img5)

		lblimg5 = Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
		lblimg5.place(x=825,y=0,width=300,height=300)
		'''


if __name__ == '__main__':
	root = Tk()
	obj = SecondOption(root)
	root.mainloop()
