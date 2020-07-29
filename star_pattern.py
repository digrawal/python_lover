"""s=int(input("how many row you want to print star\n"))
print("you entered",s)
b=int(input("enter boolen value 1/0\n"))
bu=bool(b)
if bu==1:
    for i in range(0,s+1):
        print("*"*i)
elif bu==0:
    for i in range(s,0,-1):
        print("*"* i)
"""
a=int(input("how many row you want to print\n"))
b=bool(int(input("enter boolean 0 or 1\n")))
def star(a,b):
    if b==True:
        c=1
        while c<=a:
          print(c* "*")
          c=c+1
    else:
        while a>0:
            print(a * "*")
            a=a-1
star(a,b)
