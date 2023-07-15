from tkinter import *

win=Tk()
win.title("order system")
win.geometry("500x600")
win.config(bg="#323232")

shoppingcart=[]
total=0
memo=[]
t="微軟正黑體 30"
"""
前飾語
b button
l label
f fuction
"""
def f_leave():
    global l_memo,b_leave
    l_memo.destroy()        #!!!!!!
    b_leave.destroy()
    
    b_order.pack()
    b_memo.pack()
    
def f_memo():
    global memo,b_order,b_memo,b_leave,l_memo
    b_order.pack_forget()
    b_memo.pack_forget()
     
    m=""
    for i in range(len(memo)):
        m+=memo[i]+"\n---------------------------\n"
    l_memo =Label(text=m,font=t)
    b_leave=Button(text="離開",font=t,command=lambda:f_leave())
    l_memo.pack(pady=10)
    b_leave.pack()
    
def doneorder():
    global l_shoppingcart, b_continue, b_doneorder, shoppingcart, total
    l_shoppingcart.destroy()
    b_continue.destroy()
    b_doneorder.destroy()
    
    shoppingcart=[]
    total=0

    b_order.pack()
    b_memo.pack()
    
def f_addcart(x):
    shoppingcart.append(x)
    global total
    te=shoppingcart[len(shoppingcart)-1].split("\t")
    
    total+=int(te[2])

    
    b_egg.destroy()
    b_cookie.destroy()
    b_burger.destroy()
    b_sandw.destroy()
    b_drink.destroy()
    
    global b_continue,b_doneorder,l_shoppingcart

    te="\n".join(shoppingcart)+"\ntotal\t\t"+str(total)
    
    b_continue     =Button(text="繼續點餐",font=t,command=lambda:f_maindish())
    b_doneorder    =Button(text="完成",font=t,command=lambda:doneorder())
    l_shoppingcart =Label(text=te,font=t,bg="skyblue")
    
    l_shoppingcart.pack(pady=10)
    b_continue.pack()
    b_doneorder.pack()

    global memo
    memo.append(te)
def f_sidedish(text,a1,a2,a3,a4,a5):
    
    if text=="蛋餅":
        a1.config(text="原味"    ,command=lambda:f_addcart(text+"\t原味\t"+"35"),font=t)
        a2.config(text="培根"    ,command=lambda:f_addcart(text+"\t培根\t"+"35"),font=t)
        a3.config(text="火腿"    ,command=lambda:f_addcart(text+"\t火腿\t"+"35"),font=t)
        a4.config(text="起司"    ,command=lambda:f_addcart(text+"\t起司\t"+"35"),font=t)
        a5.config(text="玉米"    ,command=lambda:f_addcart(text+"\t玉米\t"+"35"),font=t)
    if text=="蔥抓餅":
        a1.config(text="原味"    ,command=lambda:f_addcart(text+"\t原味\t"+"45"),font=t)
        a2.config(text="韓式"    ,command=lambda:f_addcart(text+"\t韓式\t"+"50"),font=t)
        a3.config(text="火腿"    ,command=lambda:f_addcart(text+"\t火腿\t"+"45"),font=t)
        a4.config(text="起司"    ,command=lambda:f_addcart(text+"\t起司\t"+"50"),font=t)
        a5.config(text="卡拉雞排",command=lambda:f_addcart(text+"\t卡拉雞\t"+"50"),font=t)
    if text=="漢堡":
        a1.config(text="花生培根",command=lambda:f_addcart(text+"\t花生培根\t"+"65"),font=t)
        a2.config(text="卡拉雞排",command=lambda:f_addcart(text+"\t卡拉雞排\t"+"65"),font=t)
        a3.config(text="經典牛肉",command=lambda:f_addcart(text+"\t經典牛肉\t"+"65"),font=t)
        a4.config(text="鱈魚"    ,command=lambda:f_addcart(text+"\t鱈魚\t"+"60"),font=t)
        a5.config(text="總匯"    ,command=lambda:f_addcart(text+"\t總匯\t"+"65"),font=t)        
    if text=="三明治":
        a1.config(text="花生培根",command=lambda:f_addcart(text+"\t花生培根\t"+"35"),font=t)
        a2.config(text="卡拉雞排",command=lambda:f_addcart(text+"\t卡拉雞排\t"+"40"),font=t)
        a3.config(text="果醬"    ,command=lambda:f_addcart(text+"\t果醬\t"+    "30"),font=t)
        a4.config(text="蛋沙拉"  ,command=lambda:f_addcart(text+"\t蛋沙拉\t"+  "35"),font=t)
        a5.config(text="總匯"    ,command=lambda:f_addcart(text+"\t總匯\t"+    "40"),font=t)       
    if text=="飲料":
        a1.config(text="紅茶"    ,command=lambda:f_addcart(text+"\t紅茶\t"+"20"),font=t)
        a2.config(text="咖啡"    ,command=lambda:f_addcart(text+"\t咖啡\t"+"30"),font=t)
        a3.config(text="奶茶"    ,command=lambda:f_addcart(text+"\t奶茶\t"+"30"),font=t)
        a4.config(text="綠茶"    ,command=lambda:f_addcart(text+"\t綠茶\t"+"20"),font=t)
        a5.config(text="多多綠"  ,command=lambda:f_addcart(text+"\t多多綠\t"+"30"),font=t)        
def f_maindish():
    #x b_"點餐"
    #n 行數
    global b_egg, b_cookie, b_burger, b_sandw, b_drink, b_order, b_memo, b_leave, l_memo
    
    b_order.pack_forget()
    b_memo.pack_forget()
    try:
        b_continue.destroy()
        b_doneorder.destroy()
        l_shoppingcart.destroy()
    except:
        pass
    b_egg     =Button(text="蛋餅",bg="#323232",fg="white",font=t,command=lambda:f_sidedish("蛋餅",b_egg,b_cookie,b_burger,b_sandw,b_drink))
    b_cookie  =Button(text="蔥抓餅",bg="#323232",fg="white",font=t,command=lambda:f_sidedish("蔥抓餅",b_egg,b_cookie,b_burger,b_sandw,b_drink))
    b_burger  =Button(text="漢堡",bg="#323232",fg="white",font=t,command=lambda:f_sidedish("漢堡",b_egg,b_cookie,b_burger,b_sandw,b_drink))
    b_sandw   =Button(text="三明治",bg="#323232",fg="white",font=t,command=lambda:f_sidedish("三明治",b_egg,b_cookie,b_burger,b_sandw,b_drink))
    b_drink   =Button(text="飲料",bg="#323232",fg="white",font=t,command=lambda:f_sidedish("飲料",b_egg,b_cookie,b_burger,b_sandw,b_drink))
    
    b_egg.pack(pady=10)
    b_cookie.pack(pady=10)
    b_burger.pack(pady=10)
    b_sandw.pack(pady=10)
    b_drink.pack(pady=10)


#====================================================================================
b_order=Button(text="點餐",font=t,command=lambda:f_maindish())
b_memo =Button(text="紀錄",command=lambda:f_memo(),font=t)


b_order.pack()
b_memo.pack()
#====================================================================================
win.mainloop()
