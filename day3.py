# t1=0 
# t2=1 
# print(t1) 
# print(t2) 
# for i in range(8):
#     next=t1+t2  
#     print(next) 
#     t1=t2 
#     t2=next   


# list  
# list=[1,3,5,86,0] 
# print(list[3])

# list slicing [start index (include) end (exclude)] 
# print(list[:3]) 

# list opertor 
# concadenation operater (+)  
# a=[2,4,6] 
# b=[5,7,8] 
# print(a+b)

# repetation operater (*)
# num=[3]
# print(num*8)

# membership operater (in,not-in)
# car=["bmw","suzu"]
# print("lancer"in car) 

# comparesion operator 
# a=[2,4,7]
# b=[7,3,4]
# print(a==b)
# print(a>b) 



# q=[2,35,58,99]
# w=[6,86.9,90] 
# print(w[2]) 
# print(w[0:3]) 
# print(q+w*7) 
# print(w in 5) 
# print(q>w)  


# # append 
# a=[2,4,6]
# b=[6,8]
# a.append(8) 
# a.insert(3,67) 
# a.extend(b) 
# b.remove(8)
# print(a)8878y8XC0
# print(b)   

# # pop 
# a=[3,6,8,1,2]
# a.pop(1) 
# a.clear() 
# a.count(3) 
# print(a.intex(2))
# a(2) 
# print(a)  

# sort 
# a=[5,7,8,9] 
# a.sort(reverse=true) 
# print(a)

# num=][1,2,3,4] 
# result=list(map(lambda x:x*2,num)) 
# print(result)   


# numone=[1,2,3,4,5,6,7,8,9] 
# resultone=list(filter(lambda x:x%2==0,numone)) 
# print(resultone) 


#reduce 
# from functools import reduce 
# num=[1,2,3,4,5] 
# result=reduce(lambda a,b:a+b,num) 
# print(result)  


# def odd(a): 
#     if(a%2!=0):
#        print("odd numbers") 
#     else: 
#         print("even numbers")  

# n=int(input("enter the number"))
# odd(n)

# palindrome with sliceing 

# word=input("enter the word") 
# if word==word[::1]: 
#     print("palindrome") 
# else: 
#     print("it is not a palindrome") 


# palindrome without sliceing 

# w=input("enter the word") 
# rev=" " 
# for ch in w:
#     rev=ch+rev 
# if w==rev: 
#     print("it is palindrome") 
# else: 
#     print("it is not palindrome")  


# with out slicing only number  

num=list(input("enter the number")) 
original=num 
rev=0 
while num>0: 
    digital=num%10 
    num=num//10 
print(rev) 
if original==rev: 
    print ("palindrome") 
else: 
    print("not a palindrome")