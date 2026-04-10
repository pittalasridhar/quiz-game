score = 0

answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("Your final score is:", score)