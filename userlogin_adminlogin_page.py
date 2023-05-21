from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1350x900+0+0")
        self.root.resizable(False, False)
        #=======BG Image==================
        self.bg = ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/types-of-phishing-attacks.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #======Login Frame=======


        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)


        #===========Images============
        self.user_icon = ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/user.png")
        self.pass_icon = ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/pass.png")
        self.ad_icon = ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/admin_icon.png")
        self.log_icon = ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/log_user.png")

        #========user login=========
        Frame_user=Frame(self.root, bg="white")
        Frame_user.place(x=730, y=150, height=340, width=500)

        title_user=Label(Frame_user,image=self.log_icon, font=("Algerian",10, "bold"), fg="#000000", bg="#8bd3e1",bd=0).place(x=170, y=10)
        desc_user=Label(Frame_user, text="User Area", font=("Georgia", 14, "bold","underline"), fg="#000000",bg="white").place(x=170, y=113)

        log_user= Label(Frame_user, text="Email ID", image=self.user_icon, compound=LEFT,font=("Georgia", 19, "bold"), fg="#154c79", bg="white").place(x=90, y=140)
        self.txt_loguser=Entry(Frame_user, font=("times new roman", 15), bg="lightgray")
        self.txt_loguser.place(x=90, y=173, width=350, height=35)

        log_user = Label(Frame_user, text="Password", image=self.user_icon, compound=LEFT, font=("Georgia", 19, "bold"),fg="#154c79", bg="white").place(x=90, y=210)
        self.txt_userpass = Entry(Frame_user,show="*",font=("times new roman", 15), bg="lightgray")
        self.txt_userpass.place(x=90, y=245, width=350, height=35)

        userlogin_btn=Button(self.root,text="Login",command=self.login, fg="white",cursor="hand2", bg="#154c79",font=("times new roman", 20)).place(x=890, y=470, width=180, height=40)

        btn_regiser=Button(Frame_user,command=self.register_window,text="Don't have an account? Create an account",font=("times new roman",13,),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=90,y=288)

    










        #============Admin Login========================
        title = Label(Frame_login, image=self.ad_icon, font=("Algerian", 10, "bold"), fg="#000000", bg="#c5d6dd").place(x=190, y=10)
        desc = Label(Frame_login, text="Admin Login ", font=("Georgia", 14, "bold","underline"), fg="#000000", bg="white",bd=0).place(x=170, y=113)

        lbl_user = Label(Frame_login, text="Username",image=self.user_icon,compound=LEFT,font=("Georgia", 19, "bold"), fg="#154c79",bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_login,font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=173, width=350, height=35)

        lbl_pass = Label(Frame_login, text="Password",image=self.pass_icon,compound=LEFT,font=("Georgia", 19, "bold"), fg="#154c79", bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=245, width=350, height=35)

        #forget_btn = Button(Frame_login,cursor="hand2",text="Forget Password?", bg="white", fg="#154c79", bd=0,font=("times new roman", 12)).place(x=90, y=280)
        Login_btn = Button(self.root,cursor="hand2",command=self.login_function, text="Login", fg="white", bg="#154c79",font=("times new roman", 20)).place(x=300, y=470, width=180, height=40)




    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get()!= "admin" or self.txt_user.get()!= "admin":
                messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}",parent=self.root)
            self.root.destroy()
            #noinspection PyUnresolvedReferences
            import Admin_page



    def register_window(self):
        self.root.destroy()
        # noinspection PyUnresolvedReferences
        import register


    def login(self):
        if self.txt_loguser.get()== "" or self.txt_userpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="hey_admin_root",database="employee")
                cur=con.cursor()
                cur.execute("select * from emp where Email=%s and password=%s",(self.txt_loguser.get(),self.txt_userpass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD")

                else:
                    messagebox.showinfo("Success","Welcome")
                    self.root.destroy()
                    import Main
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}")



root = Tk()
obj = Login(root)
root.mainloop()





