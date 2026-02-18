# st=str(input("student type(msd/mgsh/mgsds/msh)"))
# tf=float(input("tution fee"))
# bf=float(input("bus fee"))
# hf=float(input("hostel fee"))  
# if(st=="msd"): 
#     y=tf+bf 
#     print("msd",y) 
# elif(st=="msh"): 
#     y=tf+hf 
#     print("msh",y) 
# elif(st=="mgsh"): 
#     y=tf*1.5+hf 
#     print("mgsh",y) 
# elif(st=="mgsds"): 
#     y=tf*1.5+bf 
#     print("mgsds",y) 
# else:
#     print("invalid the current student")


# ab=float(input("enter the account balance")) 
# wb=float(input("enter the withdraw account")) 
# if(wb>ab): 
#     print("insufficent funds") 
# elif(wb>=10000):
#     print("limited exiceted")
# else:
#     print("allow withdraw")


# ab=10000
# atempin=1704 
# upin=int(input('enter the pin')) 
# if(atempin==upin):
#     wa=float(input("enter the withdraw amount")) 
#     if(ab<wa or ab==wa): 
#        print("insufficient balance")
#     elif(0>ab):
#         print("invaild amount")
#     else: 
#         y=ab-wa 
#         print("withdraw is successfully") 
#         print("balance amount",y)
# else:
#     print("wrong pin") 
 
    
# age=int(input("enter the age")) 
# show=str(int(input("morning/evening"))) 
# if(age>5): 
#     print("free ticket") 
# elif(age<17): 
#     print("child ticket") 
# elif(age>18<59):
#     print("adult ticket")
#     if(show=="morning"):  
#         print("ticket price",child-50) 
#     else: 
#         print("ticket price",child) 
# elif(age>60): 
#     print("adult ticket") 
#     if(show=="morning"):
#       print("ticket price",adult-50) 
#     else: 
#         print("ticket price",adult) 
# else:
#      print("senior citizen") 
#      if(show=="morning"): 
#          print("ticket price",senior-50) 
#     else: 
#         print("ticket price",senior)


# loop   

# sum=0
# for i in range(1,100,2): 
#     print(i) 
#     sum=i+sum
# print(sum)

# sum=0
# for i in range(1,100,2): 
#     if(i%2==0):
#        print(i)
#        sum=i+sum
#  print(sum) 


# for i in range (1,11): 
    # print(i,"*5",i*5)


# t=int(input("enter the mark tamil"))
# e=int(input("enter the marke english")) 
# m=int(input("enter the mark maths")) 
# s=int(input("enter the mark science")) 
# ss=int(input("enter the mark social science")) 
# f=t+e+m+s+ss/5 
# print("average mark",f) 


# for i in range(1,6): 
#     print("*"*i) 


# for i in range(5,0,-1): 
#      print("*"*i)   


# n=int(input("enter the number"))
# i=1
# while i<=n:
#     print(i) 
#     i=i+2 


# n=int(input("enter the number"))
# i=0
# while i<=n:
#     print(i) 
#     i=i-1  


i=0 
while(i<11): 
    print(i,"*5",i*5) 
    i=i+1