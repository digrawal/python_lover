#f=open("raj.txt","w") #we can also create new file instead of it by giving new file name here
#f.write("i m cool")  # this will replace existing line in file

#f=open("raj.txt2","w")  #this will create new file raj.txt2 first and then write text
#f.write("enjoying the day ")

#f=open("raj.txt2","a") #this will add line not overwrite----append mode
#a=f.write("and love you all guys\n ")
#print(a) # where a will count the written character



#Handle read and write both
f=open("raj.txt","r+")
print(f.read())
f.write("\nthankyou")

f.close()