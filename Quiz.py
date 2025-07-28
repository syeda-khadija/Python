score = 0  
print("Welcome to the Python Quiz!")
print("Please type A, B, C or D for each answer.\n")

# Question 1
print("1. Which keyword is used to create a class in Python?")
print("A. class\nB. object\nC. def\nD. function")
ans1 = input("Your answer: ").strip().upper()
if ans1 == "A":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is A. class\n")

# Question 2
print("2. What is the result of: len('Python') ?")
print("A. 5\nB. 6\nC. 7\nD. 0")
ans2 = input("Your answer: ").strip().upper()
if ans2 == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is B. 6\n")

# Question 3
print("3. What will be the output of: print(10 // 3) ?")
print("A. 3.33\nB. 3\nC. 3.0\nD. Error")
ans3 = input("Your answer: ").strip().upper()
if ans3 == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is B. 3\n")

# Question 4
print("4. What is the correct way to create a set in Python?")
print("A. (1, 2, 3)\nB. [1, 2, 3]\nC. {1, 2, 3}\nD. <1, 2, 3>")
ans4 = input("Your answer: ").strip().upper()
if ans4 == "C":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is C. {1, 2, 3}\n")

# Question 5
print("5. What is the purpose of the 'return' statement in a function?")
print("A. To exit the loop\nB. To print the result\nC. To define a function\nD. To send back a value")
ans5 = input("Your answer: ").strip().upper()
if ans5 == "D":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is D. To send back a value\n")

# Final Score
print("Quiz Completed!")
print(f"Your Total Score: {score} out of 5")

# Optional message
if score == 5:
    print("Excellent! You're a Python pro!")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("Keep learning. Practice makes perfect!")
