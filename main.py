import json
from configparser import ConfigParser
from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
import requests
from fpdf import FPDF
from PIL import Image, ImageTk

pdf = FPDF()
pdf.add_page()


def main():
    wind = Tk()
    app = DockyardManagementSystem(wind)
    wind.mainloop()
    

class DockyardManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Dockyard Management System")
        self.root.geometry("1550x800+0+0")
        
# ===================================== Variables ========================================================
        
        self.shiptype_var = StringVar()
        self.shipid_var = StringVar()
        self.shipcomp_var = StringVar()
        self.capname_var = StringVar()
        self.caplis_var = StringVar()
        self.cargo_var = StringVar()
        self.depcountry_var = StringVar()
        self.arrcountry_var = StringVar()
        self.depdate_var = StringVar()
        self.arrdate_var = StringVar()
        self.deptime_var = StringVar()
        self.arrtime_var = StringVar()
        self.insuranceid_var = StringVar()
        self.insvaliddate_var = StringVar()
        
# ============================================ Title =========================================================
        
        lbltitle = Label(self.root, text="Dockyard Management System", bd=12, relief=GROOVE, bg="#142E54", fg="white",
                         font=("Lato 35 bold"), padx=2, pady=3)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=8, relief=GROOVE, padx=20, bg="#F3F4F6")
        frame.place(x=2, y=90, width=775, height=342)
        
# =========================================== LeftFrame =================================================

        DataFrameLeft = LabelFrame(frame, bd=8, relief=GROOVE, padx=20, text=" Ship Information ",
                                   fg="blue", font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=718, height=310)

        lblshiptype = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Type of Ship :  ", padx=2, pady=6)
        lblshiptype.grid(row=0, column=0, sticky=W)

        options = ("Container Ship", "Tanker Ship", "Passenger Ship", "Naval Ship")
        ship_combo = ttk.Combobox(DataFrameLeft, value=options, width=16,
                                 font=("arial", 10, "bold"), textvariable=self.shiptype_var
                                 , state="Readonly")
        ship_combo.grid(row=0, column=1)
        ship_combo.current(0)

        lblshipid = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Ship ID :", padx=2, pady=6)
        lblshipid.grid(row=1, column=0, sticky=W)
        txtshipid = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.shipid_var, bg="white", bd=2,
                         relief=RIDGE, width=18)
        txtshipid.grid(row=1, column=1)

        lblshipcomp = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Ship Company :", padx=2, pady=6)
        lblshipcomp.grid(row=2, column=0, sticky=W)
        txtshipcomp = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.shipcomp_var, bg="white", bd=2,
                        relief=RIDGE, width=18)
        txtshipcomp.grid(row=2, column=1)

        lblcapname = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Captain Name :", padx=2, pady=6)
        lblcapname.grid(row=3, column=0, sticky=W)
        txtcapname = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.capname_var, bg="white",
                             bd=2, relief=RIDGE, width=18)
        txtcapname.grid(row=3, column=1)

        lblcaplis = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Captain Lisence No :", padx=2, pady=6)
        lblcaplis.grid(row=4, column=0, sticky=W)
        txtcaplis = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.caplis_var, bg="white", bd=2,
                            relief=RIDGE, width=18)
        txtcaplis.grid(row=4, column=1)

        lblcargo = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Ship Cargo :", padx=2, pady=6)
        lblcargo.grid(row=5, column=0, sticky=W)
        txtcargo = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.cargo_var, bg="white", bd=2,
                           relief=RIDGE, width=18)
        txtcargo.grid(row=5, column=1)

        lbldepcountry = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Ship Departure Country :", padx=2, pady=6)
        lbldepcountry.grid(row=6, column=0, sticky=W)
        txtdepcountry = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.depcountry_var, bg="white", bd=2,
                        relief=RIDGE, width=18)
        txtdepcountry.grid(row=6, column=1)

        lblarrcountry = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Ship Arrival Country :", padx=2, pady=6)
        lblarrcountry.grid(row=7, column=0, sticky=W)
        txtarrcountry = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.arrcountry_var, bg="white", bd=2,
                            relief=RIDGE, width=18)
        txtarrcountry.grid(row=7, column=1)

        lbldepdate = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Ship Departure Date :", padx=25, pady=6)
        lbldepdate.grid(row=0, column=2, sticky=W)
        txtdepdate = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.depdate_var, bg="white", bd=2,
                            relief=RIDGE, width=18)
        txtdepdate.grid(row=0, column=3)

        lblarrdate = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Ship Arrival Date:", padx=25, pady=6)
        lblarrdate.grid(row=1, column=2, sticky=W)
        txtarrdate = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.arrdate_var, bg="white", bd=2,
                          relief=RIDGE, width=18)
        txtarrdate.grid(row=1, column=3)

        lbldeptime = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Time of Departure:", padx=25, pady=6)
        lbldeptime.grid(row=2, column=2, sticky=W)
        txtdeptime = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.deptime_var, bg="white",
                             bd=2, relief=RIDGE, width=18)
        txtdeptime.grid(row=2, column=3)

        lblarrtime = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Time of Arrival:", padx=25, pady=6)
        lblarrtime.grid(row=3, column=2, sticky=W)
        txtarrtime = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.arrtime_var, bg="white", bd=2,
                          relief=RIDGE, width=18)
        txtarrtime.grid(row=3, column=3)

        lblinsuranceid = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Ship Insurance ID:", padx=25, pady=6)
        lblinsuranceid.grid(row=4, column=2, sticky=W)
        txtinsuranceid = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.insuranceid_var,
                                bg="white", bd=2, relief=RIDGE, width=18)
        txtinsuranceid.grid(row=4, column=3)

        lblinsvaliddate = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Insurance Valid Date:", padx=25, pady=6)
        lblinsvaliddate.grid(row=5, column=2, sticky=W)
        txtinsvaliddate = Entry(DataFrameLeft, font=("arial", 10, "bold"), textvariable=self.insvaliddate_var, bg="white", bd=2,
                           relief=RIDGE, width=18)
        txtinsvaliddate.grid(row=5, column=3)
        
# ========================================== RightFrame ========================================================    

        frame1 = Frame(self.root, bd=10, relief=GROOVE, padx=20, bg="#F3F4F6")
        frame1.place(x=800, y=90, width=480, height=392)
        
        DataFrameRight = LabelFrame(frame1, bd=8, relief=RIDGE, padx=10, text=" Features ",
                                    fg="blue", font=("arial", 12, "bold"))
        DataFrameRight.place(x=-10, y=2, width=440, height=360)
        
        img1 = Image.open("C:\Project\cargo.jpg")
        img1 = img1.resize((300,190),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(DataFrameRight, image=self.photoimg1, borderwidth=0)
        b1.place(x=50, y=12)  
        
        but_detained = Button(DataFrameRight, command=self.second_win, text="Detained Ship", font=("arial", 12, "bold"), width=15,
                              bg="navy", fg="white", relief=GROOVE)
        but_detained.place(x=23, y=225)
        
        but_maintenance = Button(DataFrameRight, command=self.forth_win, text="Maintenance", font=("arial", 12, "bold"), width=14,
                              bg="navy", fg="white", relief=GROOVE)
        but_maintenance.place(x=220, y=225)
        
        but_weather = Button(DataFrameRight, command=self.third_win, text="Weather Information", font=("arial", 12, "bold"), width=15,
                              bg="navy", fg="white", relief=GROOVE)
        but_weather.place(x=23, y=275)
        
        but_exit = Button(DataFrameRight, command=self.iExit, text="Exit", font=("arial", 12, "bold"), width=14,
                              bg="navy", fg="white", relief=GROOVE)
        but_exit.place(x=220, y=275)
                       
        
# ============================================== Buttons ========================================================

        framebutton = Frame(self.root, bd=7, relief=RIDGE, padx=20)
        framebutton.place(x=0, y=430, width=775, height=50)

        btnAddData = Button(framebutton, command=self.adda_data, text="ADD", font=("arial", 12, "bold"), width=21,
                            bg="navy", fg="white", relief=GROOVE, padx=8)
        btnAddData.grid(row=0, column=0)

        btnupdatedata = Button(framebutton, command=self.update, text="UPDATE", font=("arial", 12, "bold"), width=21,
                            bg="navy", fg="white", relief=GROOVE, padx=8)
        btnupdatedata.grid(row=0, column=1)

        btnresetdata = Button(framebutton, command=self.reset, text="RESET", font=("arial", 12, "bold"), width=21,
                            bg="navy", fg="white",relief=GROOVE, padx=8)
        btnresetdata.grid(row=0, column=2)
        
# =========================================== ShowStoredData ====================================================== 
        
        framedetails = Frame(self.root, bd=8, relief=RIDGE)
        framedetails.place(x=0, y=485, width=1275, height=170)

        Table_frame = Frame(framedetails, bd=5, relief=RIDGE, bg="white")
        Table_frame.place(x=0, y=2, width=1254, height=151)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        yscroll.pack(side=RIGHT, fill=Y)

        self.ship_table = ttk.Treeview(Table_frame, column=(
            "shiptype", "shipid", "shipcompany", "captainname", "captainlisence", "shipcargo", "departcountry", "arrivalcountry",
            "departdate", "arrivaldate", "departtime", "arrivaltime", "shipinsurance", "insurancedate"), xscrollcommand=xscroll.set,
                                          yscrollcommand=yscroll.set)

        xscroll.config(command=self.ship_table.xview)
        yscroll.config(command=self.ship_table.yview)

        self.ship_table.heading("shiptype", text="Type of Ship")
        self.ship_table.heading("shipid", text="Ship ID")
        self.ship_table.heading("shipcompany", text="Ship Company")
        self.ship_table.heading("captainname", text="Captain Name")
        self.ship_table.heading("captainlisence", text="Captain Lisence No")
        self.ship_table.heading("shipcargo", text="Ship Cargo")
        self.ship_table.heading("departcountry", text="Departure Country")
        self.ship_table.heading("arrivalcountry", text="Arrival Country")
        self.ship_table.heading("departdate", text="Departure Date")
        self.ship_table.heading("arrivaldate", text="Arrival Date")
        self.ship_table.heading("departtime", text="Departure Time")
        self.ship_table.heading("arrivaltime", text="Arrival Time")
        self.ship_table.heading("shipinsurance", text="Ship Insurance ID")
        self.ship_table.heading("insurancedate", text="Insurance Valid Date")

        self.ship_table["show"] = "headings"
        self.ship_table.pack(fill=BOTH, expand=1)
        
        self.ship_table.column("shiptype", width=150)
        self.ship_table.column("shipid", width=150)
        self.ship_table.column("shipcompany", width=150)
        self.ship_table.column("captainname", width=150)
        self.ship_table.column("captainlisence", width=150)
        self.ship_table.column("shipcargo", width=150)
        self.ship_table.column("departcountry", width=150)
        self.ship_table.column("arrivalcountry", width=150)
        self.ship_table.column("departdate", width=150)
        self.ship_table.column("arrivaldate", width=150)
        self.ship_table.column("departtime", width=150)
        self.ship_table.column("arrivaltime", width=150)
        self.ship_table.column("shipinsurance", width=150)
        self.ship_table.column("insurancedate", width=150)
        
        self.fetch_data()
        self.ship_table.bind("<ButtonRelease-1>", self.get_cursor)
        
    def second_win(self):
        self.new_window = Toplevel(self.root)
        self.appp = detain(self.new_window)
        
    def third_win(self):
        self.neww_windoww = Toplevel(self.root)
        self.aappp = weather_app(self.neww_windoww)
        
    def forth_win(self):
        self.newww_windowww = Toplevel(self.root)
        self.aapppp = maintenance(self.newww_windowww)
        
        
    def adda_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", passwd="shreyas", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("INSERT INTO dockyard VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.shiptype_var.get(),
            self.shipid_var.get(),
            self.shipcomp_var.get(),
            self.capname_var.get(),
            self.caplis_var.get(),
            self.cargo_var.get(),
            self.depcountry_var.get(),
            self.arrcountry_var.get(),
            self.depdate_var.get(),
            self.arrdate_var.get(),
            self.deptime_var.get(),
            self.arrtime_var.get(),
            self.insuranceid_var.get(),
            self.insvaliddate_var.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Ship Information has been Added Successfully")
        
    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", passwd="shreyas", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE dockyard SET shiptype=%s,shipcompany=%s,captainname=%s,captainlisence=%s,shipcargo=%s,departcountry=%s,arrivalcountry=%s,departdate=%s,arrivaldate=%s,departtime=%s,arrivaltime=%s,shipinsurance=%s,insurancedate=%s WHERE shipid=%s",(
            self.shiptype_var.get(),
            self.shipcomp_var.get(),
            self.capname_var.get(),
            self.caplis_var.get(),
            self.cargo_var.get(),
            self.depcountry_var.get(),
            self.arrcountry_var.get(),
            self.depdate_var.get(),
            self.arrdate_var.get(),
            self.deptime_var.get(),
            self.arrtime_var.get(),
            self.insuranceid_var.get(),
            self.insvaliddate_var.get(),
            self.shipid_var.get()      
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success","Ship Information has been Updated Successfully")
        
        
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", passwd="shreyas", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM dockyard")
        rows = my_cursor.fetchall()
        
        if len(rows) != 0:
            self.ship_table.delete(*self.ship_table.get_children())
            for i in rows:
                self.ship_table.insert("", END, values = i)
            conn.commit()
        conn.close()
        
    def get_cursor(self, event=""):
        cursor_row = self.ship_table.focus()
        content = self.ship_table.item(cursor_row)
        row = content['values']
        
        self.shiptype_var.set(row[0]),
        self.shipid_var.set(row[1]),
        self.shipcomp_var.set(row[2]),
        self.capname_var.set(row[3]),
        self.caplis_var.set(row[4]),
        self.cargo_var.set(row[5]),
        self.depcountry_var.set(row[6]),
        self.arrcountry_var.set(row[7]),
        self.depdate_var.set(row[8]),
        self.arrdate_var.set(row[9]),
        self.deptime_var.set(row[10]),
        self.arrtime_var.set(row[11]),
        self.insuranceid_var.set(row[12]),
        self.insvaliddate_var.set(row[13])
        
    def reset(self):
        self.shiptype_var.set(""),
        self.shipid_var.set(""),
        self.shipcomp_var.set(""),
        self.capname_var.set(""),
        self.caplis_var.set(""),
        self.cargo_var.set(""),
        self.depcountry_var.set(""),
        self.arrcountry_var.set(""),
        self.depdate_var.set(""),
        self.arrdate_var.set(""),
        self.deptime_var.set(""),
        self.arrtime_var.set(""),
        self.insuranceid_var.set(""),
        self.insvaliddate_var.set("")
        
    def iExit(self):
        iExit = messagebox.askyesno("Dockyard Management System","Do you want to exit?")
        if iExit > 0:
            self.root.destroy()
            return
        
        
class detain:
    def __init__(self, root):
        self.root = root
        self.root.title("Detainship Form")
        self.root.geometry("800x560+200+42")
        
# ============================================== Variables =====================================================

        self.var_shipid = StringVar()
        self.var_captname = StringVar()
        self.var_shipcargo = StringVar()
        self.var_shiparrcountry = StringVar()
        self.var_arrdate = StringVar()
        self.var_arrtime = StringVar()
        self.var_duedate = StringVar()
        self.var_fine = StringVar()
        
             
        labtitle = Label(self.root, text="  Detained Ship Information  ", relief=SOLID, font=("arial", 17, "bold"))
        labtitle.place(x=235, y=30)
            
        frame2 = Frame(self.root, bd=6, relief=GROOVE, padx=10, bg="#F3F4F6")
        frame2.place(x=90, y=90, width=620, height=320)
            
        labshipid = Label(frame2, text="Ship ID: ", font=("arial", 11, "bold"), bg="#F3F4F6", padx=2, pady=23)
        labshipid.grid(row=0, column=0, sticky=W)
        txxtshipid = Entry(frame2, textvariable=self.var_shipid, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=15)
        txxtshipid.grid(row=0, column=1)
            
        labcaptname = Label(frame2, text="Captain Name: ", font=("arial", 11, "bold"), bg="#F3F4F6", padx=2, pady=23)
        labcaptname.grid(row=1, column=0, sticky=W)
        txxtcaptname = Entry(frame2, textvariable=self.var_captname, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=15)
        txxtcaptname.grid(row=1, column=1)
            
        labshipcargo = Label(frame2, font=("arial", 11, "bold"), text="Reason:", bg="#F3F4F6", padx=2, pady=23)
        labshipcargo.grid(row=2, column=0, sticky=W)
        txxtshipcargo = Entry(frame2, textvariable=self.var_shipcargo, font=("arial", 10, "bold"), bg="white", bd=2,relief=RIDGE, width=15)
        txxtshipcargo.grid(row=2, column=1)

        labshiparrcountry = Label(frame2, font=("arial", 11, "bold"), text="Ship Arrival Country:", bg="#F3F4F6", padx=2, pady=23)
        labshiparrcountry.grid(row=3, column=0, sticky=W)
        txxtshiparrcountry = Entry(frame2, textvariable=self.var_shiparrcountry, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=15)
        txxtshiparrcountry.grid(row=3, column=1)
            
        labarrdate = Label(frame2, font=("arial", 11, "bold"), text="     Ship Arrival Date :",  bg="#F3F4F6", padx=14, pady=23)
        labarrdate.grid(row=0, column=2, sticky=W)
        txxtarrdate = Entry(frame2, textvariable=self.var_arrdate, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=18)
        txxtarrdate.grid(row=0, column=3)

        labarrtime = Label(frame2, font=("arial", 11, "bold"), text="     Time of Arrival:", bg="#F3F4F6", padx=14, pady=23)
        labarrtime.grid(row=1, column=2, sticky=W)
        txxtarrtime = Entry(frame2, textvariable=self.var_arrtime, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=18)
        txxtarrtime.grid(row=1, column=3)

        labduedate = Label(frame2, font=("arial", 11, "bold"), text="       Due Date :", bg="#F3F4F6", padx=14, pady=23)
        labduedate.grid(row=2, column=2, sticky=W)
        txxtduedate = Entry(frame2, textvariable=self.var_duedate, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=18)
        txxtduedate.grid(row=2, column=3)

        labfine = Label(frame2, font=("arial", 11, "bold"), text="       Fine :", bg="#F3F4F6", padx=14, pady=23)
        labfine.grid(row=3, column=2, sticky=W)
        txxtfine = Entry(frame2, textvariable=self.var_fine, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=18)
        txxtfine.grid(row=3, column=3)
            
        butframe1 = Frame(self.root, bd=6, relief=RIDGE, padx=5)
        butframe1.place(x=170, y=445, width=130, height=45)
        
        butnregister = Button(butframe1, command=self.register, text="Register", font=("arial", 13, "bold"), width=520,
                            bg="navy", fg="white", relief=GROOVE, padx=4)
        butnregister.pack(fill=BOTH)
            
        butframe2 = Frame(self.root, bd=6, relief=RIDGE, padx=5)
        butframe2.place(x=450, y=445, width=130, height=45)
        
        butncomplaint = Button(butframe2, command=self.send_sms("9082247211", "CAUTION,New Complaint Has Been Registered."), text="Complaint", font=("arial", 13, "bold"), width=520,
                            bg="navy", fg="white", relief=GROOVE, padx=4)
        butncomplaint.pack(fill=BOTH)
        
    def register(self):
        if self.var_shipid.get()=="" or self.var_captname.get()=="" or self.var_shipcargo.get()=="":
            messagebox.showerror("Error","All Fields are Required.")
        else:
            con = mysql.connector.connect(host="localhost", user="root", passwd="shreyas", database="mydata")
            cur = con.cursor()
            query = ("SELECT * FROM detained WHERE shippid=%s")
            value = (self.var_shipid.get(),)
            cur.execute(query, value)
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error","ShipID already Exists.")
            else:
                cur.execute("INSERT INTO detained VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_shipid.get(),
                    self.var_captname.get(),
                    self.var_shipcargo.get(),
                    self.var_shiparrcountry.get(),
                    self.var_arrdate.get(),
                    self.var_arrtime.get(),
                    self.var_duedate.get(),
                    self.var_fine.get()
                ))
                
            con.commit()
            con.close()
            
            messagebox.showinfo("Success","Information Registered Successfully.")
            
    def send_sms(self, number, message):
        url = 'https://www.fast2sms.com/dev/bulkV2'
        params = {
            'authorization': 'NdbPZCHlVcMSjg4Uxae8KGwWuX1Op0mfAJnizvE7qBrtF9hkY3bBSNWwkX9V56YvjOniqmI30roLAzup',
            'sender_id': 'TXTIND',
            'message': message,
            'language': 'english',
            'route': 'v3',
            'numbers': number    
        }
        response = requests.get(url, params=params)
        dic = response.json()
        
        print(dic)
        
        
class weather_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Information")
        self.root.geometry("700x350")
        
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        
        config_file = 'config.ini'
        config = ConfigParser()
        config.read(config_file)
        api_key = config['api_key']['key']
        
        def get_weather(city):
            result = requests.get(url.format(city, api_key))
            if result:
                json = result.json()
                city = json['name']
                country = json['sys']['country']
                temp_kelvin = json['main']['temp']
                temp_celsius = temp_kelvin - 273.15
                temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
                weather = json['weather'][0]['main']
                final = (city, country, temp_celsius, temp_fahrenheit, weather)
                return final
            else:
                return None
        
        def search():
            city = city_text.get()
            weather = get_weather(city)
            if weather:
                location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
                temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
                weather_lbl['text'] = weather[4]
            else:
                messagebox.showerror("Error","Cannot find City {}".format(city))
        
        city_text = StringVar()
        city_entry = Entry(self.root, textvariable=city_text)
        city_entry.pack()
        
        search_btn = Button(self.root, text='Search Weather', width=12, command=search)
        search_btn.pack()
        
        location_lbl = Label(self.root, text='', font=('bold', 20))
        location_lbl.pack()
        
        temp_lbl = Label(self.root, text='')
        temp_lbl.pack()
        
        weather_lbl = Label(self.root, text='')
        weather_lbl.pack()
        
class maintenance:
    def __init__(self, root):
        self.root = root
        self.root.title("Maintenance Form")
        self.root.geometry("800x560+200+42")
        
        self.variable_shipid = StringVar()
        self.variable_shipcompany = StringVar()
        self.variable_litoffuel = StringVar()
        self.variable_fuelcharges = StringVar()
        self.variable_maintenancecharges = StringVar()
        self.variable_totalcost = StringVar()
        
        lbtitle = Label(self.root, text="  Maintenance  ", relief=SOLID, font=("arial", 17, "bold"))
        lbtitle.place(x=305, y=30)
        
        frame3 = Frame(self.root, bd=6, relief=GROOVE, padx=10, bg="#F3F4F6")
        frame3.place(x=90, y=90, width=620, height=320)
        
        lbshipid = Label(frame3, text="Ship ID: ", font=("arial", 11, "bold"), bg="#F3F4F6", padx=2, pady=23)
        lbshipid.grid(row=0, column=0, sticky=W)
        textshipid = Entry(frame3, textvariable=self.variable_shipid, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=16)
        textshipid.grid(row=0, column=1)
        
        lbshipcomp = Label(frame3, font=("arial", 11, "bold"), text="Ship Company: ", bg="#F3F4F6", padx=2, pady=23)
        lbshipcomp.grid(row=1, column=0, sticky=W)
        textshipcomp = Entry(frame3, textvariable=self.variable_shipcompany, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=16)
        textshipcomp.grid(row=1, column=1)
        
        lblitoffuel = Label(frame3, font=("arial", 11, "bold"), text="Litres of Fuel: ", bg="#F3F4F6", padx=2, pady=23)
        lblitoffuel.grid(row=2, column=0, sticky=W)
        textlitoffuel = Entry(frame3, textvariable=self.variable_litoffuel, font=("arial", 10, "bold"), bg="white", bd=2,relief=RIDGE, width=16)
        textlitoffuel.grid(row=2, column=1)
        
        lbfuelcharges = Label(frame3, font=("arial", 11, "bold"), text="     Fuel Charges :", bg="#F3F4F6", padx=14, pady=23)
        lbfuelcharges.grid(row=0, column=2, sticky=W)
        textfuelcharges = Entry(frame3, textvariable=self.variable_fuelcharges, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=18)
        textfuelcharges.grid(row=0, column=3)
        
        lbmaintenancecharges = Label(frame3, font=("arial", 11, "bold"), text="     Maintenance Charges :",  bg="#F3F4F6", padx=14, pady=23)
        lbmaintenancecharges.grid(row=1, column=2, sticky=W)
        textmaintenancecharges = Entry(frame3, textvariable=self.variable_maintenancecharges, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=18)
        textmaintenancecharges.grid(row=1, column=3)
        
        lbtotalcost = Label(frame3, font=("arial", 11, "bold"), text="     Total Cost :", bg="#F3F4F6", padx=14, pady=23)
        lbtotalcost.grid(row=2, column=2, sticky=W)
        texttotalcost = Entry(frame3, textvariable=self.variable_totalcost, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=18)
        texttotalcost.grid(row=2, column=3)
        
        print_btn = Button(frame3, command=self.receipt, text="Print", font=("arial", 13, "bold"), width=15, bg="navy", fg="white", relief=GROOVE)
        print_btn.place(x=210, y=250)
        
    def receipt(self):
        pdf.set_font("Arial",size = 15)
        
        pdf.cell(200, 10, txt= "RECEIPT", ln=1, align="C")
        pdf.cell(200, 10, txt="Ship ID :- " + self.variable_shipid.get(), ln=2, align="L")
        pdf.cell(200, 10, txt="Ship Company :- " + self.variable_shipcompany.get(), ln=3, align="L")
        pdf.cell(200, 10, txt="Litres of Fuel :- " + self.variable_litoffuel.get(), ln=4, align="L")
        pdf.cell(200, 10, txt="Fuel Charges :- " + self.variable_fuelcharges.get(), ln=5, align="L")
        pdf.cell(200, 10, txt="Maintenance Charges :- " + self.variable_maintenancecharges.get(), ln=6, align="L")
        pdf.cell(200, 10, txt="Total Cost :- " + self.variable_totalcost.get(), ln=7, align="L")
        
        filename = "receipt"
        pdf.output(filename+".pdf")
           
        
if __name__ == "__main__":
    main()
  