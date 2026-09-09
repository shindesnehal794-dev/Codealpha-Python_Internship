import random

word = random.choice(["python", "code", "hangman", "script", "logic"])
guessed, wrong = set(), 0

while wrong < 6:
    display = [c if c in guessed else "_" for c in word]
    print("Word:", " ".join(display), f"| Wrong left: {6 - wrong}")

    if "_" not in display:
        print("You win!")
        break

    guess = input("Guess a letter: ").lower()
    guessed.add(guess)
    if guess not in word:
        wrong += 1
else:
    print(f"Game over! The word was: {word}")
