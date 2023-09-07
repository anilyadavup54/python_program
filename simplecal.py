#simple calculator by using python

firstNum=input("Enter 1st number:",)
firstNum=int(firstNum)

#taking operations
operation=input("Enter operation:+,-,*,/",)

SecondNum= input("Enter 2nd number:",)
SecondNum=int(SecondNum)

if operation=="+":
    print (firstNum + SecondNum)
elif operation=="-":
    print (firstNum - SecondNum)
elif operation=="*":
    print (firstNum * SecondNum)
elif operation=="/":
    print (firstNum / SecondNum)
else :
    print("Invalid operation")
