number = int(input("Please enter a five digit number ")) #12345
numder1 = number//10000
print(numder1)
number2 = number//1000%10
print(number2)
n3 = number%1000
#print(n3)
number3 = n3//100
print(number3)
number4 = n3//10%10
print(number4)
number5 = number%10
print(number5)
#1
print(f"{number5}{number4}{number3}{number2}{numder1}")
#2
print(number5,number4,number3,number2,numder1)
#3
print(number5*10000+number4*1000+number3*100+number2*10+numder1)
