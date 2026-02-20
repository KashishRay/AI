import os
# p=os.getcwd()
# print(p)
# os.chdir('D:/')
# print(os.getcwd())
# if not os.path.exists("temp1dir"):
#     os.mkdir('tempdir')
# name= input("enter your name:")
# if not os.path.exists(name):
#     os.mkdir(name)

# print("*")
# print("**")
# print("***")
# print("****")
# n=int(input("enter number"))
# for i in range(1,n+1):
#     print("*" *i)

# n=5
# for i in range(1,n+1):
#     print(" " *(n-i)+"* "* i)
# user="kashish"
# age=21
# am=500
# print(f"hello {user}your age is {age} your amount is   $%2.7d"%am)
# print(f"hello {user}your age is {age} your amount is   $%2.7x"%am)
# print(f"hello {user}your age is {age} your amount is   $%2.7s"%am)


# a=[3,2,5]
# max_val =max(a)
# for i in range (max_val):
#     for j in a:
#         if j>=max_val -i:
#             print("* ",end ="")
#         else:
#             print(" ",end ="")
#         print()

a=[3,2,6,5]
col=len(a)
row=max(a)
for i in  range (row):
    for j in a:
        if row-j<=i:
            print('*  ',end ='')
        else:
            print('    ',end ='')
            print()

   