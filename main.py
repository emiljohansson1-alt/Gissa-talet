import random


name = input("Vad heter du? ")
print(f"Hej, {name}, och välkommen till spelet!")

#Del 2

number = random.randint(1, 10)
guess = int(input("Gissa ett nummer mellan 1 och 10: "))
if guess == number:
    print("Rätt gissat!")
else:
    print(f"Fel gissat! Rätt nummer var {number}.")

#Del 3

