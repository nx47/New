#Cemetery Management System


import matplotlib.pyplot as mpt
from tabulate import tabulate
import mysql.connector as ms
import csv
import os
from datetime import datetime




con=ms.connect(host='localhost',user='root',password='root',database='hhw')
cursor=con.cursor()




def signup():
    f1=open("user1.csv",'a+',newline='')
    f2=open("user1.csv",'r',newline='')
    name=input("Enter your name: ")
    user=input("Enter a username: ")
    usr=csv.reader(f2)
    fnn=0
    for i in usr:
        
        if i[1]==user:
            print("\033[1mOops...Username Already Taken\033[0m")
            fnn=2
            break
        
    if fnn!=2:
        password=input("Enter a password")
        w=csv.writer(f1)
        data=[name,user,password]
        w.writerow(data)
        
        print()
        print("\033[1mSign Up Successfull\033[0m")
        print()
        print("\033[1mHello",name,"!!!\033[0m")
        f1.close()
        f2.close()
        menu()




      
      
def forgot():
    f1=open("user1.csv",'r+',newline='')
    f2=open("usertemp.csv",'w',newline='')
    usr=csv.reader(f1)
    w=csv.writer(f2)
    name=input("Enter your name")
    user=input("Enter your username")
    for i in usr:
        if i[0]==name and i[1]==user:
            pasd=input("Enter new password")
            i[2]=pasd
            nw=[name,user,pasd]
            w.writerow(nw)
            print()
            print("\033[1mPassword changed succesfully\033[0m")
            print("\033[1mHello",i[0],"!!!\033[0m")
        
        else:
            w.writerow(i)
                
    f2.close()
    f1.close()
    file='user1.csv'
    os.remove(file)
    os.rename('usertemp.csv',file)
    
    
    
            
            
            
            

def login():
    f=open("user1.csv",'r')
    usr=csv.reader(f)
    userr=input("Enter your username")
    flag=0
    for i in usr:
        if i[1]==userr:
            pwd=input("Enter password")
            if i[2]==pwd:
                print("\033[1mSuccessfully Logged In\033[0m")
                print()
                print("\033[1mHello",i[0],"!!!\033[0m")
                flag=1
                
            else:
                print()              
                print("\033[1mIncorrect Password\033[0m")
                print()
                print("\033[1m1.Try Again\033[0m")
                print("\033[1m2.Reset Password\033[0m")
                print()
                cho=int(input("Select Your Choice"))
                
                if cho==1:
                    login()
                elif cho==2:
                    f.close()
                    forgot()
                    flag=1
                    f.close()
                    print()
                    break
                else:
                    print("\033[1mInvalid Choice\033[0m")
                
                               
    
    if flag==1:
        menu()
        
    elif flag==0:
        print("\033[1mUser Not Found\033[0m")
    

    
              
                



def createcemetery():
    try:
        q="create table cemetery(GraveNo int primary key,Name varchar(20),Gender varchar(1),DateOfBirth date,DateOfDeath date,MOFNo int REFERENCES mode(MOFNo),CODNo int REFERENCES cause(CODNo),Location varchar(25))"
        cursor.execute(q)
        con.commit()
        print("\033[1mTable Successfully Created\033[0m")
    except Exception as e:
        print('\033[1m'+str(e)+'\033[0m')
        
        ans=input("\nDo you want to drop the existing table?\n(y/n): ")
        if ans=='y':
            qu="drop table cemetery"
            cursor.execute(qu)
            print("\033[1mTable Dropped Successfully\033[0m")
            
            q="create table cemetery(GraveNo int primary key,Name varchar(20),Gender varchar(1),DateOfBirth date,DateOfDeath date,MOFNo int REFERENCES mode(MOFNo),CODNo int REFERENCES cause(CODNo),Location varchar(25))"
            cursor.execute(q)
            con.commit()
            print()
            print()
            print("\033[1mNew Table Successfully Created\033[0m")




def createmode():
    try:
        q="create table mode(MOFNo int primary key,MOF varchar(25))"
        cursor.execute(q)
        con.commit()
        print("\033[1mTable Successfully Created\033[0m")
    except Exception as e:
        print('\033[1m'+str(e)+'\033[0m')
        
        ans=input("\nDo you want to drop the existing table?\n(y/n): ")
        if ans=='y':
            qu="drop table mode"
            cursor.execute(qu)
            print("\033[1mTable Dropped Successfully\033[0m")
            
            q="create table mode(MOFNo int primary key,MOF varchar(25))"
            cursor.execute(q)
            con.commit()
            print()
            print()
            print("\033[1mNew Table Successfully Created\033[0m")
            
            
            
            
            
def createcause():
    try:
        q="create table cause(CODNo int primary key,COD varchar(20))"
        cursor.execute(q)
        con.commit()
        print("\033[1mTable Successfully Created\033[0m")
    except Exception as e:
        print('\033[1m'+str(e)+'\033[0m')
        
        ans=input("\nDo you want to drop the existing table?\n(y/n): ")
        if ans=='y':
            qu="drop table cause"
            cursor.execute(qu)
            print("\033[1mTable Dropped Successfully\033[0m")
            
            q="create table cause(CODNo int primary key,COD varchar(20))"
            cursor.execute(q)
            con.commit()
            print()
            print()
            print("\033[1mNew Table Successfully Created\033[0m")
            
            
            
            
def create():
    text1="""\033[1mCreate:\033[0m"""
    text2="""1.Cemetery Table\n2.Mode Of Funeral Table\n3.Cause Of Death Table\n4.Exit to main menu"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        createcemetery()
    elif ch==2:
        createmode()
    elif ch==3:
        createcause()
    elif ch==4:
        print("""\033[1mExiting...\n\033[0m""")
    else:
        print("\033[1mInvalid Choice !!\033[0m")
    



def insertcemetery():
    gno=int(input("Grave number: "))
    na=input("Name of the deceased person: ")
    gen=input("Gender (M\F): ")
    dob=input("Date Of Birth (in 'YYYY-MM-DD' format): ")
    dod=input("Date Of Death (in 'YYYY-MM-DD' format): ")
    mof=int(input("Mode Of Funeral SlNo.: "))
    cod=int(input("Cause Of Death Slno: "))
    loc=input("Location: ")
    
    q="insert into cemetery values({},'{}','{}','{}','{}',{},{},'{}')".format(gno,na,gen,dob,dod,mof,cod,loc)
    cursor.execute(q)
    con.commit()
    print()
    
    print("\033[1mOne record added successfully\033[0m")
    
    
    

def insertmode():
    mno=int(input("Mode Of Funeral No.: "))
    mod=input("Mode Of Funeral: ")
    
    q="insert into mode values({},'{}')".format(mno,mod)
    cursor.execute(q)
    con.commit()
    print()
    
    print("\033[1mOne record added successfully\033[0m")    
    

def insertcause():
    cno=int(input("Cause Of Death No.: "))
    cod=input("Cause Of Death: ")
    
    q="insert into cause values({},'{}')".format(cno,cod)
    cursor.execute(q)
    con.commit()
    print()
    
    print("\033[1mOne record added successfully\033[0m")    
    
    
    
def insert():
    text1="""\033[1mInsert Into:\033[0m"""
    text2="""1.Cemetery Table\n2.Mode Of Funeral Table\n3.Cause Of Death Table\n4.Exit to main menu"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        insertcemetery()
    elif ch==2:
        insertmode()
    elif ch==3:
        insertcause()
    elif ch==4:
        print("""\033[1mExiting...\n\033[0m""")
    else:
        print("\033[1mInvalid Choice !!\033[0m")




def displayall():
    cursor.execute(" select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno")
    data=cursor.fetchall()
    print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
 
 
 
def displaycemetery():
    cursor.execute(" select * from cemetery")
    data=cursor.fetchall()
    print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mCODNo.\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
    


def displaymode():
    cursor.execute(" select * from mode")
    data=cursor.fetchall()
    print(tabulate(data,headers=['\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m'],tablefmt='grid'))
   
   

def displaycause():
    cursor.execute(" select * from cause")
    data=cursor.fetchall()
    print(tabulate(data,headers=['\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m'],tablefmt='grid'))
    




def display():
    text1="""\033[1mDisplay:\033[0m"""
    text2="""1.All Details\n2.Cemetery Table\n3.Mode Of Funeral Table\n4.Cause Of Death Table\n5.Exit to main menu"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        displayall()
    elif ch==2:
        displaycemetery()
    elif ch==3:
        displaymode()
    elif ch==4:
        displaycause()
    elif ch==5:
        print("""\033[1mExiting...\n\033[0m""")
    else:
        print("\033[1mInvalid Choice !!\033[0m")



def grave():
    no=int(input("Enter the Grave No.:"))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(no)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))

        


def name():
    name=input("Enter Name:")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and name like '%{}%'".format(name)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))




def gender():
    gen=input("Enter Gender (M/F):")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and gender='{}'".format(gen)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
    




def dob():
    dob=input("Enter Date Of Birth (in 'YYYY-MM-DD' format):")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and DateOfBirth='{}'".format(dob)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))





def dod():
    dod=input("Enter Date Of Death (in 'YYYY-MM-DD' format):")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and DateOfDeath='{}'".format(dod)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))





def location():
    loc=input("Enter Location:")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and Location='{}'".format(loc)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))





def mofno():
    mno=int(input("Enter the MOF No.:"))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and c.mofno={}".format(mno)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))

     
     
     
def codno():
    cno=int(input("Enter the COD No.:"))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and c.codno={}".format(cno)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))

        



def search():
    text1="""\033[1mSearch based on:\033[0m"""
    text2="""1.Grave no.\n2.Name\n3.Gender\n4.Date Of Birth\n5.Date Of Death\n6.Location\n7.MOF No.\n8.COD No.\n9.Exit To Main Menu"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        grave()
    elif ch==2:
        name()
    elif ch==3:
        gender()
    elif ch==4:
        dob()
    elif ch==5:
        dod()
    elif ch==6:
        location()
    elif ch==7:
        mofno()
    elif ch==8:
        codno()
    elif ch==9:
        print("""\033[1mExiting...\n\033[0m""")
    else:
        print("\033[1mInvalid Choice !!\033[0m")
        
        
    
    



def uname():
    g=int(input("Enter the grave no.: "))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        print()
        m=input("Enter the new name")
        qu="update cemetery set name='{}' where graveno={}".format(m,g)
        cursor.execute(qu)
        con.commit()
        q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
        cursor.execute(q)
        data=cursor.fetchall()
        print()
        print("\033[1mName Successfully Changed to:\033[0m",m)
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        




def ugender():
    g=int(input("Enter the grave no.: "))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        print()
        m=input("Enter the updated gender (M/F) ")
        qu="update cemetery set gender='{}' where graveno={}".format(m,g)
        cursor.execute(qu)
        con.commit()
        q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
        cursor.execute(q)
        data=cursor.fetchall()
        print()
        print("\033[1mGender Successfully Changed to:\033[0m",m)
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        





def udob():
    g=int(input("Enter the grave no.: "))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        print()
        m=input("Enter new date of birth (in 'YYYY-MM-DD' format): ")
        qu="update cemetery set dateofbirth='{}' where graveno={}".format(m,g)
        cursor.execute(qu)
        con.commit()
        q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
        cursor.execute(q)
        data=cursor.fetchall()
        print()
        print("\033[1mDate Of Birth Successfully Changed to:\033[0m",m)
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        




def udod():
    g=int(input("Enter the grave no.: "))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        print()
        m=input("Enter new date of death (in 'YYYY-MM-DD' format): ")
        qu="update cemetery set dateofdeath='{}' where graveno={}".format(m,g)
        cursor.execute(qu)
        con.commit()
        q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
        cursor.execute(q)
        data=cursor.fetchall()
        print()
        print("\033[1mDate Of Death Successfully Changed to:\033[0m",m)
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))





def ulocation():
    g=int(input("Enter the grave no.: "))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        print()
        m=input("Enter new location: ")
        qu="update cemetery set location='{}' where graveno={}".format(m,g)
        cursor.execute(qu)
        con.commit()
        q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
        cursor.execute(q)
        data=cursor.fetchall()
        print()
        print("\033[1mLocation Successfully Changed to:\033[0m",m)
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        
    

def umof():
    g=int(input("Enter the grave no.: "))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        print()
        m=int(input("Enter new MOFNo: "))
        qu="update cemetery set MOFNo={} where graveno={}".format(m,g)
        cursor.execute(qu)
        con.commit()
        q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
        cursor.execute(q)
        data=cursor.fetchall()
        print()
        print("\033[1mMode Of Funeral No. Successfully Changed to:\033[0m",m)
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        
    
    


def ucod():
    g=int(input("Enter the grave no.: "))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        print()
        m=int(input("Enter new CODNo: "))
        qu="update cemetery set CODNo={} where graveno={}".format(m,g)
        cursor.execute(qu)
        con.commit()
        q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
        cursor.execute(q)
        data=cursor.fetchall()
        print()
        print("\033[1mCause Of Death No. Successfully Changed to:\033[0m",m)
        print(tabulate(data,headers=['\033[1mGraveNo.\033[0m','\033[1mName\033[0m','\033[1mGender\033[0m','\033[1mDateOfBirth\033[0m','\033[1mDateOfDeath\033[0m','\033[1mCODNo.\033[0m','\033[1mCauseOfDeath\033[0m','\033[1mMOFNo.\033[0m','\033[1mModeOfFuneral\033[0m','\033[1mLocation\033[0m'],tablefmt='grid'))
        



def update():
    text1="""\033[1mUpdate:\033[0m"""
    text2="""1.Name\n2.Gender\n3.Date Of Birth\n4.Date Of Death\n5.Location\n6.MOFNo.\n7.CODNo.\n8.Exit to main menu"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        uname()
    elif ch==2:
        ugender()
    elif ch==3:
        udob()
    elif ch==4:
        udod()
    elif ch==5:
        ulocation()
    elif ch==6:
        umof()
    elif ch==7:
        ucod()
    elif ch==8:
        print("""\033[1mExiting...\n\033[0m""")
        
    else:
        print("\033[1mInvalid Choice !!\033[0m")






def dgrave():
    g=int(input("Enter GraveNo.:"))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and graveno={}".format(g)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        qu="delete from cemetery where graveno={}".format(g)
        cursor.execute(qu)
        con.commit()
        print("\033[1mSuccessfully Deleted\033[0m")





def dname():
    name=input("Enter Name:")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and name='{}'".format(name)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        qu="delete from cemetery where name='{}'".format(name)
        cursor.execute(qu)
        con.commit()
        print("\033[1mSuccessfully Deleted\033[0m")






def dgender():
    gen=input("Enter Gender (M/F):")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and gender='{}'".format(gen)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        qu="delete from cemetery where gender='{}'".format(gen)
        cursor.execute(qu)
        con.commit()
        print("\033[1mSuccessfully Deleted\033[0m")





def ddob():
    dob=input("Enter Date Of Birth (in 'YYYY-MM-DD' format):")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and dateofbirth='{}'".format(dob)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        qu="delete from cemetery where dateofbirth='{}'".format(dob)
        cursor.execute(qu)
        con.commit()
        print("\033[1mSuccessfully Deleted\033[0m")
        




def ddod():
    dod=input("Enter Date Of Death (in 'YYYY-MM-DD' format):")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and dateofdeath='{}'".format(dod)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        qu="delete from cemetery where dateofdeath='{}'".format(dod)
        cursor.execute(qu)
        con.commit()
        print("\033[1mSuccessfully Deleted\033[0m")
        




def dlocation():
    loc=input("Enter Location:")
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and location='{}'".format(loc)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
    
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        qu="delete from cemetery where location='{}'".format(loc)
        cursor.execute(qu)
        con.commit()
        print("\033[1mSuccessfully Deleted\033[0m")


        

def dmof():
    mof=int(input("Enter MOFNo:"))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and c.mofno={}".format(mof)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
    
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        qu="delete from cemetery where mofno={}".format(mof)
        cursor.execute(qu)
        con.commit()
        print("\033[1mSuccessfully Deleted\033[0m")


def dcod():
    cod=int(input("Enter CODNo:"))
    q="select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno and c.codno={}".format(cod)
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    if num==0:
    
        print("\033[1mRecord Not Found\033[0m")
        
    else:
        qu="delete from cemetery where codno={}".format(cod)
        cursor.execute(qu)
        con.commit()
        print("\033[1mSuccessfully Deleted\033[0m")        




def delete():
    text1="""\033[1mDelete a record based on:\033[0m"""
    text2="""1.Grave No.\n2.Name\n3.Gender\n4.Date Of Birth\n5.Date Of Death\n6.Location\n7.MOFNo.\n8.CODNo.\n9.Exit To Main Menu"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        dgrave()
    elif ch==2:
        dname()
    elif ch==3:
        dgender()
    elif ch==4:
        ddob()
    elif ch==5:
        ddod()
    elif ch==6:
        dlocation()
    elif ch==7:
        dmof()
    elif ch==8:
        dcod()
    elif ch==9:
        print("""\033[1mExiting...\n\033[0m""")
    else:
        print("\033[1mInvalid Choice !!\033[0m")
    



def usrbckup():
    f1=open("user1.csv",'r+',newline='')
    f2=open("userbackup.csv",'w',newline='')
    reader=csv.reader(f1)
    writer=csv.writer(f2)
    for i in reader:
        writer.writerow(i)
        
    f1.close()
    f2.close()
    
    print()
    print("\033[1mBackup Successfully Created\033[0m")
    print()
    
    
    
    
def dcsbckup():
    try:
        q="create table cemeterybackup as select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno"
        cursor.execute(q)
        con.commit()
        print("\033[1mBackup Table Successfully Created\033[0m")
    except Exception as e:
        print('\033[1m'+str(e)+'\033[0m')
        
        ans=input("\nDo you want to drop the existing backup table?\n(y/n): ")
        if ans=='y':
            qu="drop table cemeterybackup"
            cursor.execute(qu)
            print("\033[1mBackup Table Dropped Successfully\033[0m")
            
            q="create table cemeterybackup as select graveno,name,gender,dateofbirth,dateofdeath,c.CODNo,COD,c.MOFNo,MOF,Location from cemetery c,cause a,mode m where c.mofno=m.mofno and c.codno=a.codno"
            cursor.execute(q)
            con.commit()
            print()
            print()
            
            
            tdy=datetime.now()
            dt=tdy.strftime("%d/%m/%Y %H:%M:%S")
            
            table=[["\033[1mRecent Backup Recorded:\033[0m"],
                   [dt]]
            print(tabulate(table))



def backup():
    text1="""\033[1mSelect:\033[0m"""
    text2="""1.Backup User Info. \n2.Backup Deceased Info. \n3.Exit To Main Menu"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        usrbckup()
    elif ch==2:
        dcsbckup()
    elif ch==3:
        print("""\033[1mExiting...\n\033[0m""")
    else:
        print("\033[1mInvalid Choice !!\033[0m")
    return
              





def gengraph():
    q="select * from cemetery where gender='M'"
    cursor.execute(q)
    data=cursor.fetchall()
    num=cursor.rowcount
    
    qu="select * from cemetery where gender='F'"
    cursor.execute(qu)
    data=cursor.fetchall()
    num1=cursor.rowcount
    b,a=[num,num1],['Male','Female']
    mpt.bar(a,b,color=['r','b'])
    
    mpt.show()




def agegraph():
    q1="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 0 and 10"
    cursor.execute(q1)
    data=cursor.fetchall()
    num1=cursor.rowcount
    
    q2="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 10 and 20"
    cursor.execute(q2)
    data=cursor.fetchall()
    num2=cursor.rowcount
    
    q3="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 20 and 30"
    cursor.execute(q3)
    data=cursor.fetchall()
    num3=cursor.rowcount
    
    q4="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 30 and 40"
    cursor.execute(q4)
    data=cursor.fetchall()
    num4=cursor.rowcount
    
    q5="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 40 and 50"
    cursor.execute(q5)
    data=cursor.fetchall()
    num5=cursor.rowcount
    
    q6="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 50 and 60"
    cursor.execute(q6)
    data=cursor.fetchall()
    num6=cursor.rowcount
    
    q7="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 60 and 70"
    cursor.execute(q7)
    data=cursor.fetchall()
    num7=cursor.rowcount
    
    q8="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 70 and 80"
    cursor.execute(q8)
    data=cursor.fetchall()
    num8=cursor.rowcount
    
    q9="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 80 and 90"
    cursor.execute(q9)
    data=cursor.fetchall()
    num9=cursor.rowcount
    
    q10="select * from cemetery where (year(dateofdeath)-year(dateofbirth)) between 90 and 100"
    cursor.execute(q10)
    data=cursor.fetchall()
    num10=cursor.rowcount
    
    q11="select * from cemetery where (year(dateofdeath)-year(dateofbirth))>100"
    cursor.execute(q11)
    data=cursor.fetchall()
    num11=cursor.rowcount
    b,a=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11],['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','>100']
    mpt.bar(a,b,color=['r'])
    
    mpt.show()





def locgraph():
    q1="select * from cemetery where location='Al Mirfa Cemetery'"
    cursor.execute(q1)
    data=cursor.fetchall()
    num1=cursor.rowcount
    q2="select * from cemetery where location='Baniyas Cemetery'"
    cursor.execute(q2)
    data=cursor.fetchall()
    num2=cursor.rowcount
    q3="select * from cemetery where location not in ('Baniyas Cemetery','Al Mirfa Cemetery')"
    cursor.execute(q3)
    data=cursor.fetchall()
    num3=cursor.rowcount
    b,a=[num1,num2,num3],['Al Mirfa Cemetery','Baniyas Cemetery','Others']
    mpt.bar(a,b,color=['r','b','g'])
    
    mpt.show()



def mofgraph():
    q1="select * from cemetery where MOFNo=1"
    cursor.execute(q1)
    data=cursor.fetchall()
    num1=cursor.rowcount
    
    q2="select * from cemetery where MOFNO=2"
    cursor.execute(q2)
    data=cursor.fetchall()
    num2=cursor.rowcount
    
    q3="select * from cemetery where MOFno=3"
    cursor.execute(q3)
    data=cursor.fetchall()
    num3=cursor.rowcount
    
    q4="select * from cemetery where MOFNo=4"
    cursor.execute(q4)
    data=cursor.fetchall()
    num4=cursor.rowcount
    
    b,a=[num1,num2,num3,num4],['Burial','Cremation','Religious','Others']
    mpt.bar(a,b,color=['r','b','g','y'])
    
    mpt.show()



def codgraph():
    q1="select * from cemetery where CODNo=1"
    cursor.execute(q1)
    data=cursor.fetchall()
    num1=cursor.rowcount
    
    q2="select * from cemetery where CODNo=2"
    cursor.execute(q2)
    data=cursor.fetchall()
    num2=cursor.rowcount
    
    q3="select * from cemetery where CODNO=3"
    cursor.execute(q3)
    data=cursor.fetchall()
    num3=cursor.rowcount
    
    q4="select * from cemetery where CODNO=4"
    cursor.execute(q4)
    data=cursor.fetchall()
    num4=cursor.rowcount
    
    q5="select * from cemetery where CODNO=5"
    cursor.execute(q5)
    data=cursor.fetchall()
    num5=cursor.rowcount
    
    q6="select * from cemetery where CODNO=6"
    cursor.execute(q6)
    data=cursor.fetchall()
    num6=cursor.rowcount
    
    b,a=[num1,num2,num3,num4,num5,num6],['Natural Death','Accident','Suicide','Murder','Medical Reason','Others']
    mpt.bar(a,b,color=['r','b','g','y','c','m'])
    
    mpt.show()



def graph():
    text1="""\033[1mDisplay graph based on:\033[0m"""
    text2="""1.Gender\n2.Age\n3.Location\n4.Mode Of Funeral\n5.Cause Of Death\n6.Exit To Main Menu"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        gengraph()
    elif ch==2:
        agegraph()
    elif ch==3:
        locgraph()
    elif ch==4:
        mofgraph()
    elif ch==5:
        codgraph()
    elif ch==6:
        print("""\033[1mExiting...\n\033[0m""")
        
    else:
        print("\033[1mInvalid Choice !!\033[0m")
    return
              
    
 
 

def dropcemetery():
    try:
        q="drop table cemetery"
        cursor.execute(q)
        con.commit()
        print()
        print("\033[1mTable Successfully Dropped\033[0m")
        
    except Exception as e:
        print()
        print('\033[1m'+"Table Already Dropped/Table Doesn't Exist"+'\033[0m')
        
        print()
        print()

        
    
def dropmode():
    try:
        q="drop table mode"
        cursor.execute(q)
        con.commit()
        print()
        print("\033[1mTable Successfully Dropped\033[0m")
        
    except Exception as e:
        print()
        print('\033[1m'+"Table Already Dropped/Table Doesn't Exist"+'\033[0m')
        
        print()
        print()

        
    
def dropcause():
    try:
        q="drop table cause"
        cursor.execute(q)
        con.commit()
        print()
        print("\033[1mTable Successfully Dropped\033[0m")
        
    except Exception as e:
        print()
        print('\033[1m'+"Table Already Dropped/Table Doesn't Exist"+'\033[0m')
        
        print()
        print()



def drop():
    text1="""\033[1mDrop:\033[0m"""
    text2="""1.Cemetery Table\n2.MOF Table\n3.COD Table\n4.Exit"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        dropcemetery()
    elif ch==2:
        dropmode()
    elif ch==3:
        dropcause()
    elif ch==4:
        print("""\033[1mExiting...\n\033[0m""")
    else:
        print("\033[1mInvalid Choice !!\033[0m")
    
        

def user():
    print()
    text1="""\033[1mChoice:\033[0m"""
    text2="""1.Log In\n2.Sign Up\n3.Exit"""
    table=[[text1],[text2]]
    output=tabulate(table,tablefmt='grid')
    print(output)
    ch=int(input("\nEnter your choice: "))
    
    if ch==1:
        login()
    elif ch==2:
        signup()
    elif ch==3:
        print("""\033[1mExiting...\n\033[0m""")
        thank()
    else:
        print("\033[1mInvalid Choice !!\033[0m")
        
    
    


def menu():
    while True:
        print()
        text1="""\033[1mPlease choose an option:\033[0m"""
        text2="""1.Create Tables\n2.Insert Grave Details\n3.List All Grave\n4.Search Specific\n5.Update Grave Details\n6.Delete Grave\n7.Display Graph\n8.Backup\n9.Drop Tables\n10.Exit"""
        table=[[text1],[text2]]
        output=tabulate(table,tablefmt='grid')
        print(output)
        ch=int(input("\nEnter your choice: "))
        
        if ch==1:
            create()
        elif ch==2:
            insert()
        elif ch==3:
            display()
        elif ch==4:
            search()
        elif ch==5:
            update()
        elif ch==6:
            delete()
        elif ch==7:
            graph()
        elif ch==8:
            backup()
        elif ch==9:
            drop()
        elif ch==10:
            thank()
            break
        else:
            print("\033[1mInvalid Choice !!\033[0m")





intro="""\033[1mWelcome To Cemetery Management System\033[0m"""
table=[[intro]]
output=tabulate(table,tablefmt='grid')
print(output)
 



def thank():
    final=""""The bitterest tears \nshed over graves are for\nwords left unsaid and\ndeeds left undone."\n   -Harriet Beecher Stowe\n\n\033[1m       Thank You
    Have A Nice Day\033[0m"""
    table=[[final]]
    output=tabulate(table,tablefmt='grid')
    print(output)



user()
