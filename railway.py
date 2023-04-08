#DEfinition for the Login () 
import mysql.connector as sc

def Login():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN RAILWAY")
    print("*****************************")
    user=input("Enter USer Name:")
    pas=input("Enter password:")
    if user=='Admin' and pas=='mgm':
        print("SUCCESSFUULY LOGGED!!!!!!")
        homepage()
    else:
        print("INCORRECT CREDENTIALS")
        Login()

#Definition for AddTrain() function
def AddTrain():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN RAILWAY")
    print("*****************************")
    print("ADD TRAIN DETAILS")
    T_id=input("Enter Train ID ")
    T_name=input("Enter Train NAme:")
    T_startloc=input("Enter Starting Location:")
    T_endloc=input("Enter Ending location:")
    T_starttime=input("Enter starting time:")
    T_endtime=input("Enter ending time:")
    T_noofac=int(input("Enter number of AC "))
    T_noofsleeper=int(input("Enter no of sleepers"))
    T_noofgeneral=int(input("Enter no of general"))
    T_priceac=int(input("Amount of AC ticket"))
    T_pricesleeper=int(input("Enter price of sleeper"))
    T_pricegeneral=int(input("Enter price of general"))
    conn=sc.connect(host="localhost",user="root",password="mgm",database="ip12")
    mycursor=conn.cursor()
    query="insert into train values('{}','{}','{}','{}','{}','{}',{},{},{},{},{},{})".format(T_id,T_name,T_startloc,T_endloc,T_starttime,T_endtime,T_noofac,T_noofsleeper,T_noofgeneral,T_priceac,T_pricesleeper,T_pricegeneral)
    mycursor.execute(query)
    conn.commit()
    print("SUCCESSFULLY ADD TRAIN DETAILS !!!!!!")
    conn.close()
    
#DEfinition of UpdateTrain() function
def UpdateTrain():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN RAILWAY")
    print("*****************************")
    print("UPDATE  TRAIN DETAILS")
    T_id=input("Enter Train ID  to be updated ")
    T_starttime=input("Enter updated starting time:")
    T_endtime=input("Enter updated ending time:")
    T_noofac=int(input("Enter updated number of AC "))
    T_noofsleeper=int(input("Enter updated no of sleepers"))
    T_noofgeneral=int(input("Enter updated  no of general"))
    T_priceac=int(input("Enter updated Amount of AC ticket"))
    T_pricesleeper=int(input("Enter updated price of sleeper"))
    T_pricegeneral=int(input("Enter updated price of general"))
    conn=sc.connect(host="localhost",user="root",password="mgm",database="ip12")
    mycursor=conn.cursor()
    query="update  train set starttime='{}',endtime='{}',NoofAC={},noofsleeper={},noofgeneral={},priceAc={},pricesleeper={},pricegeneral={} where Tid='{}'".format(T_starttime,T_endtime,T_noofac,T_noofsleeper,T_noofgeneral,T_priceac,T_pricesleeper,T_pricegeneral,T_id)
    mycursor.execute(query)
    conn.commit()
    print("SUCCESSFULLY UPDATED  TRAIN DETAILS !!!!!!")
    conn.close()

#Definition for the RemoveTrain() function
def RemoveTrain():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN RAILWAY")
    print("*****************************")
    print("REMOVE   TRAIN DETAILS")
    T_id=input("Enter Train ID  to be removed  ")
    conn=sc.connect(host="localhost",user="root",password="mgm",database="ip12")
    mycursor=conn.cursor()
    query="delete from train where Tid='{}'".format(T_id)
    mycursor.execute(query)
    conn.commit()
    print("SUCCESSFULLY REMOVED   TRAIN DETAILS !!!!!!")
    conn.close()
    
#DEfinition for SEarch Train details.
def SearchTrain():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN RAILWAY")
    print("*****************************")
    print("SEARCH   TRAIN DETAILS")
    T_id=input("Enter Train ID  to be Search   ")
    conn=sc.connect(host="localhost",user="root",password="mgm",database="ip12")
    mycursor=conn.cursor()
    query="select *  from train where Tid='{}'".format(T_id)
    mycursor.execute(query)
    myrecord=mycursor.fetchall()
    for x in myrecord:
        print(x)
    conn.close()
    
#DEfinition for TicketBooking() function 
def TicketBooking():
    print("\n\n\n\n")
    print("***************************")
    print("WELCOME TO INDIAN RAILWAY")
    print("*****************************")
    print("TICKET BOOKING SECTION ")
    conn=sc.connect(host="localhost",user="root",password="mgm",database="ip12")
    mycursor=conn.cursor()
    query="select *  from train "
    mycursor.execute(query)
    myrecord=mycursor.fetchall()
    print("TID\t\tTname\t\tSTARTINGPOINT\t\tENDLOC\t\tSTARTTIME\t\tENDTIME\t\tNOOFAC\t\tNOOFsleeper\t\tNOOFgeneral\t\tPRICEAC\t\tPRICESLEEPER\t\tPRICEGENERAL\t\t\n")
    for x in myrecord:
        print(x[0],'\t\t',x[1],"\t\t",x[2],"\t\t",x[3],"\t\t",x[4],"\t\t",x[5],"\t\t",x[6],"\t\t",x[7],"\t\t",x[8],"\t\t",x[9],"\t\t",x[10],"\t\t",x[11],"\n")
    conn.close()
    Tid=input("Enter ID of the TRain you are Booking")
    tname=input("Enter name of the train")
    adharnouser=int(input("Enter your Ahdar No"))
    name=input("Enter your name")
    age=int(input("Enter your age"))
    typeticket=input("Enter type of Ticket(AC/Sleeper/General)")
    startloc=input("Starting location")
    endloc=input("Enter Destination location")
    conn=sc.connect(host="localhost",user="root",password="mgm",database="ip12")
    fare=0
    mycursor=conn.cursor()
    query="select *  from train where Tid='{}'".format(Tid)
    mycursor.execute(query)
    myrecord=mycursor.fetchall()

   # else:
        #fare=fare
    conn=sc.connect(host="localhost",user="root",password="mgm",database="ip12")
    mycursor=conn.cursor()
    query="insert into trainbooking values('{}','{}',{},'{}',{},'{}','{}','{}',{})".format(Tid,tname,adharnouser,name,age,typeticket,startloc,endloc,fare)
    mycursor.execute(query)
    conn.commit()
    print("SUCCESSFULLY DONE TICKEt BOOKING !!!!!!")
    conn.close()
    
## Definition for SearchBooking() function
def SearchBooking():
    ano=int(input("Enter your adhar number for checking"))
    conn=sc.connect(host="localhost",user="root",password="mgm",database="ip12")
    mycursor=conn.cursor()
    query="select *  from trainbooking where adharno_user={}".format(ano)
    mycursor.execute(query)
    myrecord=mycursor.fetchall()
    for x in myrecord:
        print(x)
    else:
        print("No Booking in this Adhar No")
    conn.close() 
    
    
#Definition for CancelTicket() function
def CancelTicket():
    ano=int(input("Enter your adhar number for cancellation"))
    conn=sc.connect(host="localhost",user="root",password="mgm",database="ip12")
    mycursor=conn.cursor()
    query="delete  from trainbooking where adharno_user={}".format(ano)
    mycursor.execute(query)
    conn.commit()
   # mycursor.execute(query4)
    conn.commit()
    conn.close() 
    
def homepage():    
    
       while True:

                print('*********************************')
                print("WELCOME TO INDIAN RAILWAY")
                print("********************************")
                print("1. ADD TRAIN DETAILS")
                print("2. UPDATE TRAIn DETAILS")
                print("3. CANCELL TRAIN DETAILS")
                print("4. SEARCH TRAIn DETAILS")
                print("5.TICKET BOOKING")
                print("6. CANCEL TICKET BOOKING")
                print("7. SEARCH BOOKING DETAILS")
                print("8. REPORT ")
                op=int(input("Enter your option:"))
                if op==1:
                    AddTrain()
        
                elif op==2:
                    UpdateTrain()
                elif op==3:
                    RemoveTrain()
                elif op==4:
                    SearchTrain()
                elif op==5:
                    TicketBooking()
                elif op==6:
                    CancelTicket()
                elif op==7:
                    SearchBooking()
                elif op==8:
                   break
                    
                else:
                    print("Invalid option") 
    
    
#Calling main section
Login()
