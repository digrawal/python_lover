import time
initial= time.time()
#print(initial)
k=0

while(k<15):
    time.sleep(2) #it will pause result for two second and then print
    print("this is rajesh")
    k+=1
print("wlile loop execution time:",time.time() - initial,"second")

initial2 =time.time()

for i in range(15):
    print(" and this is digrawal")
print("for loop execution time:",time.time() - initial2,"second")

#localtime = time.asctime(time.localtime(time.time()))
#time.time count tics and then return  it
# and time.localtime convert into local time as tuple to return
# so asctime convert tuple into presentable time format

#print(localtime)
#time.sleep() this function is used pause the code for desire time example is given above