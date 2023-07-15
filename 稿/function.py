#4/10 因可自選幾樣配菜，main openmenu 要修正"""
import os
def test():
    print("useful")

def writemenu(inpu,n):
    # n 總主菜數
    with open(inpu,"w",encoding="utf-8") as f:
        for i in range(n):
            print("input 主菜({})".format(i+1))
            inpu=input()
            f.write(inpu)
            f.write("\n")
            print("主菜({})有幾樣配菜\t\t\t(input a number)".format(i+1))
            side=int(input())
            if side==0:
                f.write("")
                f.write("\n")
            for j in range(side):
                print("input 配菜({})".format(j+1))
                inpu=input()
                f.write(inpu)
                if j==side-1:                 #if the last line
                    f.write("\n")
                else:
                    f.write(",")
            os.system("pause")
            os.system("cls")
    


def opmenu(inpu):
    #opmenu(菜單名稱)
    
    menu=[]    

    with open (inpu,"r",encoding="utf-8") as f:
        n=0
        while 1:
            line = f.readline()
            if not line:
                break
            if "," in line :
                line=line.strip()
                temporary=line.split(",")
                menu.append(  temporary  )
            else :
                menu.append( line.strip() )
            n+=1
        return(menu,n)

def resetmenu(n,menu):
    word_arry=[]
    arry=[]
    for i in range(0,n,2):
        word_arry.append(menu[i])

    for i in range(1,n+1,2):
        arry.append(menu[i])
    return(word_arry,arry)

