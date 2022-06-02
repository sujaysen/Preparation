from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
		



class Roombooking:
	def __init__(self,root):
		self.root = root
		self.root.title("Hotel Management System")
		self.root.geometry("1120x510+230+220")

		#================================ title ====================================
		lbl_title = Label(self.root,text = "Add Customer Details",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
		lbl_title.place(x=0,y=0,width=1295,height=50)
		
		#================================ logo ====================================
		img2 = Image.open(r"/home/justdial/Preparation/SystemDesign/Hotel_Management_System/Images/logo.jpg")
		img2 = img2.resize((230,50),Image.Resampling.LANCZOS)
		self.photoimg2 = ImageTk.PhotoImage(img2)

		lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
		lblimg.place(x=0,y=0,width=230,height=50)


		#====================================labelframe===============================
		labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
		labelframeleft.place(x=5,y=50,width=425,height=490)

		#======================================labels and entry=============================
		lblcustref = Label(labelframeleft,text = "Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblcustref.grid(row=0,column=0,sticky=W)
		entryref = ttk.Entry(labelframeleft,width=30,font=("times new roman",13,"bold"))
		entryref.grid(row=0,column=1)		


		lblcname = Label(labelframeleft,text = "Customer Name",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblcname.grid(row=1,column=0,sticky=W)
		entrycname = ttk.Entry(labelframeleft,width=30,font=("times new roman",13,"bold"))
		entrycname.grid(row=1,column=1)		


		lblmname = Label(labelframeleft,text = "Mother Name",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblmname.grid(row=2,column=0,sticky=W)
		entrymname = ttk.Entry(labelframeleft,width=30,font=("times new roman",13,"bold"))
		entrymname.grid(row=2,column=1)		

		lblgender = Label(labelframeleft,text = "Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblgender.grid(row=3,column=0,sticky=W)
		combogender = ttk.Combobox(labelframeleft,width=29,font=("times new roman",13,"bold"),state="readonly")
		combogender["values"]=("Male","Female","Other")
		combogender.current(0)
		combogender.grid(row=3,column=1)

		lblpost = Label(labelframeleft,text = "Postcode",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblpost.grid(row=4,column=0,sticky=W)
		entrypost = ttk.Entry(labelframeleft,width=30,font=("times new roman",13,"bold"))
		entrypost.grid(row=4,column=1)		

		lblmobile = Label(labelframeleft,text = "Mobile",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblmobile.grid(row=5,column=0,sticky=W)
		entrymobile = ttk.Entry(labelframeleft,width=30,font=("times new roman",13,"bold"))
		entrymobile.grid(row=5,column=1)		

		lblemail = Label(labelframeleft,text = "Email",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblemail.grid(row=6,column=0,sticky=W)
		entryemail = ttk.Entry(labelframeleft,width=30,font=("times new roman",13,"bold"))
		entryemail.grid(row=6,column=1)		

		lblnationality = Label(labelframeleft,text = "Nationality",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblnationality.grid(row=7,column=0,sticky=W)
		combonationality = ttk.Combobox(labelframeleft,width=29,font=("times new roman",13,"bold"),state="readonly")
		combonationality["values"]=("Indian","Other")
		combonationality.current(0)
		combonationality.grid(row=7,column=1)

		lblidproof = Label(labelframeleft,text = "ID Proof",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblidproof.grid(row=8,column=0,sticky=W)
		comboidproof = ttk.Combobox(labelframeleft,width=29,font=("times new roman",13,"bold"),state="readonly")
		comboidproof["values"]=("Adhar","Voter","Passport","Driving")
		comboidproof.current(0)
		comboidproof.grid(row=8,column=1)

		lblidnum = Label(labelframeleft,text = "Id Number",font=("times new roman",12,"bold"),padx=2,pady=6)
		lblidnum.grid(row=9,column=0,sticky=W)
		entryidnum = ttk.Entry(labelframeleft,width=30,font=("times new roman",13,"bold"))
		entryidnum.grid(row=9,column=1)		

		lbladdress = Label(labelframeleft,text = "Address",font=("times new roman",12,"bold"),padx=2,pady=6)
		lbladdress.grid(row=10,column=0,sticky=W)
		entryaddress = ttk.Entry(labelframeleft,width=30,font=("times new roman",13,"bold"))
		entryaddress.grid(row=10,column=1)		

		#=================================btn frame========================================
		btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
		btn_frame.place(x=0,y=390,width=412,height=40)

		btnadd = Button(btn_frame,width=9,text="ADD",font=("times new roman",12,"bold"),bg="black",fg="gold")
		btnadd.grid(row=0,column=0,padx=1)

		btnupdate = Button(btn_frame,width=9,text="UPDATE",font=("times new roman",12,"bold"),bg="black",fg="gold")
		btnupdate.grid(row=0,column=1,padx=1)

		btndelete = Button(btn_frame,width=9,text="DELETE",font=("times new roman",12,"bold"),bg="black",fg="gold")
		btndelete.grid(row=0,column=2,padx=1)

		btnreset = Button(btn_frame,width=9,text="RESET",font=("times new roman",12,"bold"),bg="black",fg="gold")
		btnreset.grid(row=0,column=3,padx=1)

		#============================= table frame =====================================
		labelframeright = LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("times new roman",12,"bold"))
		labelframeright.place(x=435,y=50,width=700,height=490)

		lblsearch = Label(labelframeright,text = "Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
		lblsearch.grid(row=0,column=0,sticky=W,padx=1)
		combosearch = ttk.Combobox(labelframeright,width=24,font=("times new roman",12,"bold"),state="readonly")
		combosearch["values"]=("Mobile","Ref No")
		combosearch.current(0)
		combosearch.grid(row=0,column=1,padx=1)
		
		entrysearch = ttk.Entry(labelframeright,width=23,font=("times new roman",12,"bold"))
		entrysearch.grid(row=0,column=2,padx=1)		
		
		btnsearch = Button(labelframeright,width=8,text="Search",font=("times new roman",12,"bold"),bg="black",fg="gold")
		btnsearch.grid(row=0,column=3,padx=1)

		btnshowall = Button(labelframeright,width=8,text="Show All",font=("times new roman",12,"bold"),bg="black",fg="gold")
		btnshowall.grid(row=0,column=4,padx=1)

		#=================================== show data table =======================================
		tbldetail = LabelFrame(labelframeright,bd=2,relief=RIDGE)
		tbldetail.place(x=0,y=50,width=700,height=350)

		scroll_x = ttk.Scrollbar(tbldetail,orient=HORIZONTAL)
		scroll_y = ttk.Scrollbar(tbldetail,orient=VERTICAL)

		self.Cust_Tbl = ttk.Treeview(tbldetail,column = ("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.Cust_Tbl.xview)
		scroll_y.config(command=self.Cust_Tbl.yview)

		self.Cust_Tbl.heading("ref",text="Ref No")
		self.Cust_Tbl.heading("name",text="Name")
		self.Cust_Tbl.heading("mother",text="Mother Name")
		self.Cust_Tbl.heading("gender",text="Gender")
		self.Cust_Tbl.heading("post",text="Post")
		self.Cust_Tbl.heading("mobile",text="Mobile")
		self.Cust_Tbl.heading("email",text="Email")
		self.Cust_Tbl.heading("nationality",text="Nationality")
		self.Cust_Tbl.heading("idproof",text="Id Proof")
		self.Cust_Tbl.heading("idnumber",text="Id Number")
		self.Cust_Tbl.heading("address",text="Address")

		self.Cust_Tbl["show"] = "headings"
		
		self.Cust_Tbl.column("ref",width=100)
		self.Cust_Tbl.column("name",width=100)
		self.Cust_Tbl.column("mother",width=100)
		self.Cust_Tbl.column("gender",width=100)
		self.Cust_Tbl.column("post",width=100)
		self.Cust_Tbl.column("mobile",width=100)
		self.Cust_Tbl.column("email",width=100)
		self.Cust_Tbl.column("nationality",width=100)
		self.Cust_Tbl.column("idproof",width=100)
		self.Cust_Tbl.column("idnumber",width=100)
		self.Cust_Tbl.column("address",width=100)

		self.Cust_Tbl.pack(fill=BOTH,expand=1)



if __name__ == '__main__':
	root = Tk()
	obj = Roombooking(root)
	root.mainloop()
