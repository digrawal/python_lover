#file io basic
"""
"r" open file for reading -default
"w" open file for writing
"x" create file if not exist
"a" add more content to the file
"t" text mode -default
"b" binary mode
"+" read and write mode
"""
#p=open("raj.txt","r")
#content=p.read()
#for line in content: #this will read file charecter by character
 #   print(line)
p=open("raj.txt","r")
#print(p.readline())# this will read one line from file with new line character
#print(p.readline()) #
print(p.readlines()) # this will print lines in list with new line character
#for line in p: #this will read file line by line
    #print(line) #with new line character
    #print(line,end="")

#print(content)
#p=open("raj.txt","rb") #p is file pointer Where "r" can be in text or binary form "rt" is default mode
#p=open("raj.txt","rt") #this is default mode
#content=p.read(344) # it will read 3 character
#print("PART A)",content)
#content=p.read(344) #it will ignore this part bcos all line already printed in above section upto 344 character
#print("PART B)",content)
p.close()