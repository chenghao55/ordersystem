import os   #os.system("cls") 清除終端
from function import opmenu
from function import resetmenu
from function import writemenu
#===================================================================
menu=[]
word_arry=[]
arry=[]

menu,n=opmenu("預設menu.txt")   #開啟檔案的步驟  n 菜單行數
word_arry,arry=resetmenu(n,menu)#
while 1:
    
    print('開始點餐')
    print('請選擇你的餐點')
    #print menu
    j=1
    for i in range(0,n,2):
        print("{},{}".format(j,menu[i]))
        j+=1
    print()
    
        #功能選單
    print("open>>載入檔案資料\nwrite>>撰寫菜單\nquit>>結束")
    x=input()

    #功能選單----------------------------------------------------------
    if x=="quit":
        break
    elif x=="open":
        try:
            os.system("cls")
            print("輸入要開啟的檔案名稱\t\t\t(例:預設menu.txt)")
            inpu=input()
            menu,n=opmenu(inpu)
            word_arry,arry=resetmenu(n,menu)
            print("\n導入成功")
            
            print() 
            os.system("pause")
            os.system("cls")
            continue
        except FileNotFoundError:
            os.system("cls")
            print("檔名無效，請重新選擇")

            print() 
            os.system("pause")
            os.system("cls")
            continue
    elif x=="write":
        os.system("cls")
        print("name a title for your save")
        inpu=input()
        print("input the number of main dishes")
        n=int(input())

        writemenu(inpu,n)
        os.system("pause")
        os.system("cls")
    try:
        x=int(x)
    except:
        continue


    #menu----------------------------------------------------------------------
    if 1:
        os.system("cls")
        if arry[x-1]=="":
            print("無選項")
            print(menu)
        else:
            print(arry[x-1])
            print("第幾樣配菜>>")
            y=int(input())
            print("你選擇的是{}({})".format(arry[x-1][y-1],word_arry[x-1]))
    print()    
    os.system("pause")
    os.system("cls")

