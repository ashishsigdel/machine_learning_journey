import random

target = random.randint(0, 100)
score = 100

while True:
    guessedNum = int(input("Guess the Number in 0 to 100: "))
    if(score <= 70):
        print("Game Over! You loose.")
        break
    if guessedNum == target:
        print("You guessed it!")
        print("Your score is: ", score)
        break
    elif guessedNum > target:
        print("Your guess is bigger. try smaller!")
        score -= 5
        continue
    else :
        print("Your guess is smaller. Try Bigger one.")
        score -= 5
        continue
