number = int (input("Please enter a four digit number: ")) #1234
intermediate_number=number//10 #123
# print(intermediate_number)
first_number = number//1000 #1
print(first_number)
number_two = intermediate_number//10%10 #2
print(number_two)
number_three = intermediate_number%10 #3
print(number_three)
number_four = number%10 #4
print(number_four)

# first_number=number%10
# print(first_number)
# number_two=intermediate_number%10
# print(number_two)
# number_three=intermediate_number//10%10
# print(number_three)
# number_four=number//1000
# print(number_four)
