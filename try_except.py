print("enter first number")
num1=input()
print("enter second number")
num2=input()
try:  # we use try except Exception as e to print code after a perticular code give an error it does not stop programm instead of it will print error and code will run 
    print("the sum of these two number is:",
          int(num1)+int(num2))
except Exception as e:
    print(e)
print("this line is very important")