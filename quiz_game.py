print("welcome to my computer quiz!")
playing = input("do you want    to play? ")
if playing.lower() != "yes":
    quit()
print("okay! let's play :)")
answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
else:
    print("incorrect!")
    
answer = input("what does gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
else:
    print("incorrect!")