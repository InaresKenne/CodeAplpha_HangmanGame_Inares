import random

def choose_word():
    words = ["python", "development", "hangman", "programming", "education"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
        
        print(display_word(word, guessed_letters))
        
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word correctly!")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was '{word}'.")

hangman()
