from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import re
import mysql.connector

# import libraries for price prediction

import numpy as np
import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

wp = Tk()
wp.title("House Price Prediction & Loan Prediction")
wp.geometry("1600x900+0+0")

# check image path
bgimage = ImageTk.PhotoImage(Image.open(r"Images\wellcome_img.jpg"))
wp.configure(background="black")

img = Label(wp, image=bgimage)
img.place(x=0, y=0)
val=0

def t_and_c(event=None):
    tc_frame = Frame(wr, bg="grey")
    tc_frame.place(x=480, y=100, width=700, height=500)

    close_fg = Button(tc_frame, text="X", font=(8), bg="grey", fg="white",
                      relief=GROOVE, justify=CENTER,
                      width=4, bd=0, command=tc_frame.destroy).place(x=650, y=2)

    my_text = Text(tc_frame, height=40, width=10, font=('Arial', 12))
    my_text.config(wrap='word', relief=FLAT)
    my_text.pack(pady=30, expand=True, fill=BOTH)
    url = "Terms-and-Conditions.txt"
    with open(url, 'rb') as for_read:
        my_text.insert(1.0, for_read.read())
        for_read.close()
    scroll = Scrollbar(my_text)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=my_text.yview)
    my_text.config(yscrollcommand=scroll.set)
    my_text.configure(state="disabled")


a=[0]
def eye():
    if a[-1]==0:
        txt_passwod.configure(show="")
        a.append(1)
    elif a[-1]==1:
        txt_passwod.configure(show="*")
        a.append(0)


b=[0]
def c_eye():
    if b[-1]==0:
        txt_conpassword.configure(show="")
        b.append(1)
    elif b[-1]==1:
        txt_conpassword.configure(show="*")
        b.append(0)


# ---------register wellcome button

def reg_wel_btn(event=None):
    global contact_error_msg, email_error_msg, pass_error_msg, var_fname, rgts_frame, var_lname, var_contact,var_email,\
        var_quetion, var_answer, var_chk, var_con_password, var_password
    global txt_fname, txt_lname, txt_contact, txt_email, cmb_quetion, txt_answer, txt_passwod, txt_conpassword, chk, wr
    wr = Frame(wp, bg="white")
    wr.place(x=0, y=0, width=1600, height=900)
    bgimage = ImageTk.PhotoImage(Image.open(r"Images\register_img.jpg"))
    label = Label(wr, image=bgimage)
    label.image = bgimage
    label.place(x=0, y=0)
    wr.configure(background="black")
    #img = Label(wr, image=bgimage)
    #img.place(x=0, y=0)

    # ----------=============== Registration page ===============--------------

    rgts_frame = Frame(wr, bg="white")
    rgts_frame.place(x=480, y=100, width=700, height=500)

    title = Label(rgts_frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place(
        x=50, y=30)

    # --------------------row 1
    var_fname = StringVar()
    f_name = Label(rgts_frame, text="First Name*", font=("times new roman", 15, "bold"), bg="white", fg="#244954").\
        place(x=50, y=100)
    txt_fname = Entry(rgts_frame, font=("times new roman", 15), bg="white", textvariable=var_fname)
    txt_fname.place(x=50, y=130, width=250)

    var_lname = StringVar()
    l_name = Label(rgts_frame, text="Last Name*", font=("times new roman", 15, "bold"), bg="white", fg="#244954").place(
        x=370,
        y=100)
    txt_lname = Entry(rgts_frame, font=("times new roman", 15), bg="white", textvariable=var_lname)
    txt_lname.place(x=370, y=130, width=250)

    # --------------------row 2

    var_contact = StringVar()
    contact = Label(rgts_frame, text="Contact No.*", font=("times new roman", 15, "bold"), bg="white", fg="#244954").\
        place(x=50, y=170)
    txt_contact = Entry(rgts_frame, font=("times new roman", 15), bg="white", textvariable=var_contact)
    txt_contact.place(x=50, y=200, width=250)
    contact_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    contact_error_msg.place(x=50, y=225)

    var_email = StringVar()
    email = Label(rgts_frame, text="Email*", font=("times new roman", 15, "bold"), bg="white", fg="#244954").\
        place(x=370, y=170)
    txt_email = Entry(rgts_frame, font=("times new roman", 15), bg="white", textvariable=var_email)
    txt_email.place(x=370, y=200, width=250)
    email_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    email_error_msg.place(x=370, y=225)

    # --------------------row 3

    quetion = Label(rgts_frame, text="Security Question*", font=("times new roman", 15, "bold"), bg="white",
                    fg="#244954").place(
        x=50, y=240)

    var_quetion = StringVar()
    cmb_quetion = ttk.Combobox(rgts_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                               textvariable=var_quetion)
    cmb_quetion["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Favorite Book",
                             "What Is Your Teacher Maiden Name ?", "Other")
    cmb_quetion.place(x=50, y=270, width=250)
    cmb_quetion.current(0)

    var_answer = StringVar()
    l_answer = Label(rgts_frame, text="Answer*", font=("times new roman", 15, "bold"), bg="white", fg="#244954").place(
        x=370,
        y=240)
    txt_answer = Entry(rgts_frame, font=("times new roman", 15), bg="white", textvariable=var_answer)
    txt_answer.place(x=370, y=270, width=250)

    # --------------------row 4

    var_password = StringVar()
    password = Label(rgts_frame, text="Password*", font=("times new roman", 15, "bold"), bg="white", fg="#244954").\
        place(x=50, y=310)
    txt_passwod = Entry(rgts_frame, font=("times new roman", 15), bg="white", textvariable=var_password)
    txt_passwod.place(x=50, y=340, width=250)
    txt_passwod.configure(show="*")

    eye_photo = ImageTk.PhotoImage(Image.open(r"Images\icons-eye.png"))
    eye_btn = Button(txt_passwod,relief=FLAT, image=eye_photo, command=eye)
    eye_btn.image = eye_photo
    eye_btn.pack(side = RIGHT)
    pass_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    pass_error_msg.place(x=50, y=365)

    var_con_password = StringVar()
    con_password = Label(rgts_frame, text="Confirm Password*", font=("times new roman", 15, "bold"), bg="white",
                         fg="#244954"). \
        place(x=370, y=310)
    txt_conpassword = Entry(rgts_frame, font=("times new roman", 15), bg="white", textvariable=var_con_password)
    txt_conpassword.place(x=370, y=340, width=250)
    txt_conpassword.configure(show="*")
    c_eye_btn = Button(txt_conpassword, relief=FLAT, image=eye_photo, command=c_eye)
    c_eye_btn.image = eye_photo
    c_eye_btn.pack(side=RIGHT)
    # --------------------terms
    t_c = Button(rgts_frame, text="Terms & Conditions", font=("times new roman", 13), bg="white", fg="blue",
                 activebackground="white", activeforeground="blue", relief=GROOVE, justify=CENTER, width=15, bd=0,
                 command=t_and_c)
    t_c.place(x=50, y=380)
    t_c.bind('<Return>', t_and_c)
    var_chk = IntVar()
    chk = Checkbutton(rgts_frame, text="I Agree The Terms & Conditions", onvalue=1, offvalue=0, variable=var_chk,
                      bg="white", font=("times new roman", 13))
    chk.place(x=50, y=400)

    # --------------------register and log in  btn

    register_btn = Button(rgts_frame, text="Register", font=("times new roman", 20, "bold"), bg="#1b7d5c", fg="white",
                          activebackground="grey", activeforeground="blue", relief=GROOVE, justify=CENTER,
                          width=15, bd=0, command=register)
    register_btn.place(x=50, y=440)
    register_btn.bind('<Return>', register)

    log_in_btn = Button(rgts_frame, text="Log In", font=("times new roman", 20, "bold"), bg="#1b7d5c", fg="white",
                        activebackground="grey", activeforeground="blue", relief=GROOVE, justify=CENTER,
                        width=15, bd=0, command=log_in)
    log_in_btn.place(x=370, y=440)
    log_in_btn.bind('<Return>', log_in)


# ---------register button call

def reset_entry():
    txt_fname.delete(0, END)
    txt_lname.delete(0, END)
    txt_contact.delete(0, END)
    txt_email.delete(0, END)
    cmb_quetion.current(0)
    txt_answer.delete(0, END)
    txt_passwod.delete(0, END)
    txt_conpassword.delete(0, END)
    chk.deselect()


def register(event=None):
    contact_error_msg.configure(text="")
    email_error_msg.configure(text="")
    pass_error_msg.configure(text="")
    if var_fname.get() == "" or var_lname.get() == "" or var_contact.get() == "" or var_email.get() == "" or \
            var_quetion.get() == "Select" or var_answer.get() == "" or var_password.get() == "" or \
            var_con_password.get() == "":
        messagebox.showerror("Error", "All Fields Are Required", parent=rgts_frame)
    elif not re.match(r'[6789]\d{9}$', var_contact.get()):
        contact_error_msg.configure(text="Invalid Contact")
    elif not re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", var_email.get()):
        email_error_msg.configure(text="Invalid Email")
    elif (len(var_password.get()) < 8) or not re.search("[a-z]", var_password.get()) or not \
            re.search("[A-Z]", var_password.get()) or not re.search("[0-9]", var_password.get()) or not \
            re.search("[_@$]", var_password.get()) or re.search("\s", var_password.get()):
        pass_error_msg.configure(text="Invalid Password use strong password")
    elif var_password.get() != var_con_password.get():
        messagebox.showerror("Error", "Password & Confirm Password should be same", parent=rgts_frame)
    elif var_chk.get() == 0:
        messagebox.showerror("Error", "Please Agree Our Terms & Condition", parent=rgts_frame)
    else:
        try:
            myprjc = mysql.connector.connect(host="localhost", user="root", password="Raj@coder")
            cur = myprjc.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS PROJECT")
            cur.execute("USE PROJECT")
            s = "CREATE TABLE IF NOT EXISTS REGISTER_DATA (Id integer(4)  AUTO_INCREMENT PRIMARY KEY," \
                " First_Name varchar(50) NOT NULL, Last_Name varchar(50) NOT NULL, Contact varchar(15) NOT NULL," \
                " Email varchar(100) NOT NULL, Security_Quetion varchar(100) NOT NULL, Answer varchar(100) NOT NULL," \
                " Password varchar(100) NOT NULL)"
            cur.execute(s)
            cur.execute("SELECT * FROM REGISTER_DATA WHERE Email = %s", (var_email.get(), ))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "User Already Exist, Please try with another email", parent=rgts_frame)
            else:
                s1 = "INSERT INTO register_data (First_Name, Last_Name, Contact, Email, Security_Quetion, Answer," \
                     " Password) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                data = (var_fname.get(), var_lname.get(), var_contact.get(), var_email.get(), var_quetion.get(),
                        var_answer.get(), var_password.get())
                cur.execute(s1, data)
                myprjc.commit()
                myprjc.close()
                messagebox.showinfo("Success", "Register Successful", parent=rgts_frame)
                reset_entry()

        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To: {str(ex)}", parent=rgts_frame)


# ---------upadate_pass

def upadate_pass():
    pass_error_msg_f.configure(text="")
    if var_password_f.get() == "" or var_con_password_f.get() == "":
        messagebox.showerror("Error", "Password & Confirm Fields Are Required", parent=forgot_fram)
    elif (len(var_password_f.get()) < 8) or not re.search("[a-z]", var_password_f.get()) or not \
            re.search("[A-Z]", var_password_f.get()) or not re.search("[0-9]", var_password_f.get()) or not \
            re.search("[_@$]", var_password_f.get()) or re.search("\s", var_password_f.get()):
        pass_error_msg_f.configure(text="Invalid Password use strong password")
    elif var_password_f.get() != var_con_password_f.get():
        messagebox.showerror("Error", "Password & Confirm Password should be same", parent=forgot_fram)
    else:
        try:
            myprjc = mysql.connector.connect(host="localhost", user="root", password="Raj@coder", database="PROJECT")
            cur = myprjc.cursor()
            cur.execute("UPDATE register_data SET Password= %s WHERE Email= %s", (var_password_f.get(),
                                                                                  var_emaillgi.get()))
            row3 = cur.fetchone()
            myprjc.commit()
            myprjc.close()
            messagebox.showinfo("Success", "Password Reset Successful", parent=forgot_fram)
            log_in()

        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To: {str(ex)}", parent=forgot_fram)



# ---------reset password

def reset_pass():
    global var_password_f, var_con_password_f, pass_error_msg_f, row2
    try:
        myprjc = mysql.connector.connect(host="localhost", user="root", password="Raj@coder", database="PROJECT")
        cur = myprjc.cursor()
        cur.execute("SELECT Security_Quetion, Answer FROM REGISTER_DATA WHERE Email = %s", (var_emaillgi.get(),))
        row2 = cur.fetchone()
        myprjc.commit()
        myprjc.close()
        #print(row2)
        #print(var_quetion_f.get(), var_answer_f.get())

    except Exception as ex:
        messagebox.showerror("Error", f"Error Due To: {str(ex)}", parent=forgot_fram)

    if  var_quetion_f.get() == "Select" or var_answer_f.get() == "":
        messagebox.showerror("Error", "Select Security Question And Fill Answer", parent=forgot_fram)


    elif row2[0] == var_quetion_f.get() and row2[1] == var_answer_f.get():

        var_password_f = StringVar()
        password_f = Label(forgot_fram, text="New Password", font=("times new roman", 15, "bold"), bg="white",
                         fg="gray").place(
            x=400,
            y=10)
        txt_passwod_f = Entry(forgot_fram, font=("times new roman", 15), bg="white", textvariable=var_password_f)
        txt_passwod_f.place(x=400, y=40, width=250)
        pass_error_msg_f = Label(forgot_fram, text="", font=("times new roman", 10), bg="white", fg="orange")
        pass_error_msg_f.place(x=400, y=65)

        var_con_password_f = StringVar()
        con_password_f = Label(forgot_fram, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray"). \
            place(x=400, y=90)
        txt_conpassword_f = Entry(forgot_fram, font=("times new roman", 15), bg="white", textvariable=
        var_con_password_f)
        txt_conpassword_f.place(x=400, y=120, width=250)
        reset_for_btn = Button(forgot_fram, text="Reset", font=("times new roman", 15, "bold"), bg="blue", fg="white",
                               activebackground="grey", activeforeground="blue", relief=GROOVE, justify=CENTER,
                               width=10, bd=0, command=upadate_pass).place(x=400, y=170)
    else:
        messagebox.showerror("Wrong", "Please Try Again", parent=forgot_fram)


# ---------forgot password

def forgot_pass():
    global var_answer_f, var_quetion_f, forgot_fram
    forgot_fram = Frame(box, bg="white")
    forgot_fram.place(x=100, y=160, width=800, height=440)
    quetion_f = Label(forgot_fram, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white",
                    fg="gray").place(
        x=50, y=10)

    var_quetion_f = StringVar()
    cmb_quetion_f = ttk.Combobox(forgot_fram, font=("times new roman", 13), state="readonly", justify=CENTER,
                               textvariable=var_quetion_f)
    cmb_quetion_f["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Favorite Book",
                             "What Is Your Teacher Maiden Name ?", "Other")
    cmb_quetion_f.place(x=50, y=40, width=250)
    cmb_quetion_f.current(0)

    var_answer_f = StringVar()

    l_answer_f = Label(forgot_fram, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
        x=50,
        y=90)
    txt_answer_f = Entry(forgot_fram, font=("times new roman", 15), bg="white", textvariable=var_answer_f)
    txt_answer_f.place(x=50, y=120, width=250)

    sub_for_btn = Button(forgot_fram, text="Submit", font=("times new roman", 15, "bold"), bg="blue", fg="white",
                        activebackground="grey", activeforeground="blue", relief=GROOVE, justify=CENTER,
                        width=10, bd=0, command=reset_pass).place(x=50, y=170)
    close_fg = Button(forgot_fram, text="X", font=(20), bg="White", fg="black",
                         relief=GROOVE, justify=CENTER,
                         width=4, bd=0, command=forgot_fram.destroy).place(x=750, y=10)


# -------predict price result------------------------------------------------

def predict_house_price(bath, balcony, total_sqft_int, bhk, price_per_sqft, area_type, availability, location):
    # load data
    df = pd.read_csv("ohe_data_reduce_cat_class.csv")

    # Split data
    X = df.drop('price', axis=1)
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

    # feature scaling
    sc = StandardScaler()
    sc.fit(X_train)
    X_train = sc.transform(X_train)
    X_test = sc.transform(X_test)

    # Load Model

    model = joblib.load('bangalore_house_price_prediction_rfr_model.pkl')

    x = np.zeros(len(X.columns))  # create zero numpy array, len = 107 as input value for model

    # adding feature's value accorind to their column index
    x[0] = bath
    x[1] = balcony
    x[2] = total_sqft_int
    x[3] = bhk
    x[4] = price_per_sqft

    if "availability_" + availability in X.columns:
        availability_index = np.where(X.columns == "availability_" + availability)[0][0]
        if availability == "Ready To Move":
            x[availability_index] = 1
        else:
            x[availability_index] = 0

    if 'area_type' + area_type in X.columns:
        area_type_index = np.where(X.columns == "area_type" + area_type)[0][0]
        x[area_type_index] = 1

    if 'location_' + location in X.columns:
        loc_index = np.where(X.columns == "location_" + location)[0][0]
        x[loc_index] = 1

    # feature scaling
    x = sc.transform([x])[0]  # give 2d np array for feature scaling and get 1d scaled np array
    x = np.array(x).reshape((1, -1))

    return model.predict(x)  # return the predicted value by train Random Forest model


# ------------------------------------------------------end of prediction------------
# function for calling
def predict(event=None):

    if var_bath.get()=="" or var_balcony.get()=="" or var_tsf.get()=="" or var_bhk.get() == "" or var_ppsf.get()=="" or\
            var_area_typ.get()=="Select" or var_ha.get()=="Select" or var_hl.get()=="Select":
        messagebox.showerror("Error", "All Fields Are Required", parent=pr)
    elif not re.search('^[0-9\.]*$', var_bath.get()) or not re.search('^[0-9\.]*$', var_balcony.get()) or not\
            re.search('^[0-9\.]*$', var_tsf.get()) or not re.search('^[0-9\.]*$', var_bhk.get()) or not \
            re.search('^[0-9\.]*$', var_ppsf.get()):
        messagebox.showerror("Error", "Use Only number For Bathroom, Balcony, Total Square Foot, BHK And Price Per Square Foot", parent=pr)
    else:
        m_rslt = predict_house_price(var_bath.get(), var_balcony.get(), var_tsf.get(), var_bhk.get(), var_ppsf.get(), var_area_typ.get(), var_ha.get(), var_hl.get())
        m_rslt_l.configure(text=str("{:.2f}".format((m_rslt[0])))+" Lakh")


# ------------price prediction page

count = 0

if count == 0:
    combostyle = ttk.Style()

    combostyle.theme_create('combostyle', parent='alt',
                            settings={'TCombobox':
                                          {'configure':
                                               {'selectbackground': '#a8d3e6',
                                                'fieldbackground': '#a8d3e6',
                                                'background': '#a8d3e6'
                                                }}}
                            )
    count += 1


def price_prediction():
    global pr, m_rslt_l, var_bath, var_balcony, var_tsf, var_bhk, var_ppsf, var_area_typ, var_ha, var_hl

    combostyle.theme_use('combostyle')

    pr = Frame(t_side, bg="grey")
    pr.place(x=0, y=0, width=1600, height=900)

    # ----------=============== price prediction page ===============--------------

    price_frame = Frame(pr, bg="white")
    price_frame.place(x=0, y=100, width=1600, height=500)

    bgimage = ImageTk.PhotoImage(Image.open(r"Images\Promo.jpeg"))
    label = Label(pr, image=bgimage)
    label.image = bgimage
    label.place(x=0, y=0)
    pr.configure(background="black")
    l_frame = Frame(label, bg="#a8d3e6")
    l_frame.place(x=340, y=10, width=700, height=500)

    home_btn = Button(label, text="Back To Home", font=("times new roman", 15, "bold"), bg="#9cacab", fg="white",
                      activebackground="#9cacab", activeforeground="white", relief=GROOVE, justify=CENTER,
                      width=12, bd=0, command=pr.destroy).place(x=0, y=0)
    logout_btn = Button(l_frame, text="Logout", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="#0062ff",
                        activebackground="#a8d3e6", activeforeground="#0062ff", relief=GROOVE, justify=CENTER,
                        width=8, bd=0, command=log_in)
    logout_btn.place(x=600, y=0)
    logout_btn.bind('<Return>', log_in)

    title = Label(l_frame, text="HOUSE PRICE PREDICTION", font=("times new roman", 20, "bold"), bg="#a8d3e6",
                  fg="green").place(x=50, y=30)

    # --------------------row 1
    var_bath = StringVar()
    l_bath = Label(l_frame, text="Number of Bathrooms", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                   fg="#244954").place(x=50, y=100)
    txt_bath = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_bath)
    txt_bath.place(x=50, y=130, width=250)

    var_balcony = StringVar()
    l_balcony = Label(l_frame, text="Balcony", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="#244954").place(
        x=370,
        y=100)
    txt_balcony = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_balcony)
    txt_balcony.place(x=370, y=130, width=250)

    # --------------------row 2

    var_tsf = StringVar()
    l_tsf = Label(l_frame, text="Total Square Foot", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="#244954").\
        place(x=50, y=170)
    txt_tsf = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_tsf)
    txt_tsf.place(x=50, y=200, width=250)
    #contact_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    #contact_error_msg.place(x=50, y=225)

    var_bhk = StringVar()
    bhk = Label(l_frame, text="BHK", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="#244954").place(x=370,
                                                                                                               y=170)
    txt_bhk = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_bhk)
    txt_bhk.place(x=370, y=200, width=250)
    #email_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    #email_error_msg.place(x=370, y=225)

    # --------------------row 3

    var_ppsf = StringVar()
    ppsf = Label(l_frame, text="Price Per Square Foot (Plot)", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                    fg="#244954").place(
        x=50, y=240)
    txt_ppsf = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_ppsf)
    txt_ppsf.place(x=50, y=270, width=250)

    var_area_typ = StringVar()
    area_typ = Label(l_frame, text="Area Type", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="#244954").place(
        x=370,
        y=240)
    cmb_area_typ = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                               textvariable=var_area_typ)
    cmb_area_typ["values"] = ("Select", "Build-in Area", "Build-up Area", "Plot Area")
    cmb_area_typ.place(x=370, y=270, width=250)
    cmb_area_typ.current(0)

    # --------------------row 4

    var_ha = StringVar()
    ha = Label(l_frame, text="House Availability", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="#244954").\
        place(x=50, y=310)
    cmb_ha = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                          textvariable=var_ha)
    cmb_ha["values"] = ("Select", "Ready To Move", "No")
    cmb_ha.place(x=50, y=340, width=250)
    cmb_ha.current(0)
    #pass_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    #pass_error_msg.place(x=50, y=365)

    var_hl = StringVar()
    hl = Label(l_frame, text="House Location", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                         fg="#244954"). \
        place(x=370, y=310)
    cmb_hl = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                          textvariable=var_hl)
    cmb_hl["values"] = ('Select', 'Whitefield', 'Sarjapur  Road', 'Electronic City',
       'Raja Rajeshwari Nagar', 'Haralur Road', 'Marathahalli',
       'Bannerghatta Road', 'Hennur Road', 'Uttarahalli', 'Thanisandra',
       'Electronic City Phase II', 'Hebbal', '7th Phase JP Nagar', 'Yelahanka',
       'Kanakpura Road', 'KR Puram', 'Sarjapur', 'Rajaji Nagar', 'Bellandur',
       'Kasavanhalli', 'Begur Road', 'Kothanur', 'Banashankari', 'Hormavu',
       'Harlur', 'Akshaya Nagar', 'Jakkur', 'Electronics City Phase 1',
       'Varthur', 'Ramamurthy Nagar', 'Hennur', 'HSR Layout', 'Chandapura',
       'Ramagondanahalli', 'Kundalahalli', 'Kaggadasapura', 'Koramangala',
       'Hulimavu', 'Hoodi', 'Budigere', 'Malleshwaram', 'Gottigere',
       'JP Nagar', 'Hegde Nagar', 'Yeshwanthpur', '8th Phase JP Nagar',
       'Channasandra', 'Bisuvanahalli', 'Vittasandra', 'Indira Nagar',
       'Old Airport Road', 'Vijayanagar', 'Hosa Road', 'Sahakara Nagar',
       'Kengeri', 'Brookefield', 'Balagere', 'Bommasandra',
       'Green Glen Layout', 'Panathur', 'Rachenahalli', 'Old Madras Road',
       'Kudlu Gate', 'Thigalarapalya', 'Mysore Road', 'Kadugodi',
       'Talaghattapura', 'Yelahanka New Town', 'Jigani', 'Ambedkar Nagar',
       'Devanahalli', 'Attibele', 'Dodda Nekkundi', 'Kanakapura',
       'Frazer Town', 'Nagarbhavi', 'Lakshminarayana Pura', 'Ananth Nagar',
       '5th Phase JP Nagar', 'Anekal', 'TC Palaya', 'Jalahalli',
       'Kengeri Satellite Town', 'Kudlu', 'CV Raman Nagar', 'Horamavu Agara',
       'Bhoganhalli', 'Kalena Agrahara', 'Doddathoguru', 'Subramanyapura',
       'Hosur Road', 'Hebbal Kempapura', 'Vidyaranyapura', 'BTM 2nd Stage',
       'Mahadevpura', 'Domlur', 'Horamavu Banaswadi', 'Tumkur Road')
    cmb_hl.place(x=370, y=340, width=250)
    cmb_hl.current(0)
    predict_btn = Button(l_frame, text="Predict Price", font=("times new roman", 15, "bold"), bg="blue", fg="white",
                         activebackground="grey", activeforeground="blue", relief=GROOVE, justify=CENTER,
                         width=10, bd=0, command=predict)
    predict_btn.place(x=260, y=440)
    predict_btn.bind('<Return>', predict)

    m_rslt_l = Label(l_frame, text="", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="blue")
    m_rslt_l.place(x=500, y=445)


# -----------loan prediction page

def predict_loan(Loan_Amount, Loan_Tenor, age, Housing_Rental, Monthly_Income, Office_Area, Loan_Purpose,
                        Gender, Marital_Status_num, Education_Level_num, Residential_Status, Employment_Type,
                        Nature_of_Business, Job_Position):
    df = pd.read_csv('loan_num_data2.csv')
    X = df.drop("Indicators", axis=1)
    y = df['Indicators']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
    sc = StandardScaler()
    sc.fit(X_train)
    X_train = sc.transform(X_train)
    X_test = sc.transform(X_test)
    model = joblib.load("loan_model.pkl")

    x = np.zeros(len(X.columns))  # create zero numpy array, len = 107 as input value for model

    # adding feature's value accorind to their column index
    x[0] = Loan_Amount
    x[1] = Loan_Tenor
    x[2] = age
    x[3] = Housing_Rental
    x[4] = Monthly_Income
    x[5] = Office_Area

    if 'Loan_Purpose_' + Loan_Purpose in X.columns:
        Loan_Purpose_index = np.where(X.columns == 'Loan_Purpose_' + Loan_Purpose)[0][0]
        x[Loan_Purpose_index] = 1

    if 'Gender_M' in X.columns:
        gender_index = np.where(X.columns == 'Gender_M')[0][0]
        if Gender == 'Male':
            x[gender_index] = 1
        else:
            x[gender_index] = 0

    if 'Marital Status_num' in X.columns:
        Marital_index = np.where(X.columns == 'Marital Status_num')[0][0]
        if Marital_Status_num == 'Single':
            x[Marital_index] = 2
        elif Marital_Status_num == 'Married':
            x[Marital_index] = 1
        else:
            x[Marital_index] = 0

    if 'Education Level_num' in X.columns:
        Education_index = np.where(X.columns == 'Education Level_num')[0][0]
        if Education_Level_num == 'Secondary':
            x[Education_index] = 4
        elif Education_Level_num == 'Form 3 or below':
            x[Education_index] = 0
        elif Education_Level_num == 'Post Graduate':
            x[Education_index] = 1
        elif Education_Level_num == 'Post Secondary':
            x[Education_index] = 2
        elif Education_Level_num == 'University':
            x[Education_index] = 5
        else:
            x[Education_index] = 3

    if 'Residential Status_' + Residential_Status in X.columns:
        Residential_Status_index = np.where(X.columns == 'Residential Status_' + Residential_Status)[0][0]
        x[Residential_Status_index] = 1

    if 'Employment Type_' + Employment_Type in X.columns:
        Employment_index = np.where(X.columns == 'Employment Type_' + Employment_Type)[0][0]
        x[Employment_index] = 1

    if 'Nature of Business_' + Nature_of_Business in X.columns:
        Business_index = np.where(X.columns == 'Nature of Business_' + Nature_of_Business)[0][0]
        x[Business_index] = 1

    if 'Job Position_' + Job_Position in X.columns:
        Job_index = np.where(X.columns == 'Job Position_' + Job_Position)[0][0]
        x[Job_index] = 1

    # feature scaling
    x = sc.transform([x])[0]  # give 2d np array for feature scaling and get 1d scaled np array
    x = np.array(x).reshape((1, -1))
    return model.predict(x)

def l_predict(event=None):
    if var_loan_amount.get() == "" or var_loan_tenor.get() == "" or var_age.get() == "" or var_housing_rental.get() == \
            "" or var_monthly_income.get() == "" or var_office_area.get() == "Select" or var_loan_purpose.get() == \
            "Select" or var_gender.get() == "Select" or var_marital_status.get() == "Select" or \
            var_education_level.get() == "Select" or var_residential_status.get() == "Select" or var_employment_type.\
            get() == "Select" or var_nature_business.get() == "Select" or var_job_position.get() == "Select":
        messagebox.showerror("Error", "All Fields Are Required", parent=lp)

    elif not re.search('^[0-9\.]*$', var_loan_amount.get()) or not re.search('^[0-9\.]*$', var_loan_tenor.get()) or not\
            re.search('^[0-9\.]*$', var_age.get()) or not re.search('^[0-9\.]*$', var_housing_rental.get()) or not \
            re.search('^[0-9\.]*$', var_monthly_income.get()):
        messagebox.showerror("Error", "Use Only number For loan Amount, Loan Tenor, Age, Housing Rental And Monthly "
                                      "Income", parent=lp)

    else:
        result = predict_loan(var_loan_amount.get(), var_loan_tenor.get(), var_age.get(), var_housing_rental.get(),
                              var_monthly_income.get(), var_office_area.get(), var_loan_purpose.get(), var_gender.get(),
                              var_marital_status.get(), var_education_level.get(), var_residential_status.get(),
                              var_employment_type.get(), var_nature_business.get(), var_job_position.get())

        if result[0] == 0:
            m_rslt_l1.configure(text= 'Not Eligible')
        elif result[0] == 1:
            m_rslt_l1.configure(text='Eligible')


def loan_prediction():
    global lp, m_rslt_l1, var_loan_amount, var_loan_tenor, var_age, var_housing_rental, var_monthly_income, \
        var_office_area, var_loan_purpose, var_gender, var_marital_status, var_education_level, \
        var_residential_status, var_employment_type, var_nature_business, var_job_position

    combostyle.theme_use('combostyle')

    lp = Frame(t_side, bg="grey")
    lp.place(x=0, y=0, width=1600, height=900)

    # ----------=============== price prediction page ===============--------------

    loan_frame = Frame(lp, bg="white")
    loan_frame.place(x=0, y=100, width=1600, height=500)

    bgimage = ImageTk.PhotoImage(Image.open(r"Images\loan.jpg"))
    label = Label(lp, image=bgimage)
    label.image = bgimage
    label.place(x=0, y=0)
    lp.configure(background="black")
    l_frame = Frame(label, bg="#a8d3e6")
    l_frame.place(x=340, y=10, width=700, height=700)

    home_btn = Button(label, text="Back To Home", font=("times new roman", 15, "bold"), bg="#6c5a66", fg="white",
                      activebackground="#6c5a66", activeforeground="white", relief=GROOVE, justify=CENTER,
                      width=12, bd=0, command=lp.destroy).place(x=0, y=0)
    logout_btn = Button(l_frame, text="Logout", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="#0062ff",
                        activebackground="#a8d3e6", activeforeground="#0062ff", relief=GROOVE, justify=CENTER,
                        width=8, bd=0, command=log_in)
    logout_btn.place(x=600, y=0)
    logout_btn.bind('<Return>', log_in)

    title = Label(l_frame, text="LOAN PREDICTION", font=("times new roman", 20, "bold"), bg="#a8d3e6",
                  fg="green").place(x=50, y=30)

    # --------------------row 1
    var_loan_amount = StringVar()
    l_loan_amount = Label(l_frame, text="Loan Amount", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                   fg="#244954").place(x=50, y=100)
    txt_loan_amount = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_loan_amount)
    txt_loan_amount.place(x=50, y=130, width=250)

    var_loan_tenor = StringVar()
    l_loan_tenor = Label(l_frame, text="Loan Tenor (Month)", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="#244954").place(
        x=370,
        y=100)
    txt_loan_tenor = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_loan_tenor)
    txt_loan_tenor.place(x=370, y=130, width=250)

    # --------------------row 2

    var_age = StringVar()
    l_age = Label(l_frame, text="Age", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="#244954"). \
        place(x=50, y=170)
    txt_age = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_age)
    txt_age.place(x=50, y=200, width=250)
    # contact_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    # contact_error_msg.place(x=50, y=225)

    var_housing_rental = StringVar()
    l_housing_rental = Label(l_frame, text="Housing Rental", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                             fg="#244954").place(x=370, y=170)
    txt_housing_rental = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_housing_rental)
    txt_housing_rental.place(x=370, y=200, width=250)
    # email_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    # email_error_msg.place(x=370, y=225)

    # --------------------row 3

    var_monthly_income = StringVar()
    l_monthly_income = Label(l_frame, text="Monthly Income", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                 fg="#244954").place(x=50, y=240)
    txt_monthly_income = Entry(l_frame, font=("times new roman", 15), bg="#a8d3e6", textvariable=var_monthly_income)
    txt_monthly_income.place(x=50, y=270, width=250)

    var_office_area = StringVar()
    l_office_area = Label(l_frame, text="Office Area", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                          fg="#244954").place(x=370, y=240)
    cmb_office_area = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                                   textvariable=var_office_area)
    cmb_office_area["values"] = ("Select", "1", "2", "3")
    cmb_office_area.place(x=370, y=270, width=250)
    cmb_office_area.current(0)

    # --------------------row 4

    var_loan_purpose = StringVar()
    l_loan_purpose = Label(l_frame, text="Loan Purpose", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                           fg="#244954").place(x=50, y=310)
    cmb_loan_purpose = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                                    textvariable=var_loan_purpose)
    cmb_loan_purpose["values"] = ("Select", 'Personal use', 'Tax Payment', 'Settle Loan / Credit Card O/S', 'Stand by',
                                  'Decoration', 'Investment', 'Car Purchase', 'Business', 'Marriage', 'Education')
    cmb_loan_purpose.place(x=50, y=340, width=250)
    cmb_loan_purpose.current(0)
    # pass_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    # pass_error_msg.place(x=50, y=365)

    var_gender = StringVar()
    l_gender = Label(l_frame, text="Gender", font=("times new roman", 15, "bold"), bg="#a8d3e6",
               fg="#244954"). \
        place(x=370, y=310)
    cmb_gender = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                              textvariable=var_gender)
    cmb_gender["values"] = ('Select', 'Male', 'Female')
    cmb_gender.place(x=370, y=340, width=250)
    cmb_gender.current(0)

    # --------------------row 5

    var_marital_status = StringVar()
    l_loan_purpose = Label(l_frame, text="Marital Status", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                           fg="#244954").place(x=50, y=380)
    cmb_marital_status_num = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                                          textvariable=var_marital_status)
    cmb_marital_status_num["values"] = ("Select", 'Married', 'Single', 'Divorced')
    cmb_marital_status_num.place(x=50, y=410, width=250)
    cmb_marital_status_num.current(0)
    # pass_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    # pass_error_msg.place(x=50, y=365)

    var_education_level = StringVar()
    l_education_level_num = Label(l_frame, text="Education Level", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                                  fg="#244954").place(x=370, y=380)
    cmb_education_level_num = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                                           textvariable=var_education_level)
    cmb_education_level_num["values"] = ('Select', 'Secondary', 'Post Graduate', 'Post Secondary', 'University',
                                         'Form 3 or below', 'Primary')
    cmb_education_level_num.place(x=370, y=410, width=250)
    cmb_education_level_num.current(0)

    # --------------------row 6

    var_residential_status = StringVar()
    l_residential_status = Label(l_frame, text="Residential Status", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                           fg="#244954"). \
        place(x=50, y=450)
    cmb_residential_status = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                                    textvariable=var_residential_status)
    cmb_residential_status["values"] = ("Select", 'Live With Relatives', 'Rental', 'Self-owned Private Housing',
                                        'Mortgaged Private Housing', 'Self-owned Public Housing', 'Company Provision',
                                        'Mortgaged Public Housing')
    cmb_residential_status.place(x=50, y=480, width=250)
    cmb_residential_status.current(0)
    # pass_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    # pass_error_msg.place(x=50, y=365)

    var_employment_type = StringVar()
    l_employment_type = Label(l_frame, text="Employment Type", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                     fg="#244954"). \
        place(x=370, y=450)
    cmb_employment_type = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                              textvariable=var_employment_type)
    cmb_employment_type["values"] = ('Select', 'Fixed Income Earner', 'Civil Servant', 'Non Fixed Income Earner',
                                     'Self-Employed')
    cmb_employment_type.place(x=370, y=480, width=250)
    cmb_employment_type.current(0)

    # --------------------row 7

    var_nature_business = StringVar()
    l_nature_business = Label(l_frame, text="Nature of Business", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                           fg="#244954").place(x=50, y=510)
    cmb_nature_business = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                                    textvariable=var_nature_business)
    cmb_nature_business["values"] = ("Select", 'Manager', 'Office Worker', 'Services', 'Sales', 'Executive',
                                     'Professional', 'Skilled Worker', 'Owner of a Business', 'Guard', 'Driver',
                                     'Unskilled Worker', 'Factory Worker', 'Construction Trades')
    cmb_nature_business.place(x=50, y=540, width=250)
    cmb_nature_business.current(0)
    # pass_error_msg = Label(rgts_frame, text="", font=("times new roman", 10), bg="white", fg="orange")
    # pass_error_msg.place(x=50, y=365)

    var_job_position = StringVar()
    l_job_position = Label(l_frame, text="Job Position", font=("times new roman", 15, "bold"), bg="#a8d3e6",
                     fg="#244954").place(x=370, y=510)
    cmb_job_position = ttk.Combobox(l_frame, font=("times new roman", 13), state="readonly", justify=CENTER,
                              textvariable=var_job_position)
    cmb_job_position["values"] = ('Select', 'Private', 'Government/Semi-Government', 'Self Employed', 'Public')
    cmb_job_position.place(x=370, y=540, width=250)
    cmb_job_position.current(0)

    predict_btn = Button(l_frame, text="Predict", font=("times new roman", 15, "bold"), bg="blue", fg="white",
                         activebackground="grey", activeforeground="blue", relief=GROOVE, justify=CENTER,
                         width=10, bd=0, command=l_predict)
    predict_btn.place(x=260, y=640)
    predict_btn.bind('<Return>', l_predict)


    m_rslt_l1 = Label(l_frame, text="", font=("times new roman", 15, "bold"), bg="#a8d3e6", fg="blue")
    m_rslt_l1.place(x=500, y=645)

#----------price and loan

def home_and_loan():
    global t_side
    t_side = Frame(lw, bg="white")
    t_side.place(x=0, y=0, width=1600, height=900)
    bgimage = ImageTk.PhotoImage(Image.open(r"Images\slide.jpg"))
    label = Label(t_side, image=bgimage)
    label.image = bgimage
    label.place(x=0, y=0)
    t_side.configure(background="black")
    price_pre_btn = Button(t_side, text="Price Prediction", font=("times new roman", 20, "bold"), bg="blue", fg="white",
                           activebackground="grey", activeforeground="blue", relief=GROOVE, justify=CENTER,
                           width=15, bd=0, command=price_prediction).place(x=300, y=680)
    loan_pre_btn = Button(t_side, text="Loan Prediction", font=("times new roman", 20, "bold"), bg="blue", fg="white",
                          activebackground="grey", activeforeground="blue", relief=GROOVE, justify=CENTER,
                          width=15, bd=0, command=loan_prediction).place(x=1100, y=680)


# ---------login access button call

def log_in_exis(event=None):
    password_error_msglgi.configure(text="")
    if var_emaillgi.get() == "" or var_passwordlgi.get() == "":
        messagebox.showerror("Error", "Please enter Email & password", parent=lw)
    else:
        try:
            myprjc = mysql.connector.connect(host="localhost", user="root", password="Raj@coder", database="PROJECT")
            cur = myprjc.cursor()
            cur.execute("SELECT * FROM REGISTER_DATA WHERE Email = %s", (var_emaillgi.get(), ))
            row1 = cur.fetchone()
            myprjc.commit()
            myprjc.close()
            if row1 != None:
                if row1[4] == var_emaillgi.get() and row1[7] == var_passwordlgi.get():
                    messagebox.showinfo("Success", "Login Successful", parent=lw)
                    home_and_loan()

                elif row1[4] != var_emaillgi.get():
                    messagebox.showerror("Error", "Invalid Email", parent=lw)
                else:
                    password_error_msglgi.configure(text="Incorrect password")
                    Forgotten_pss_btn = Button(box2, text="Forgotten Password?", font=("times new roman", 10), bg="#232623",
                                               fg="blue",
                                               activebackground="#232623", activeforeground="blue", relief=GROOVE,
                                               justify=CENTER, width=16,
                                               bd=0, command=forgot_pass)
                    Forgotten_pss_btn.place(x=250, y=180)
            else:
                messagebox.showerror("Error", "Invalid Email & password", parent=lw)

        except Exception as ex:
            messagebox.showerror("Error", f"Error Due To: {str(ex)}", parent=lw)



# ---------log in button call

def log_in(event=None):
    global lw, var_emaillgi, var_passwordlgi, password_error_msglgi, box2, box

    lw = Frame(wp, bg="white")
    lw.place(x=0, y=0, width=1600, height=900)

    abu = Frame(lw, bg='white')
    abu.place(x=0, y=0, width= 500, height=900)
    aboutus = ImageTk.PhotoImage(Image.open(r"images\about_us.jpg"))
    imgau = Label(abu, image=aboutus)
    imgau.image = aboutus
    imgau.place(x=0, y=0)
    abu.configure(background="white")

    box = Frame(lw, bg='#232623')
    box.place(x=600, y=0, width=1100, height=900)
    box1 = Frame(box, bg='white')
    box1.place(x=250, y=200, width=400, height=400)
    box2 = Frame(box1, bg='#232623')
    box2.place(x=5, y=5, width=390, height=390)

    title_log = Label(box, text="Log-in", font=("times new roman", 20, "bold"), bg="#232623", fg="white").place(
        x=400, y=150)

    var_emaillgi = StringVar()
    emaillgi = Label(box2, text="Email", font=("times new roman", 15, "bold"), bg="#232623", fg="white").place(x=20,
                                                                                                          y=20)
    txt_emaillgi = Entry(box2, font=("times new roman", 15), bg="white", textvariable=var_emaillgi).place(x=20, y=60,
                                                                                                        width=350)

    var_passwordlgi = StringVar()
    passwordlgi = Label(box2, text="Password", font=("times new roman", 15, "bold"), bg="#232623", fg="white").place(
        x=20, y=110)
    txt_passwodlgi = Entry(box2, font=("times new roman", 15), bg="white", textvariable=var_passwordlgi, show='*').place(
        x=20, y=150, width=350)
    password_error_msglgi = Label(box2, text="", font=("times new roman", 10), bg="#232623", fg="orange")
    password_error_msglgi.place(x=20, y=180)


    log_in_btnlgi = Button(box2, text="Log In", font=("times new roman", 20, "bold"), bg="blue", fg="white",
                           activebackground="green", activeforeground="blue", relief=GROOVE, justify=CENTER, width=21,
                           bd=0, command=log_in_exis)
    log_in_btnlgi.bind('<Return>', log_in_exis)
    log_in_btnlgi.place(x=20, y=230)
    new_user = Label(box2, text="« if you are a new user please", font=("times new roman", 15, "bold"), bg="#232623", fg="white").place(
        x=0, y=330)
    login_btnrgt = Button(box2, text="register here »", font=("times new roman", 15, "bold"), bg="#232623", fg="blue",
                           activebackground="#232623", activeforeground="blue", relief=GROOVE, justify=CENTER, width=10,
                           bd=0, command=reg_wel_btn)
    login_btnrgt.place(x=257, y=327)
    login_btnrgt.bind('<Return>', reg_wel_btn)

# -------wellcome register button

register_btn = Button(wp, text="Register", font=("times new roman", 20, "bold"), bg="green", fg="white",
                          activebackground="grey", activeforeground="green", relief=GROOVE, justify=CENTER,
                          width=15, bd=0, command=reg_wel_btn).place(x=600, y=500)

# -------wellcome login button

log_in_btn = Button(wp, text="Log In", font=("times new roman", 20, "bold"), bg="blue", fg="white",
                        activebackground="grey", activeforeground="blue", relief=GROOVE, justify=CENTER,
                        width=15, bd=0, command=log_in).place(x=600, y=600)


wp.mainloop()
