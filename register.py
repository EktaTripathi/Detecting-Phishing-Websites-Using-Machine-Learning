from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x900+0+0")
        self.root.resizable(False, False)
        self.root.config(bg="white")
        #=======Images=======
        self.bg=ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/bckk.png")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)


        #=====left image=====
        self.left=ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/unnamed.png")
        left=Label(self.root,image=self.left).place(x=80,y=150,width=400,height=500)

        #=====Register frame======
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=150,width=700,height=500)

        title=Label(frame1, text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="#063970").place(x=50,y=30)



        f_name=Label(frame1, text="First Name",font=("times new roman",15,"bold"),bg="white").place(x=50,y=80)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=110,width=250)


        l_name=Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white").place( x=370, y=80)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=110, width=250)


        contact=Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=150)
        self.txt_contact= Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=180, width=250)


        Email= Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white").place( x=370, y=150)
        self.txt_Email= Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_Email.place(x=370, y=180, width=250)


        question= Label(frame1, text="Security Questions", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=220)
        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name",)
        self.cmb_quest.place(x=50, y=250, width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white").place(x=370,y=220)
        self.txt_answer= Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=250, width=250)

        password= Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=290)
        self.txt_password= Entry(frame1,show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=320, width=250)

        cpassword=Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=290)
        self.txt_cpassword = Entry(frame1,show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=320, width=250)

        self.var_chk=IntVar()
        chk = Checkbutton(frame1, text="I agree The terms & conditions",variable=self.var_chk, onvalue=1, offvalue=0, bg="white",font=("times new roman", 12, "bold")).place(x=50, y=360)

        self.btn_image = ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/register (1).png")
        btn_register = Button(frame1, image=self.btn_image, bd=0, cursor="hand2", command=self.register_data).place(x=50, y=390)

        sign_in = Label(frame1, text="Already have an account?", font=("times new roman", 12, "bold"),bg="white").place(x=50, y=460)
        btn_login = Button(frame1, text="Sign In",command=self.login_window,font=("Georgia", 12), bd=0, cursor="hand2", bg="#103A76",fg="white").place(x=230, y=458, width=100)


    def login_window(self):
        self.root.destroy()
        # noinspection PyUnresolvedReferences
        import userlogin_adminlogin_page


    def claer(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_Email.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.txt_answer.delete(0, END)
        self.cmb_quest.current(0)
        self.var_chk.set(0)
        self.txt_fname.focus()

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get() == "" or self.txt_contact.get()=="" or self.txt_Email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should be match", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please agree our Terms & Conditions", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="hey_admin_root",database="employee")
                cur=con.cursor()
                cur.execute("select * from emp where email=%s",self.txt_Email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error", "User already exist please try with another Email id", parent=self.root)
                else:
                    cur.execute("insert into emp (f_name,l_name,contact,Email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_Email.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successful",parent=self.root)
                    self.claer()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)
            #messagebox.showinfo("Success","Register Successful",parent=self.root)





root=Tk()
obj=Register(root)
root.mainloop()


