
import random

num = random.randint(1,100)
points = 100

factors = []
multiples =[]

for i in range(2, num+1):
    if num % i == 0:
        factors.append(i)

divv = 100//num

for i in range(2, divv+1):
    multiples.append(num*i)

def generate_clue(user , num , list1 , list2):
    if user < num :
        if user in list2:
            print("Hidden Number is divisible by your choice " , user)
            return 20
        print("Try a Larger one ")
        return 10
    else:
        if user in list1:
            print("Your choice " ,user, " is a Multiple of the Hidden Number")
            return 20
        print("Try Smaller one ")
        return 10





print("You have to Guess the Number between 1 to 100 ")

while points > 0:
    user = int(input("Guess a Number "))
    
    if user == num :
        print("Correct ! " )
        break
    else:
        k = generate_clue(user , num , multiples , factors)
        points-=k

        
if points < 0:
    points = 0

print("You have scored ", points)