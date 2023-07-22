import random

score = 0
points = 10
questions = 0
num_questions = 5

while questions < num_questions:

    num1 = random.randint(10,30)
    num2 = random.randint(10,30)
    
    valid = num1 + num2
    questions += 1

    answer = int(input("%d + %d = " %(num1, num2)))

    if answer == valid:
        score += points
    else:
        print("Sorry, the answer is %d" %valid)

print("Your score: %d / %d" %(score, num_questions * points))