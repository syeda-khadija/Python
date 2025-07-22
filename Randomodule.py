import random as rd
import sys
import string

print(string.digits)
print(string.ascii_letters)
print(string.punctuation)
print(string.whitespace)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.hexdigits)




# city=["Karachi","Lahore","Multan","Hyderabad","Islamabad","Rawalpindi","Gujranwala","Balochistan","Faislabad","Abbottabad"]
# print(rd.sample(city,3))
# rd.shuffle(city)
# print(rd.choice(city))
# print(city)

# print("*********** Random Number Guessing Game **********\n")
# computer_number =rd.randint(1,20)
# lives = 3
# 
# 
# while lives > 0:
#     user_input = int(input("Enter Any Number Between 1 - 20 :"))
# 
#     if user_input == computer_number:
#         print("Congratulation you've Guessed!")
#         sys.exit()
# 
#     else:
#         lives -=1
# 
#         if user_input > computer_number:
#             print("*Hint : Think Lower Number")
#         elif user_input < computer_number:
#             print("*hint : Think higher Number")
# 
#         if lives == 0:
#             print("Lives Ended")
#         else:
#             print(f"{lives} Remaining")
