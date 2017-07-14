import random

__author__ = 'Filip'
# MAKING AN ARRAY
numlist = [0,1,2,3,4,5,6,7,8]
listan = ["1","2","3","4","5","6","7","8","9"]
counter = 0
x=0
global t
def check():
    for x in range(0,2,1):
        if(listan[x]==listan[x+3] and listan[x]==listan[x+6]):
            print("Pobedio je" , listan[x])
            global t
            t=0
            break
    for x in range(0, 9, 3):
        if (listan[x] == listan[x + 1] and listan[x] == listan[x + 2]):
            print("Pobedio je", listan[x])
            t = 0
            break

    for x in range(2, 5, 2):
        if (listan[4] == listan[4 - x] and listan[4] == listan[4 + x]):
            print("Pobedio je", listan[x])
            t = 0
            break
t=1
def printbrd():
    print("\n")
    for x in range(0,9,1):
       print(listan[x], end=" ")
       if(x==2 or x==5):
          print("\n")
printbrd()
while(2):
 print ("Da li zelis da igras? 1 za da, 2 za ne")
 k=int(input())
 if(k==2):
     break

 while(t):
    print("\n")
    d = int(input("Koje polje os bajo? X:")) #we get dat by the remainder
    if(listan[d-1]=="O" or listan[d-1]=="X"):
        print("To polje je zauzeto slepce")
    else:
      listan[d-1] = "X"
      numlist.remove(d-1)
    x=0
    check()
    #commenting below because we want the AI
   #''''f = int(input ("Koje polje os OKSE?"))
    #if(listan[f-1]=="O" or listan[f-1]=="X"):
     #   print("To polje je zauzeto slepce")
   # else:
     # listan[f-1] = "O" '''''
    kek=1
    abaga=1
    count=0
    arr=[]
    while(1):
     for i in range(0,8,1):
        if(listan[i]=="X" or listan[i]=="O"):
           count+=1
           arr.append(i)
        if(i==2):
            if(count==2):
                abc=3-sum(arr)
                arr=[]
                abaga=0
                break
        if(i==6):
            if(count==2):
                abc=12-sum(arr)
                arr=[]
                abaga = 0
                break
        if(i==8):
            if(count==2):
                abaga = 0
                abc=21-sum(arr)
                arr=[]
                break
     if(abaga==1):
      abc = random.choice(numlist)
     else:
      numlist.remove(abc)
      listan[abc] = "O"
      break
    check()
    printbrd()