import threading
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")
        # Set fullscreen
        self.root.attributes("-fullscreen", True)

        self.bg = PhotoImage(file=r"D:/0df675008d1b42f693786ddcd4e2fe22.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1=Image.open(r"D:\Downloads\contact-image-icon-11.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
#label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
         

        Password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        Password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        #===============ICOn image======================
        img2=Image.open(r"D:\Downloads\contact-image-icon-11.jpg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        
        img3=Image.open(r"D:\Downloads\icons8-password-48.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
 


# loginButton

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)


# registerButton
        registerbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"),
                     borderwidth=0, fg="white", bg="black",
                     activeforeground="white", activebackground="black",
                     command=self.open_register_window)
        registerbtn.place(x=20, y=350, width=160)

# forgetpassbtn
        forgetpassbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"),
                       borderwidth=0, fg="white", bg="black",
                       activeforeground="white", activebackground="black",
                       command=self.open_forget_password_window)
        forgetpassbtn.place(x=10, y=370, width=160)



    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="login"
                )
                cur = conn.cursor()
                cur.execute(
                    "SELECT * FROM users WHERE email=%s AND password=%s",
                    (self.txtuser.get(), self.txtpass.get())
                )
                row = cur.fetchone()
                if row:
                    messagebox.showinfo("Success", "Login Successful")
                else:
                    messagebox.showerror("Error", "Invalid username or password")
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}")


    def open_register_window(self):
        reg_win = Toplevel(self.root)
        reg_win.title("Register")
        # Set fixed size and center the window (not fullscreen)
        window_width = 800
        window_height = 600
        screen_width = reg_win.winfo_screenwidth()
        screen_height = reg_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        reg_win.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
        reg_win.grab_set()

        # Variables
        var_fname = StringVar()
        var_lname = StringVar()
        var_contact = StringVar()
        var_email = StringVar()
        var_security_q = StringVar()
        var_security_a = StringVar()
        var_password = StringVar()
        var_cpassword = StringVar()
        var_check = IntVar()

        # Background Image
        bg = ImageTk.PhotoImage(file="D:\\Downloads\\pexels-thisisengineering-3861969.jpg", master=reg_win)
        bg_lbl = Label(reg_win, image=bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        reg_win.bg = bg  # Prevent garbage collection

        # Left Image
        left = ImageTk.PhotoImage(file="D:\\Downloads\\artificial-intelligence-brain-circuitry.jpg", master=reg_win)
        left_lbl = Label(reg_win, image=left)
        left_lbl.place(x=50, y=100, width=470, height=500)
        reg_win.left = left

        # Main Frame
        frame = Frame(reg_win, bg="white")
        frame.place(x=520, y=100, width=800, height=500)

        Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white").place(x=20, y=20)
        Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="red").place(x=20, y=70)
        Entry(frame, textvariable=var_fname, font=("times new roman", 15)).place(x=20, y=100, width=250)
        Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white").place(x=400, y=70)
        Entry(frame, textvariable=var_lname, font=("times new roman", 15)).place(x=400, y=100, width=250)
        Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white").place(x=20, y=150)
        Entry(frame, textvariable=var_contact, font=("times new roman", 15)).place(x=20, y=180, width=250)
        Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="red").place(x=400, y=150)
        Entry(frame, textvariable=var_email, font=("times new roman", 15)).place(x=400, y=180, width=250)
        Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="red").place(x=20, y=230)
        combo_security_q = ttk.Combobox(frame, textvariable=var_security_q, font=("times new roman", 15), state="readonly")
        combo_security_q["values"] = ("Select", "Your Birth Place", "Your Best Friend", "Your Pet Name")
        combo_security_q.current(0)
        combo_security_q.place(x=20, y=260, width=250)
        Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="red").place(x=400, y=230)
        Entry(frame, textvariable=var_security_a, font=("times new roman", 15)).place(x=400, y=260, width=250)
        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="red").place(x=20, y=310)
        Entry(frame, textvariable=var_password, font=("times new roman", 15), show="*").place(x=20, y=340, width=250)
        Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="red").place(x=400, y=310)
        Entry(frame, textvariable=var_cpassword, font=("times new roman", 15), show="*").place(x=400, y=340, width=250)
        Checkbutton(frame, text="I Agree The Terms & Conditions", font=("times new roman", 13, "bold"), bg="white",
                    variable=var_check, onvalue=1, offvalue=0).place(x=20, y=380)

        img = Image.open(r"D:\Downloads\register-button-png-18469.png")
        img = img.resize((200, 50), Image.LANCZOS)
        btn_reg_img = ImageTk.PhotoImage(img, master=reg_win)
        reg_win.btn_reg_img = btn_reg_img
        Button(frame, image=btn_reg_img, borderwidth=0, cursor="hand2", command=lambda: register_data()).place(x=50, y=420)

        img1 = Image.open(r"D:\Downloads\0beffd75571aee0a45f458116e5cf1ae.png")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        btn_login_img = ImageTk.PhotoImage(img1, master=reg_win)
        reg_win.btn_login_img = btn_login_img
        Button(frame, image=btn_login_img, borderwidth=0, cursor="hand2", command=reg_win.destroy).place(x=350, y=420)

        def register_data():
            def db_task():
                if var_fname.get() == "" or var_email.get() == "" or var_security_q.get() == "Select":
                    messagebox.showerror("Error", "All fields are required", parent=reg_win)
                elif var_password.get() != var_cpassword.get():
                    messagebox.showerror("Error", "Password and Confirm Password must be same", parent=reg_win)
                elif var_check.get() == 0:
                    messagebox.showerror("Error", "Please agree to the terms and conditions", parent=reg_win)
                else:
                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="login",
                            connection_timeout=5
                        )
                        cur = conn.cursor()
                        cur.execute("SELECT * FROM users WHERE email=%s", (var_email.get(),))
                        row = cur.fetchone()
                        if row:
                            messagebox.showerror("Error", "User already exists, please try another email", parent=reg_win)
                        else:
                            cur.execute(
                                "INSERT INTO users (firstname, lastname, contact, email, security_q, security_a, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                (
                                    var_fname.get(),
                                    var_lname.get(),
                                    var_contact.get(),
                                    var_email.get(),
                                    var_security_q.get(),
                                    var_security_a.get(),
                                    var_password.get()
                                )
                            )
                            conn.commit()
                            messagebox.showinfo("Success", "Registration Successful", parent=reg_win)
                            reg_win.destroy()
                        conn.close()
                    except Exception as e:
                        messagebox.showerror("Error", f"Error due to: {str(e)}", parent=reg_win)
            threading.Thread(target=db_task).start()

    def open_forget_password_window(self):
        fp_win = Toplevel(self.root)
        fp_win.title("Forgot Password")
        # Remove fullscreen, set fixed size and center the window
        window_width = 400
        window_height = 300
        screen_width = fp_win.winfo_screenwidth()
        screen_height = fp_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        fp_win.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
        fp_win.grab_set()

        email = StringVar()
        new_password = StringVar()
        confirm_password = StringVar()

        # Remove fg="red" for neutral color (default is black)
        Label(fp_win, text="Enter your registered Email").pack(pady=10)
        Entry(fp_win, textvariable=email).pack()
        Label(fp_win, text="New Password").pack(pady=10)
        Entry(fp_win, textvariable=new_password).pack()
        Label(fp_win, text="Confirm Password").pack(pady=10)
        Entry(fp_win, textvariable=confirm_password).pack()

        def reset_password():
            if not email.get() or not new_password.get() or not confirm_password.get():
                messagebox.showerror("Error", "All fields are required", parent=fp_win)
            elif new_password.get() != confirm_password.get():
                messagebox.showerror("Error", "Passwords do not match", parent=fp_win)
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="login"
                    )
                    cur = conn.cursor()
                    cur.execute("SELECT  FROM users WHERE email=%s", (email.get(),))
                    if not cur.fetchone():
                        messagebox.showerror("Error", "Email not registered", parent=fp_win)
                    else:
                        cur.execute("UPDATE users SET password=%s WHERE email=%s", (new_password.get(), email.get()))
                        conn.commit()
                        messagebox.showinfo("Success", "Password reset successful", parent=fp_win)
                        fp_win.destroy()
                    conn.close()
                except Exception as e:
                    messagebox.showerror("Error", f"Error: {str(e)}", parent=fp_win)

        Button(fp_win, text="Reset Password", command=reset_password).pack(pady=20)

    def open_login_page(self):
        login_win = Toplevel(self.root)
        login_win.title("Login Page")
        # Set fixed size and center the window (not fullscreen)
        window_width = 400
        window_height = 300
        screen_width = login_win.winfo_screenwidth()
        screen_height = login_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        login_win.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
        login_win.grab_set()

        var_email = StringVar()
        var_password = StringVar()
        show_password = IntVar(value=0)

        Label(login_win, text="Login", font=("times new roman", 18, "bold")).pack(pady=10)
        Label(login_win, text="Email").pack(pady=5)
        Entry(login_win, textvariable=var_email).pack()
        Label(login_win, text="Password").pack(pady=5)
        password_entry = Entry(login_win, textvariable=var_password, show="*")
        password_entry.pack()

        def toggle_password():
            if show_password.get():
                password_entry.config(show="")
            else:
                password_entry.config(show="*")

        Checkbutton(login_win, text="Show Password", variable=show_password, command=toggle_password).pack(pady=5)

        def do_login():
            if not var_email.get() or not var_password.get():
                messagebox.showerror("Error", "All fields are required", parent=login_win)
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="login"
                    )
                    cur = conn.cursor()
                    cur.execute(
                        "SELECT * FROM users WHERE email=%s AND password=%s",
                        (var_email.get(), var_password.get())
                    )
                    row = cur.fetchone()
                    if row:
                        messagebox.showinfo("Success", "Login Successful", parent=login_win)
                        login_win.destroy()
                    else:
                        messagebox.showerror("Error", "Invalid username or password", parent=login_win)
                    conn.close()
                except Exception as e:
                    messagebox.showerror("Error", f"Error due to: {str(e)}", parent=login_win)

        Button(login_win, text="Login", command=do_login).pack(pady=20)

    def open_register_page(self):
        reg_win = Toplevel(self.root)
        reg_win.title("Register Page")
        # Set fixed size and center the window (not fullscreen)
        window_width = 500
        window_height = 500
        screen_width = reg_win.winfo_screenwidth()
        screen_height = reg_win.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        reg_win.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
        reg_win.grab_set()

        var_fname = StringVar()
        var_lname = StringVar()
        var_contact = StringVar()
        var_email = StringVar()
        var_security_q = StringVar()
        var_security_a = StringVar()
        var_password = StringVar()
        var_cpassword = StringVar()
        var_check = IntVar()

        Label(reg_win, text="Register", font=("times new roman", 18, "bold")).pack(pady=10)
        Label(reg_win, text="First Name").pack()
        Entry(reg_win, textvariable=var_fname).pack()
        Label(reg_win, text="Last Name").pack()
        Entry(reg_win, textvariable=var_lname).pack()
        Label(reg_win, text="Contact No").pack()
        Entry(reg_win, textvariable=var_contact).pack()
        Label(reg_win, text="Email").pack()
        Entry(reg_win, textvariable=var_email).pack()
        Label(reg_win, text="Select Security Question").pack()
        combo_security_q = ttk.Combobox(reg_win, textvariable=var_security_q, state="readonly")
        combo_security_q["values"] = ("Select", "Your Birth Place", "Your Best Friend", "Your Pet Name")
        combo_security_q.current(0)
        combo_security_q.pack()
        Label(reg_win, text="Security Answer").pack()
        Entry(reg_win, textvariable=var_security_a).pack()
        Label(reg_win, text="Password").pack()
        Entry(reg_win, textvariable=var_password, show="*").pack()
        Label(reg_win, text="Confirm Password").pack()
        Entry(reg_win, textvariable=var_cpassword, show="*").pack()
        Checkbutton(reg_win, text="I Agree The Terms & Conditions", variable=var_check, onvalue=1, offvalue=0).pack(pady=5)

        def register_data():
            if var_fname.get() == "" or var_email.get() == "" or var_security_q.get() == "Select":
                messagebox.showerror("Error", "All fields are required", parent=reg_win)
            elif var_password.get() != var_cpassword.get():
                messagebox.showerror("Error", "Password and Confirm Password must be same", parent=reg_win)
            elif var_check.get() == 0:
                messagebox.showerror("Error", "Please agree to the terms and conditions", parent=reg_win)
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="login"
                    )
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM users WHERE email=%s", (var_email.get(),))
                    row = cur.fetchone()
                    if row:
                        messagebox.showerror("Error", "User already exists, please try another email", parent=reg_win)
                    else:
                        cur.execute(
                            "INSERT INTO users (firstname, lastname, contact, email, security_q, security_a, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (
                                var_fname.get(),
                                var_lname.get(),
                                var_contact.get(),
                                var_email.get(),
                                var_security_q.get(),
                                var_security_a.get(),
                                var_password.get()
                            )
                        )
                        conn.commit()
                        messagebox.showinfo("Success", "Registration Successful", parent=reg_win)
                        reg_win.destroy()
                    conn.close()
                except Exception as e:
                    messagebox.showerror("Error", f"Error due to: {str(e)}", parent=reg_win)

        Button(reg_win, text="Register", command=register_data).pack(pady=20)

if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root) 
    root.mainloop()