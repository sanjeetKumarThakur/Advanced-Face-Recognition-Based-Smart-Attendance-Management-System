from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1500x900+0+0")

        # ================== VARIABLES ==================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()

        # ================= Background Image =================
        self.bg = ImageTk.PhotoImage(
            file="D:\\Downloads\\pexels-thisisengineering-3861969.jpg",
            master=self.root
        )
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ================= Left Image =================
        self.left = ImageTk.PhotoImage(
            file="D:\\Downloads\\artificial-intelligence-brain-circuitry.jpg",
            master=self.root
        )
        left_lbl = Label(self.root, image=self.left)
        left_lbl.place(x=50, y=100, width=470, height=500)

        # ================= Main Frame =================
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=500)

        Label(
            frame,
            text="REGISTER HERE",
            font=("times new roman", 20, "bold"),
            fg="green",
            bg="white"
        ).place(x=20, y=20)

        # ================= First Name =================
        Label(frame, text="First Name",
              font=("times new roman", 15, "bold"),
              bg="white").place(x=20, y=70)

        Entry(frame, textvariable=self.var_fname,
              font=("times new roman", 15)).place(x=20, y=100, width=250)

        # ================= Last Name =================
        Label(frame, text="Last Name",
              font=("times new roman", 15, "bold"),
              bg="white").place(x=400, y=70)

        Entry(frame, textvariable=self.var_lname,
              font=("times new roman", 15)).place(x=400, y=100, width=250)

        # ================= Contact =================
        Label(frame, text="Contact No",
              font=("times new roman", 15, "bold"),
              bg="white").place(x=20, y=150)

        Entry(frame, textvariable=self.var_contact,
              font=("times new roman", 15)).place(x=20, y=180, width=250)

        # ================= Email =================
        Label(frame, text="Email",
              font=("times new roman", 15, "bold"),
              bg="white").place(x=400, y=150)

        Entry(frame, textvariable=self.var_email,
              font=("times new roman", 15)).place(x=400, y=180, width=250)

        # ================= Security Question =================
        Label(frame, text="Select Security Question",
              font=("times new roman", 15, "bold"),
              bg="white").place(x=20, y=230)

        combo_security_q = ttk.Combobox(
            frame,
            textvariable=self.var_security_q,
            font=("times new roman", 15),
            state="readonly"
        )
        combo_security_q["values"] = (
            "Select",
            "Your Birth Place",
            "Your Best Friend",
            "Your Pet Name"
        )
        combo_security_q.current(0)
        combo_security_q.place(x=20, y=260, width=250)

        # ================= Security Answer =================
        Label(frame, text="Security Answer",
              font=("times new roman", 15, "bold"),
              bg="white").place(x=400, y=230)

        Entry(frame, textvariable=self.var_security_a,
              font=("times new roman", 15)).place(x=400, y=260, width=250)

        # ================= Password =================
        Label(frame, text="Password",
              font=("times new roman", 15, "bold"),
              bg="white").place(x=20, y=310)

        Entry(frame, textvariable=self.var_password,
              font=("times new roman", 15),
              show="*").place(x=20, y=340, width=250)

        # ================= Confirm Password =================
        Label(frame, text="Confirm Password",
              font=("times new roman", 15, "bold"),
              bg="white").place(x=400, y=310)

        Entry(frame, textvariable=self.var_cpassword,
              font=("times new roman", 15),
              show="*").place(x=400, y=340, width=250)

        # ================= Terms & Conditions =================
        Checkbutton(
            frame,
            text="I Agree The Terms & Conditions",
            font=("times new roman", 13, "bold"),
            bg="white"
        ).place(x=20, y=380)

        # ================= Register Button =================
        img = Image.open(r"D:\Downloads\register-button-png-18469.png")
        img = img.resize((200, 50), Image.LANCZOS)
        self.btn_reg_img = ImageTk.PhotoImage(img, master=self.root)

        Button(frame, image=self.btn_reg_img,
               borderwidth=0, cursor="hand2").place(x=50, y=420)

        # ================= Login Button =================
        img1 = Image.open(r"D:\Downloads\0beffd75571aee0a45f458116e5cf1ae.png")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        self.btn_login_img = ImageTk.PhotoImage(img1, master=self.root)

        Button(frame, image=self.btn_login_img,
               borderwidth=0, cursor="hand2").place(x=350, y=420)
        #=============function declaration===============
        def register_data(self):
            if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security_q.get() == "Select":
                messagebox.showerror("Error", "All fields are required")
            elif self.var_password.get() != self.var_cpassword.get():
                messagebox.showerror("Error", "Password and Confirm Password must be same")
            elif self.var_check.get() == 0:
                messagebox.showerror("Error", "Please agree to the terms and conditions")
            else:
                # Here you would add the actual registration logic
                messagebox.showinfo("Success", "welcome Successful")

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
