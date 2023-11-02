from tkinter import *
import random
import time

def save():
    text = ("Order No.: "+ E1.get())+"\n"+E2.get()+"\n"+E3.get()+"\n"+E4.get()+"\n"+E5.get()+"\n"+E7.get()+"\n"+E8.get()+"\n"+"Cost of Meal: " + E6.get()+"\n"+"Service Charge: " + E9.get()+"\n"+"Tax: " +E10.get()+"\n"+"Total: " +E11.get()
    with open('taxt.txt','w') as f:
        f.writelines(text)
        
root = Tk()
root.geometry("1600x700")
root.title("Restaurant Management System")
root.configure(background='silver')

#-----------------------------------
gui_title = Label(root,font=('Monotype Corsiva',40,'bold'),bg="silver",text="Restaurant Management System",fg="black",bd=10,anchor='w')
gui_title.grid(row=0,column=1)

#-----------------TIME--------------
time=time.asctime(time.localtime(time.time()))
lbl_time = Label(font=('Times New Roman',20, 'bold' ),bg="silver",text=time,fg="black",anchor='w')
lbl_time.grid(row=1,column=1)

#------------------------------------

def quit():
    root.destroy()

def reset():
    rand.set("")
    PizzaFries.set("")
    LunchMeal.set("")
    ChickenManchurian.set("")
    Macronies.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")

def Ref():
    x=random.randint(2000, 5000)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(PizzaFries.get())
    coLunchMeal= float(LunchMeal.get())
    coChickenManchurian= float(ChickenManchurian.get())
    comacronies= float(Macronies.get())
    cocheese_burger= float(Cheese_burger.get())
    codrinks= float(Drinks.get())

    costoffries = cof*150
    costofLunchMeal = coLunchMeal*500
    costofc_m = coChickenManchurian*250
    costofmacronies = comacronies*100
    costofcheeseburger = cocheese_burger*600
    costofdrinks = codrinks*60

    costofmeal = "Rs.",str('%.2f'% (costoffries +costofLunchMeal + costofc_m + costofmacronies + costofcheeseburger + costofdrinks))
    
    PayTax=((costoffries +  costofLunchMeal + costofc_m + costofmacronies +  costofcheeseburger + costofdrinks)*0.33)
    
    Totalcost=(costoffries +  costofLunchMeal + costofc_m + costofmacronies  + costofcheeseburger + costofdrinks)
    
    Service=((costoffries +  costofLunchMeal + costofmacronies + costofc_m + costofcheeseburger + costofdrinks)/99)
    
    TotalCost="Rs.",str( PayTax + Totalcost + Service)
    PaidTax="Rs.",str('%.3f'% PayTax)
    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Total.set(TotalCost)
    
def cost_of_meal():
    gui = Tk()
    gui.geometry("600x220+0+0")
    gui.title("Price List")
    lblinfo = Label(gui, font=('arial', 18, 'bold'), text="ITEM", fg="black",bd=5)
    lblinfo.grid(row=0, column=0,padx=30)
    lblinfo = Label(gui, font=('arial', 18,'bold'), text="", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2,padx=30)
    lblinfo = Label(gui, font=('arial', 18, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="Pizza Fries ", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="150", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="500", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="Chicken Manchurian", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="250", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="Macronies", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="100", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W, padx=10)
    lblinfo.grid(row=5, column=0, padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="600", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0,padx=30)
    lblinfo = Label(gui, font=('arial', 15, 'bold'), text="60", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3,padx=30)
    gui.mainloop()

#---------------------------------------------------------------------------------
def receipt():
    top=Toplevel()
    top.geometry('312x325')
    top.configure(bg="grey")
    l1 = Label(top,text="Restaurant".upper(), font=('arial 20 bold')).grid(row=0,column=1)
    l2 = Label(top,text="-------receipt---------".upper(),font=('arial 12 bold'),width=10,bd=6,padx=10,fg= "white", bg="black").grid(row=1,column=1)
    l3 = Label(top,text="Order No. :" ,font=('arial 15 bold'),width=10,bd=6,padx=10,fg= "white", bg="black",anchor='w').grid(row=2,column=0)
    l3 =Entry(top, font='arial 20 bold',textvariable=rand,relief=SUNKEN).grid(row=2,column=1)
##    l3 = Label().grid(row=2,column=1)
    l4 = Label(top, text="Thankyou for Coming").grid(row=3,column=1)
    
    b1= Button(top,text="OK",bd=10, width=10 ,fg="white",font=('arial' ,16,'bold'), bg="black",command=top.destroy)
    b1.grid(row=5,column=2)
    save()
    top.mainloop()

#----------------------------------------------------------------------------------
rand = StringVar()
PizzaFries = StringVar()
LunchMeal = StringVar()
ChickenManchurian = StringVar()
Macronies = StringVar()
Drinks = StringVar()
Cheese_burger = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
cost = StringVar()

#-------------------------------buttons for menu------------------------------------

lbl_order = Label(root, font=('arial' ,14, 'bold'),text="Order No.",bg="silver",fg="black",bd=10,anchor='w').grid(row=3,column=0)
E1 =Entry(root,font=('arial' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right', relief=SUNKEN)
E1.grid(row=3,column=1,padx=10)

lbl_fries = Label(root, font=('arial' ,14, 'bold'),text="Pizza Fries",bg="silver",fg="black",bd=10,anchor='w')
lbl_fries.grid(row=4,column=0)
E2 = Entry(root,font=('arial' ,16,'bold'), textvariable=PizzaFries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E2.grid(row=4,column=1,padx=20,pady=20)

lblLunchMeal = Label(root, font=('arial' ,14, 'bold'),text="Lunch Meal",bg="silver",fg="black",bd=10,anchor='w')
lblLunchMeal.grid(row=5,column=0,padx=20)
E3 = Entry(root,font=('arial' ,16,'bold'), textvariable=LunchMeal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E3.grid(row=5,column=1,padx=20,pady=20)

lblmanchurian = Label(root, font=('arial', 14, 'bold'),text="Chicken Manchurian",bg="silver",fg="black",bd=10,anchor='w')
lblmanchurian.grid(row=6,column=0)
E4 = Entry(root,font=('arial' ,16,'bold'), textvariable=ChickenManchurian, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E4.grid(row=6,column=1,padx=10,pady=20)

lbl_macronies = Label(root, font=('arial' ,14, 'bold'),text="Macronies",bg="silver",fg="black",bd=10,anchor='w')
lbl_macronies.grid(row=7,column=0)
E5 = Entry(root,font=('arial' ,16,'bold'), textvariable=Macronies , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E5.grid(row=7,column=1,padx=20,pady=20)

lbl_mealcost = Label(root, font=('arial' ,14, 'bold'),text="Cost of Meal",bg="silver",fg="black",bd=10,anchor='w')
lbl_mealcost.grid(row=4,column=2)
E6 = Entry(root,font=('arial' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E6.grid(row=4,column=3,padx=20,pady=20)

###--------------------------------------------------------------------------------------
lbl_Drinks = Label(root, font=('arial' ,14, 'bold' ),text="Drinks",bg="silver",fg="black",bd=10,anchor='w')
lbl_Drinks.grid(row=3,column=2)
E7 = Entry(root,font=('arial' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E7.grid(row=3,column=3,padx=20,pady=20)

lblcost = Label(root, font=('arial' ,16, 'bold' ),text="Cheese Burger",bg="silver",fg="black",bd=10,anchor='w').grid(row=8,column=0)
E8= Entry(root,font=('arial' ,16,'bold'), textvariable=Cheese_burger,bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E8.grid(row=8,column=1)

lblService_Charge = Label(root, font=('arial', 16, 'bold' ),text="Service Charge",bg="silver",bd=10,fg="black",anchor='w').grid(row=7,column=2)
E9 = Entry(root,font=('arial', 16,'bold'), textvariable=Service_Charge, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E9.grid(row=7,column=3)

lbl_Tax = Label(root, font=('arial',16, 'bold' ),text="Tax",fg="black",bg="silver",bd=10,anchor='w').grid(row=6,column=2)
E10= Entry(root,font=('arial' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E10.grid(row=6,column=3)

lblTotal = Label(root, font=('arial' ,16, 'bold' ),text="Total",bg="silver",fg="black",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
E11 = Entry(root,font=('arial' ,16,'bold'), textvariable=Total, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
E11.grid(row=5,column=3)

##-----------------------------------------buttons------------------------------------------
btn_Total=Button(root, bd=10, width=10 ,fg="white",font=('arial' ,16,'bold'),text="TOTAL", bg="black",command=Ref)
btn_Total.grid(row=9,column=1)

btn_reset=Button(root, bd=10, width=10,fg="white",font=('arial' ,16,'bold'), text="CLEAR", bg="black",command=reset)
btn_reset.grid(row=10,column=1,pady=10)

btn_quit=Button(root,bd=10, width=10 ,fg="white",font=('arial' ,16,'bold'), text="EXIT", bg="black",command= quit)
btn_quit.grid(row=9,column=2,padx=10)

btn_price=Button(root, bd=10, width=12 ,fg="white",font=('arial' ,16,'bold'), text="PRICE", bg="black",command=cost_of_meal)
btn_price.grid(row=9,column=0,padx=20)


btn_submit=Button(root, text="Submit".upper(),command=receipt, font=('arial' ,16,'bold'),fg="white",bd=10, width=10, bg="Black")
btn_submit.grid(row=10,column=0)
##
##btn_save=Button(root,text='OK'.upper(),bd=10, bg= 'black',width=10 ,fg="white",command=save,font=('arial' ,16,'bold'))
##btn_save.grid(row = 10, column=3)

##btnsubmit=Button(root,padx=16,pady=8,bd=10,fg="white",font=('ariel',16,'bold'),width=10,text="Submit",bg="black")
##btnsubmit.grid(row=10, column=2)
##

root.mainloop()
