def getdate():
    import datetime
    return datetime.datetime.now()
"""print("enter the name of the person among rahul ,lokesh and pappu you want operate\n")
s=input()
if s== "rahul":
    print("write,what do u want log or retrive\n")
    lg=input()
    if lg=="log":
        print("write exercise or food to log\n")
        rf=input()
        if rf=="food":
            print("enter food item\n")
            rfd=input()
            with open("rahul_f.txt","a") as f:
                f.write(str([str(getdate())]) + rfd +"\n")
                print("file written successfully")
                f.close()
        elif rf == "exercise":
            print("enter exercise name\n")
            rfd = input()
            with open("rahul_e.txt", "a") as f:
                f.write(str([str(getdate())]) + rfd + "\n")
                print("file written successfully")
                f.close()
        else:
            print("inter valid input between food or exercise")

    elif lg=="retrive":
        print("retrive food or exercise\n")
        rf = input()
        if rf == "food":
            with open("rahul_f.txt", "r") as f:
                print("you log for food:")
                print(f.read())
                f.close()
        elif rf=="exercise":
            with open("rahul_e.txt", "r") as f:
                print("you log for food:")
                print(f.read())
                f.close()

if s== "lokesh":
    print("write,what do u want log or retrive\n")
    lg=input()
    if lg=="log":
        print("write exercise or food to log\n")
        rf=input()
        if rf=="food":
            print("enter food item\n")
            rfd=input()
            with open("lokesh_f.txt","a") as f:
                f.write(str([str(getdate())]) + rfd +"\n")
                print("file written successfully")
                f.close()
        elif rf == "exercise":
            print("enter exercise name\n")
            rfd = input()
            with open("lokesh_e.txt", "a") as f:
                f.write(str([str(getdate())]) + rfd + "\n")
                print("file written successfully")
                f.close()
        else:
            print("inter valid input between food or exercise")

    elif lg=="retrive":
        print("retrive food or exercise\n")
        rf = input()
        if rf == "food":
            with open("lokesh_f.txt", "r") as f:
                print("you log for food:")
                print(f.read())
                f.close()
        elif rf=="exercise":
            with open("lokesh_e.txt", "r") as f:
                print("you log for food:")
                print(f.read())
                f.close()

if s== "pappu":
    print("write,what do u want log or retrive\n")
    lg=input()
    if lg=="log":
        print("write exercise or food to log\n")
        rf=input()
        if rf=="food":
            print("enter food item\n")
            rfd=input()
            with open("pappu_f.txt","a") as f:
                f.write(str([str(getdate())]) + rfd +"\n")
                print("file written successfully")
                f.close()
        elif rf == "exercise":
            print("enter exercise name\n")
            rfd = input()
            with open("pappu_e.txt", "a") as f:
                f.write(str([str(getdate())]) + rfd + "\n")
                print("file written successfully")
                f.close()
        else:
            print("inter valid input between food or exercise")

    elif lg=="retrive":
        print("retrive food or exercise\n")
        rf = input()
        if rf == "food":
            with open("pappu_f.txt", "r") as f:
                print("you log for food:")
                print(f.read())
                f.close()
        elif rf=="exercise":
            with open("pappu_e.txt", "r") as f:
                print("you log for food:")
                print(f.read())
                f.close()
"""
i=int(input("enter 0 for log and 1 for retriev\n"))
if i==0:
    j=int(input("enter 0 for harry ,1 for jack,2 for raj\n"))
    k=int(input("enter 0 for food and 1 for exercise\n"))
    l1=["harry","jack","raj"]
    l2=["food","exercise"]
    with open((l1[j]+"_"+l2[k])+".txt","a") as f:
        val=str(input("enter item\n"))
        f.write(str("Date:-") + str( getdate()) + "---" + val+"\n")
        f.close()
elif i==1:
    j = int(input("enter 0 for harry ,1 for jack,2 for raj\n"))
    k = int(input("enter 0 for food and 1 for exercise\n"))
    l1 = ["harry", "jack", "raj"]
    l2 = ["food", "exercise"]
    with open((l1[j] + "_" + l2[k]) + ".txt", "r") as f:
        print(f.read())
        f.close()
