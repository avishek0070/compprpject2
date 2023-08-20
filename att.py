t=0;dict={}
k=int(input("ENTER the percentage of attendance required "))
k=k/100
while(t!=1):
    sub=input("ENTER SUBJESCT  ");lt=[];ltx=[]
    n1=int(input("ENTER number of classes attended  "));temp1=n1
    n2=int(input("ENTER total number of classes "));
    dt={}
    while(n1/n2<k):
        n1=n1+1
        n2=n2+1
    # print("final",(n1-temp1))
    # lt.append(sub);ltx.append(n1-temp1)
    dt[sub]=(n1-temp1)
    dict[sub]=(n1-temp1)
    print(dict)
    t=int(input("TO CONTINUE PRESS 0 ELSE 1  "))
print(dict)
# print(lt)
# print(ltx)
# chem-3
# epd-3
# python-5
# statics-2
# maths-4
# chemlab-2




k=int(input("ENTER the percentage of attendance required "))
k=k/100
sub=input("ENTER SUBJESCT  ");lt=[];ltx=[]
n1=int(input("ENTER number of classes attended  "));temp1=n1
n2=int(input("ENTER total number of classes "));
while(n1/n2<k):
    n1=n1+1
    n2=n2+1
print(n1-temp1)