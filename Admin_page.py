import tkinter
from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Admin:

    def __init__(self, root):
        self.root = root
        self.root.title("Admin Page")
        self.root.geometry("1350x1000+0+0")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/cap.png")
        self.back_image = ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Documents/PRIYANKA FOLDER/bckk.png")

        self.bg_image = Label(self.root, image=self.bg, compound=TOP).place(x=0, y=0)
        # self.bckk_image = Label(image=self.back_image).place(x=20, y=320)
        # self.background = ImageTk.PhotoImage(file="C:/Users/hp/Documents/PRIYANKA FOLDER/img.png")
        # self.back = Label(self.root, image=self.background).place(x=0, y=350,relwidth=1, relheight=1)

        Frame_1 = Frame(self.root, bg="white")
        Frame_1.place(x=0, y=150, height=1350, width=1350)
        self.bckk_image = Label(Frame_1, image=self.back_image).place(x=0, y=0)
        b1 = Button(self.root, text="View Users", fg="black", bg="lightgray", font=("times new roman", 25)).place(x=0, y=150,width=240,height=80)

        b2 = Button(self.root, text="Add to Blacklist", command=self.blacklist, fg="black", bg="lightgray",
                    font=("times new roman", 25)).place(x=360, y=150, width=240, height=80)
        b3 = Button(self.root, text="View List", command=self.list_website, fg="black", bg="lightgray",
                    font=("times new roman", 25)).place(x=695, y=150, width=240, height=80)
        b4 = Button(self.root, text="Log out", command=self.logout, fg="black", bg="lightgray",
                    font=("times new roman", 25)).place(x=1020, y=150, width=240, height=80)
        lbl1 = Label(Frame_1, text="USERS LIST", font=("times new roman", 20, "bold"), bg="white").place(x=550, y=140,
                                                                                                         width=200)
        connect = pymysql.connect(host="localhost", user="root", password="hey_admin_root", database="employee")
        conn = connect.cursor()
        conn.execute("select * from emp")
        self.tree = ttk.Treeview(Frame_1)
        self.tree['show'] = 'headings'
        self.s = ttk.Style(Frame_1)
        self.s.theme_use("clam")
        self.s.configure(".", font=('Helvetica', 11))
        self.s.configure("Treeview.Heading", foreground='blue', font=('Helvetica', 11, "bold"))
        self.tree['columns'] = ("id", "f_name", "l_name", "contact", "Email", "question", "answer")

        self.tree.column("id", width=100, minwidth=100, anchor=tkinter.CENTER)
        self.tree.column("f_name", width=100, minwidth=100, anchor=tkinter.CENTER)
        self.tree.column("l_name", width=100, minwidth=100, anchor=tkinter.CENTER)
        self.tree.column("contact", width=150, minwidth=150, anchor=tkinter.CENTER)
        self.tree.column("Email", width=200, minwidth=150, anchor=tkinter.CENTER)
        self.tree.column("question", width=200, minwidth=200, anchor=tkinter.CENTER)
        self.tree.column("answer", width=200, minwidth=200, anchor=tkinter.CENTER)

        self.tree.heading("id", text="Student ID", anchor=tkinter.CENTER)
        self.tree.heading("f_name", text="First Name", anchor=tkinter.CENTER)
        self.tree.heading("l_name", text="Last Name", anchor=tkinter.CENTER)
        self.tree.heading("contact", text="Contact", anchor=tkinter.CENTER)
        self.tree.heading("Email", text="Email", anchor=tkinter.CENTER)
        self.tree.heading("question", text="Question", anchor=tkinter.CENTER)
        self.tree.heading("answer", text="Answer", anchor=tkinter.CENTER)

        i = 0
        for ro in conn:
            self.tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))
            i = i + 1
        self.tree.place(x=100, y=200)

    def clear(self):
        self.entry1.delete(0, END)

    def log(self):
        if self.entry1.get() == "":
            messagebox.showerror("Error", "Please enter an URL", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="hey_admin_root", database="employee")
                cur = con.cursor()
                cur.execute("select * from url where url=%s", (self.entry1.get()))
                row = cur.fetchone()

                cur.execute("insert into url (url) values(%s)",
                            (self.entry1.get()))
                con.commit()
                con.close()
                messagebox.showinfo("successfull", "URL added successfully")
                self.clear()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def blacklist(self):
        Frame_2 = Frame(bg="white")
        Frame_2.place(x=0, y=250, height=1350, width=1350)
        self.second_image = Label(Frame_2, image=self.back_image).place(x=0, y=0)

        lbl1 = Label(Frame_2, text="Add to Blacklist", font=("times new roman", 20, "bold"), bg="white").place(x=680,
                                                                                                               y=80)
        lbl2 = Label(Frame_2, text="URL", fg="#154c79", font=("times new roman", 18, "bold"), bg="white").place(x=440,
                                                                                                                y=170)
        self.entry1 = Entry(Frame_2, font=("times new roman", 20), bg="lightgray")
        self.entry1.place(x=550, y=170, width=490)
        btn1 = Button(Frame_2, text="Submit", command=self.log, font=("times new roman", 20), bg="black",
                      fg="white").place(x=680, y=260, width=130, height=48)

    def list_website(self):
        Frame_3 = Frame(bg="white")
        Frame_3.place(x=1, y=250, height=1350, width=1350)
        self.third_image = Label(Frame_3, image=self.back_image).place(x=0, y=0)
        lbl1 = Label(Frame_3, text="Blacklisted Websites", font=("times new roman", 20, "bold"), bg="white").place(
            x=610, y=75, width=300)
        connect = pymysql.connect(host="localhost", user="root", password="hey_admin_root", database="employee")
        conn = connect.cursor()
        conn.execute("select * from url")
        self.tree = ttk.Treeview(Frame_3)
        self.tree['show'] = 'headings'
        self.s = ttk.Style(Frame_3)
        self.s.theme_use("clam")
        self.s.configure(".", font=('Helvetica', 11))
        self.s.configure("Treeview.Heading", foreground='blue', font=('Helvetica', 11, "bold"))
        self.tree['columns'] = ("id", "url")

        self.tree.column("id", width=100, minwidth=100, anchor=tkinter.CENTER)
        self.tree.column("url", width=600, minwidth=00, anchor=tkinter.CENTER)

        self.tree.heading("id", text="Sr. No.", anchor=tkinter.CENTER)
        self.tree.heading("url", text="Phishing URLs", anchor=tkinter.CENTER)

        i = 0
        for ro in conn:
            self.tree.insert('', i, text="", values=(ro[0], ro[1]))
            i = i + 1
        self.tree.place(x=370, y=150)

    def logout(self):
        self.root.destroy()
        # noinspection PyUnresolvedReferences
        import userlogin_adminlogin_page




root = Tk()
obj = Admin(root)
root.mainloop()



