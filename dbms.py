import pymysql
from datetime import datetime
from tabulate import tabulate
import random
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

conn=pymysql.connect(host='localhost',user='root',password='root',database='dbmsproject')
a=conn.cursor()


def ContactUs():
    def Upload():
        Text1=intboxCU1.get()
        Text2=intboxCU2.get(1.0,"end-1c")
        
        if Text1=='':
            Text1="Anomalous"
            
        if Text2=='':
            print("Enter suggestion")
            labelCU.config(text="Enter Suggestion/Issue",fg='red')

        else:
            print("Uploaded")
            a.execute("insert into Suggestions values('"+str(Text1)+"','"+str(Text2)+"');")
            conn.commit()
            buttonCU2.place_forget()
            labelCU.config(text="THANK YOU FOR THE SUGGESTION/PROBLEM!!!",fg='green')
            print("THANK YOU FOR THE SUGGESTION/PROBLEM")
        
    win1=Tk()
    win1.title("Contact Us")
    win1.geometry("500x500")
    Label(win1,text="TELL US ABOUT YOUR ISSUE OR SUGGESTION",font=('Caveat 16 bold')).place(x=10,y=2)
    Label(win1,text="Name : ",font=('Caveat 10')).place(x=10,y=50)
    Label(win1,text="Suggestion : ",font=('Caveat 10')).place(x=10,y=80)
    intboxCU1=ttk.Entry(win1)
    intboxCU1.place(x=100,y=50)
    intboxCU2=Text(win1,height=5,width=40)
    intboxCU2.place(x=100,y=80)
    buttonCU1=ttk.Button(win1,text="Close",command=win1.destroy)
    buttonCU1.place(x=260,y=450)
    buttonCU2=ttk.Button(win1,text="Submit",command=Upload)
    buttonCU2.place(x=180,y=450)
    labelCU=Label(win1,text="",font=('Caveat 10 bold'))
    labelCU.place(x=10,y=200)
    print()
    print()



def Register():
    def Upload():
        First_Name=intboxR1.get()
        Last_Name=intboxR2.get()

        if First_Name=='':
            print("Invalid First Name")
            LabelR.config(text="Invalid First Name",fg='red')

        elif Last_Name=='':
            print("Invalid Last Name")
            LabelR.config(text="Invalid Last Name",fg='red')

        else:
            Status="FormFill"
            Pid=random.randint(1,99999)
            l=[]
            a.execute("select pid from player;")
            conn.commit()
            data=a.fetchall()
            
            for i in data:
                for j in i:
                    l.append(j)

            i=0
            while Pid in l:
                Pid=random.randint(1,99999)
                i=i+1
                
                if(i>=5):
                    try:
                        Pid=int(input("Enter Pid : "))
                        
                    except:
                        print("Invalid Pid")
                        return
                
            a.execute("insert into player(Pid,First_Name,Last_Name,Status) values("+str(Pid)+",'"+str(First_Name)+"','"+str(Last_Name)+"','"+str(Status)+"');")
            conn.commit()
            LabelR.config(text="ACCOUNT CREATED SUCCESSFULLY",fg='green')
            LabelR1=Label(win1,text="YOUR PID IS : "+str(Pid),font=('Caveat 10 bold'),fg='green')
            LabelR1.place(x=10,y=230)
            LabelR2=Label(win1,text="PID is needed to Login",font=('Caveat 10 bold'),fg='green')
            LabelR2.place(x=10,y=260)
            buttonR2.place_forget()
            print()
            print("Your Pid is : ",Pid)
            print("ACCOUNT CREATED SUCCESSFULLY")          
            print()

                    
    win1=Tk()
    win1.title("Register")
    win1.geometry("500x500")
    Label(win1,text="REGISTRATION",font=('Caveat 16 bold')).place(x=10,y=2)
    Label(win1,text="First_Name : ",font=('Caveat 10')).place(x=10,y=50)
    Label(win1,text="Last_Name : ",font=('Caveat 10')).place(x=10,y=80)
    LabelR=Label(win1,text="",font=('Caveat 10 bold'))
    LabelR.place(x=10,y=200)
    intboxR1=ttk.Entry(win1)
    intboxR1.place(x=100,y=50)
    intboxR2=ttk.Entry(win1)
    intboxR2.place(x=100,y=80)
    buttonR1=ttk.Button(win1,text="Close",command=win1.destroy)
    buttonR1.place(x=260,y=450)
    buttonR2=ttk.Button(win1,text="Submit",command=Upload)
    buttonR2.place(x=180,y=450)
    

def Login():
    def PressLogin():
        global Pid
        def UpdateProfile():
            def Update():
                print("Update")
                First_Name=intboxLPU1.get()
                Last_Name=intboxLPU2.get()
                Gender=intboxLPU3.get()
                Weight=intboxLPU4.get()
                Height=intboxLPU5.get()
                Age=intboxLPU6.get()
                Eid=intboxLPU7.get()
                
                if First_Name=='':
                    a.execute("select First_Name from player where Pid="+str(Pid)+";")
                    conn.commit()
                    data=a.fetchall()
                    l=[]
                    for i in data:
                        for j in i:
                            l.append(j)
                    First_Name=l[0]

                if Last_Name=='':
                    a.execute("select Last_Name from player where Pid="+str(Pid)+";")
                    conn.commit()
                    data=a.fetchall()
                    l=[]
                    for i in data:
                        for j in i:
                            l.append(j)
                    Last_Name=l[0]
                    
                if Gender=='Male' or Gender=='M':
                    Gender='M'
                    labelLPUtmp.config(text="",fg="red")
                    
                elif Gender=='Female' or Gender=='F':
                    Gender='F'
                    labelLPUtmp.config(text="",fg="red")
                    
                elif Gender=='':
                    a.execute("select Gender from player where Pid="+str(Pid)+";")
                    conn.commit()
                    data=a.fetchall()
                    l=[]
                    for i in data:
                        for j in i:
                            l.append(j)
                    Gender=l[0]
                    labelLPUtmp.config(text="",fg="red")
                       
                else:
                    a.execute("select Gender from player where Pid="+str(Pid)+";")
                    conn.commit()
                    data=a.fetchall()
                    l=[]
                    for i in data:
                        for j in i:
                            l.append(j)
                    Gender=l[0]
                    labelLPUtmp.config(text="Invalid Gender",fg="red")

                if Weight=='':
                    a.execute("select Weight from player where Pid="+str(Pid)+";")
                    conn.commit()
                    data=a.fetchall()
                    l=[]
                    for i in data:
                        for j in i:
                            l.append(j)
                    Weight=l[0]

                if Height=='':
                    a.execute("select Height from player where Pid="+str(Pid)+";")
                    conn.commit()
                    data=a.fetchall()
                    l=[]
                    for i in data:
                        for j in i:
                            l.append(j)
                    Height=l[0]

                if Age=='':
                    a.execute("select Age from player where Pid="+str(Pid)+";")
                    conn.commit()
                    data=a.fetchall()
                    l=[]
                    for i in data:
                        for j in i:
                            l.append(j)
                    Age=l[0]

                if Eid=='':
                    a.execute("select Eid from player where Pid="+str(Pid)+";")
                    conn.commit()
                    data=a.fetchall()
                    l=[]
                    for i in data:
                        for j in i:
                            l.append(j)
                    Eid=l[0]

                try:
                    Weight=float(Weight)
                except:
                    labelLPUtmp.config(text="Invalid Weight",fg="red")

                try:
                    Height=float(Height)
                except:
                    labelLPUtmp.config(text="Invalid Height",fg="red")

                try:
                    Age=int(Age)
                except:
                    labelLPUtmp.config(text="Invalid Age",fg="red")

                try:
                    Eid=int(Eid)
                except:
                    labelLPUtmp.config(text="Invalid Eid",fg="red")

                a.execute("select Eid from event;")
                conn.commit()
                data=a.fetchall()
                l=[]
                for i in data:
                    for j in i:
                        l.append(j)
                        
                if(Eid in l):
                    labelLPUtmp.config(text="Updated Successfully",fg="green")
                    Status='Pending'
                    a.execute("Update player set First_Name='"+str(First_Name)+"',Last_Name='"+str(Last_Name)+"',Gender='"+str(Gender)+"',Weight="+str(Weight)+",Height="+str(Height)+",Age="+str(Age)+",Status='"+str(Status)+"',Eid="+str(Eid)+" where Pid="+str(Pid)+";")
                    conn.commit()
                    buttonLPU1.place_forget()
                    
                else:
                    labelLPUtmp.config(text="Eid Not Found",fg="red")


            global Pid
            print("Update Profile")
            labelL3.place_forget()
            buttonL3.place_forget()
            labelL4.place_forget()
            buttonL4.place_forget()
            labelL5.place_forget()
            buttonL5.place_forget()
            buttonL1.place_forget()
            buttonL2.place_forget()
            
            labelLPU1=Label(win1,text="First Name : ",font=('Caveat 10'))
            labelLPU1.place(x=10,y=120)
            intboxLPU1=ttk.Entry(win1)
            intboxLPU1.place(x=100,y=120)
            labelLPU2=Label(win1,text="Last Name : ",font=('Caveat 10'))
            labelLPU2.place(x=10,y=150)
            intboxLPU2=ttk.Entry(win1)
            intboxLPU2.place(x=100,y=150)
            labelLPU3=Label(win1,text="Gender : ",font=('Caveat 10'))
            labelLPU3.place(x=10,y=180)
            intboxLPU3=ttk.Entry(win1)
            intboxLPU3.place(x=100,y=180)
            labelLPU4=Label(win1,text="Weight : ",font=('Caveat 10'))
            labelLPU4.place(x=10,y=210)
            intboxLPU4=ttk.Entry(win1)
            intboxLPU4.place(x=100,y=210)
            labelLPU5=Label(win1,text="Height : ",font=('Caveat 10'))
            labelLPU5.place(x=10,y=240)
            intboxLPU5=ttk.Entry(win1)
            intboxLPU5.place(x=100,y=240)
            labelLPU6=Label(win1,text="Age : ",font=('Caveat 10'))
            labelLPU6.place(x=10,y=270)
            intboxLPU6=ttk.Entry(win1)
            intboxLPU6.place(x=100,y=270)
            labelLPU7=Label(win1,text="Eid : ",font=('Caveat 10'))
            labelLPU7.place(x=10,y=300)
            intboxLPU7=ttk.Entry(win1)
            intboxLPU7.place(x=100,y=300)
            buttonLPU1=ttk.Button(win1,text="Update",command=Update)
            buttonLPU1.place(x=100,y=400)
            labelLPUtmp=Label(win1,text="",font=('Caveat 16 bold'))
            labelLPUtmp.place(x=10,y=400)
            
            buttonLPU2=ttk.Button(win1,text="Close",command=win1.destroy)
            buttonLPU2.place(x=260,y=450)

            
        def DeleteAccount():
            def Delete():
                global Pid
                print("Deleted")
                a.execute("Delete from player where pid="+str(Pid)+";")
                conn.commit()
                a.execute("Delete from approval where pid="+str(Pid)+";")
                conn.commit()
                LabelDA1.config(text="Account Deleted",fg='green')
                buttonLA2.place_forget()
                buttonLA3.config(text="Close")
                
            print("Delete Account")
            labelL3.place_forget()
            buttonL3.place_forget()
            labelL4.place_forget()
            buttonL4.place_forget()
            labelL5.place_forget()
            buttonL5.place_forget()
            buttonL1.place_forget()
            buttonL2.place_forget()
            LabelDA1=Label(win1,text="Are You Sure?",font=('Caveat 16 bold'),fg='red')
            LabelDA1.place(x=180,y=100)
            buttonLA2=ttk.Button(win1,text="Confirm",command=Delete)
            buttonLA2.place(x=180,y=450)
            buttonLA3=ttk.Button(win1,text="Cancel",command=win1.destroy)
            buttonLA3.place(x=260,y=450)

            
        def Acknowledgement():
            print("Acknowledgement")
            labelL3.place_forget()
            buttonL3.place_forget()
            labelL4.place_forget()
            buttonL4.place_forget()
            labelL5.place_forget()
            buttonL5.place_forget()
            buttonL1.place_forget()
            buttonL2.place_forget()
            
            a.execute("select Eid from player where Pid="+str(Pid)+";")
            conn.commit()
            data=a.fetchall()
            l=[]
            for i in data:
                for j in i:
                    l.append(j)
            Eid=l[0]

            a.execute("Select First_Name,Last_Name,Gender,Weight,Height,Age,Event_Name from player,event where Pid="+str(Pid)+" and player.Eid=event.Eid;")
            conn.commit()
            data=a.fetchall()
            count=0
            Label(win1,text="First_Name Last_Name Gender Weight Height Age Event_Name ",font=('Caveat 10 bold')).place(x=10,y=100)
            for i in data:
                labelVE=Label(win1,text=i,font=('Caveat 10'))
                labelVE.place(x=10,y=130+30*count)
                count=count+1
            buttonLPU2=ttk.Button(win1,text="Close",command=win1.destroy)
            buttonLPU2.place(x=260,y=450)
            print(tabulate(data,headers=['First_Name','Last_Name','Gender','Weight','Height','Age','Event_Name']))
            print()

            
            
        print("Login:")
        Pid=intboxL1.get()
        if Pid=='':
            print("Invalid PID")
            LabelL.config(text="Invalid Pid",fg="red")

        elif Pid=='admin':
            print("ADMIN")
            LabelL.config(text="ADMIN LOGIN",fg="red")
            Admin()


        else:
            try:
                Pid=int(Pid)
                    
            except:
                print("Invalid Pid")
                LabelL.config(text="Invalid Pid",fg="red")
                return
                    
            l=[]
            a.execute("select pid from player;")
            conn.commit()
            data=a.fetchall()
            for i in data:
                for j in i:
                    l.append(j)

            if Pid in l:
                print("Welcome")
                LabelL.config(text="")
                LabelL1.config(text="PID : ")
                intboxL1.place_forget()
                buttonL2.place_forget()
                Label(win1,text=Pid,font=('Caveat 10')).place(x=70,y=30)
                Label(win1,text="WELCOME",fg="green",font=('Caveat 16 bold')).place(x=200,y=60)
                a.execute("select status from player where pid="+str(Pid)+";")
                conn.commit()
                data=a.fetchall()
                l=[]
                for i in data:
                    for j in i:
                        l.append(j)
                        
                if(l[0]=="FormFill"):
                    color1="red"
                    
                elif(l[0]=="Pending"):
                    color1="yellow"
                    
                elif(l[0]=="Approved"):
                    color1="green"
                    
                Label(win1,text="Status :",font=('Caveat 10 bold')).place(x=350,y=30)
                Label(win1,text=l[0],fg=color1,font=('Caveat 10 bold')).place(x=400,y=30)
                buttonL1.config(text="Logout")

                
                labelL3=Label(win1,text="Update Profile : ",font=('Caveat 10'))
                labelL3.place(x=10,y=90)
                buttonL3=ttk.Button(win1,text="UpdateProfile",command=UpdateProfile)
                buttonL3.place(x=120,y=90)
                
                labelL4=Label(win1,text="Delete Account : ",font=('Caveat 10'))
                labelL4.place(x=10,y=120)
                buttonL4=ttk.Button(win1,text="DeleteAccount",command=DeleteAccount)
                buttonL4.place(x=120,y=120)

                labelL5=Label(win1,text="Acknowledgement : ",font=('Caveat 10'))
                labelL5.place(x=10,y=150)
                buttonL5=ttk.Button(win1,text="Acknowledgement",command=Acknowledgement)
                buttonL5.place(x=120,y=150)

            else:
                LabelL.config(text="Pid not found",fg="red")

                
    def Admin():
        def Approval():
            def UpdateAdm():
                Pid=intboxR1.get()
                Eid=intboxR2.get()
                Cid=intboxR3.get()
                Lid=intboxR4.get()
                try:
                    Pid=int(Pid)
                    Cid=int(Cid)
                    Eid=int(Eid)
                    Lid=int(Lid)
                    Time=datetime.now()
                    Year=datetime.now().year
                    Month=datetime.now().month
                    Date=datetime.now().day
                    Time=str(Year)+'-'+str(Month)+'-'+str(Date)
                    a.execute("insert into approval values("+str(Pid)+",'"+str(Time)+"',"+str(Cid)+","+str(Eid)+","+str(Lid)+");")
                    conn.commit()
                    Status="Approved"
                    a.execute("update player set Status='"+str(Status)+"' where Pid="+str(Pid)+";")
                    conn.commit()
                    print("Updated Successfully")
                    LabelL.config(text="Updated Successfully",fg="green")
                except:
                    LabelL.config(text="Error Updating",fg="red")
                    
            print("Approval")
            LabelA1.place_forget()
            LabelA3.place_forget()
            buttonA1.place_forget()
            buttonA3.place_forget()
            a.execute("Select Pid,First_Name,Last_Name,Eid,Age from player where Status='Pending';")
            conn.commit()
            data=a.fetchall()
            count=0
            Label(win1,text="Pid First_Name Last_Name Eid Age",font=('Caveat 10 bold')).place(x=280,y=30)
            for i in data:
                labelVE=Label(win1,text=i,font=('Caveat 10'))
                labelVE.place(x=280,y=50+30*count)
                count=count+1
            print(tabulate(data,headers=['Pid','First_Name','Last_Name','Eid','Age']))
            print()
            buttonA4=ttk.Button(win1,text="Update",command=UpdateAdm)
            buttonA4.place(x=10,y=170)
            Label(win1,text="Pid : ",font=('Caveat 10')).place(x=10,y=50)
            Label(win1,text="Eid : ",font=('Caveat 10')).place(x=10,y=80)
            Label(win1,text="Cid : ",font=('Caveat 10')).place(x=10,y=110)
            Label(win1,text="Lid : ",font=('Caveat 10')).place(x=10,y=140)
            LabelR=Label(win1,text="",font=('Caveat 10 bold'))
            LabelR.place(x=10,y=200)
            intboxR1=ttk.Entry(win1)
            intboxR1.place(x=100,y=50)
            intboxR2=ttk.Entry(win1)
            intboxR2.place(x=100,y=80)
            intboxR3=ttk.Entry(win1)
            intboxR3.place(x=100,y=110)
            intboxR4=ttk.Entry(win1)
            intboxR4.place(x=100,y=140)
                                         
        def Medal():
            def UpdateAd():
                Pid=intboxR1.get()
                Eid=intboxR2.get()
                Cid=intboxR3.get()
                Medal=intboxR4.get()
                try:
                    Pid=int(Pid)
                    Eid=int(Eid)
                    Cid=int(Cid)
                    a.execute("Insert into medal values("+str(Pid)+",'"+str(Medal)+"',"+str(Cid)+","+str(Eid)+");")
                    conn.commit()
                    print("Updated Successfully")
                    LabelL.config(text="Updated Successfully",fg="green")
                    buttonA4.place_forget()
                except:
                    print("Error Updating")
                    LabelL.config(text="Error Updating",fg="red")
                    
                    
            print("Medal")
            LabelA1.place_forget()
            LabelA3.place_forget()
            buttonA1.place_forget()
            buttonA3.place_forget()
            a.execute("Select Pid,First_Name,Last_Name,Eid from player;")
            conn.commit()
            data=a.fetchall()
            count=0
            Label(win1,text="Pid First_Name Last_Name Eid",font=('Caveat 10 bold')).place(x=300,y=30)
            for i in data:
                labelVE=Label(win1,text=i,font=('Caveat 10'))
                labelVE.place(x=300,y=50+30*count)
                count=count+1
            print(tabulate(data,headers=['Pid','First_Name','Last_Name','Eid']))
            print()

            Label(win1,text="Pid : ",font=('Caveat 10')).place(x=10,y=50)
            Label(win1,text="Eid : ",font=('Caveat 10')).place(x=10,y=80)
            Label(win1,text="Cid : ",font=('Caveat 10')).place(x=10,y=110)
            Label(win1,text="Medal : ",font=('Caveat 10')).place(x=10,y=140)
            LabelR=Label(win1,text="",font=('Caveat 10 bold'))
            LabelR.place(x=10,y=200)
            intboxR1=ttk.Entry(win1)
            intboxR1.place(x=100,y=50)
            intboxR2=ttk.Entry(win1)
            intboxR2.place(x=100,y=80)
            intboxR3=ttk.Entry(win1)
            intboxR3.place(x=100,y=110)
            intboxR4=ttk.Entry(win1)
            intboxR4.place(x=100,y=140)
            buttonA4=ttk.Button(win1,text="Update",command=UpdateAd)
            buttonA4.place(x=10,y=170)
            
        print("Admin")
        intboxL1.place_forget()
        buttonL2.place_forget()
        Label(win1,text="ADMIN",font=('Caveat 10 bold'),fg="red").place(x=80,y=30)
        LabelA1=Label(win1,text="Approval : ",font=('Caveat 10'))
        LabelA3=Label(win1,text="Update Medals : ",font=('Caveat 10'))
        LabelA1.place(x=10,y=60)
        LabelA3.place(x=10,y=90)
        buttonA1=ttk.Button(win1,text="Approval",command=Approval)
        buttonA3=ttk.Button(win1,text="Medal",command=Medal)
        buttonA1.place(x=100,y=60)
        buttonA3.place(x=100,y=90)

    
    win1=Tk()
    win1.title("Login")
    win1.geometry("500x500")
    Label(win1,text="LOGIN",font=('Caveat 16 bold')).place(x=10,y=2)
    LabelL1=Label(win1,text="Enter PID : ",font=('Caveat 10'))
    LabelL1.place(x=10,y=30)
    intboxL1=ttk.Entry(win1)
    intboxL1.place(x=100,y=30)
    buttonL1=ttk.Button(win1,text="Close",command=win1.destroy)
    buttonL1.place(x=260,y=450)
    buttonL2=ttk.Button(win1,text="Login",command=PressLogin)
    buttonL2.place(x=180,y=450)
    LabelL=Label(win1,text="",font=('Caveat 16 bold'))
    LabelL.place(x=10,y=420)


def ViewEvents():
    win1=Tk()
    win1.title("View Events")
    win1.geometry("500x500")

    a.execute("select event.Eid,category.Category_Name,event.Event_Name,event.Year,event.Season,location.City,location.Country from category,event,location where category.Eid=event.Eid and category.Eid=location.Eid;")
    conn.commit()
    data=a.fetchall()
    count=0
    Label(win1,text="VIEW EVENTS",font=('Caveat 16 bold')).place(x=10,y=2)
    Label(win1,text="Eid Category_Name Event_Name Year Season City Country",font=('Caveat 10 bold')).place(x=10,y=30)
    for i in data:
        labelVE=Label(win1,text=i,font=('Caveat 10'))
        labelVE.place(x=10,y=50+30*count)
        count=count+1
        
    print(tabulate(data,headers=['Eid','CategoryName','EventName','Year','Season','City','Country']))
    print()
    buttonVE=ttk.Button(win1,text="Close",command=win1.destroy)
    buttonVE.place(x=210,y=450)
    

def HallOfFame():
    win1=Tk()
    win1.title("Hall Of Fame")
    win1.geometry("500x500")
    a.execute("Select player.First_Name,player.Last_Name,medal.Medal_Won,event.Event_Name from player,medal,event where medal.Pid=player.Pid and player.Eid=event.Eid;")
    #a.execute("Select * from event;")
    conn.commit()
    data=a.fetchall()
    count=0
    Label(win1,text="HALL OF FAME",font=('Caveat 16 bold')).place(x=10,y=2)
    Label(win1,text="First_Name Last_Name Medel_Won Event_Name",font=('Caveat 10 bold')).place(x=10,y=30)
    
    for i in data:
        labelHOF=Label(win1,text=i,font=('Caveat 10'))
        labelHOF.place(x=10,y=50+30*count)
        count=count+1
        
    print(tabulate(data,headers=['First_Name','Last_Name','Medal_Won','Event']))
    print()
    buttonHOF=ttk.Button(win1,text="Close",command=win1.destroy)
    buttonHOF.place(x=210,y=450)


def End():
    conn.commit()
    win.destroy()
    exit(0)




win=Tk()
win.geometry("500x500")
win.title("DBMS")
Label(win,text="OLYMPIC MANAGEMENT SYSTEM",font=('Caveat 16 bold')).place(x=80,y=2)
label1=Label(win,text="Register : ",font=('Caveat 16'))
label2=Label(win,text="Login : ",font=('Caveat 16'))
label3=Label(win,text="View Events : ",font=('Caveat 16'))
label4=Label(win,text="Contact Us : ",font=('Caveat 16'))
label5=Label(win,text="Hall Of Fame : ",font=('Caveat 16'))
label6=Label(win,text="Save and Exit : ",font=('Caveat 16'))

label1.place(x=10,y=50)
label2.place(x=10,y=80)
label3.place(x=10,y=110)
label4.place(x=10,y=140)
label5.place(x=10,y=170)
label6.place(x=10,y=200)

button1=ttk.Button(win,text="Register",command=Register)    #DONE
button2=ttk.Button(win,text="Login",command=Login)          #
button3=ttk.Button(win,text="Events",command=ViewEvents)    #DONE
button4=ttk.Button(win,text="Suggestion",command=ContactUs) #DONE
button5=ttk.Button(win,text="HOF",command=HallOfFame)       #DONE
button6=ttk.Button(win,text="Exit",command=End)             #DONE

button1.place(x=200,y=50)
button2.place(x=200,y=80)
button3.place(x=200,y=110)
button4.place(x=200,y=140)
button5.place(x=200,y=170)
button6.place(x=200,y=200)

win.mainloop()
