import random
import time

#List of Words
fruits=['Apple', 'Orange', 'Banana', 'Cherry', 'Kiwi', 'Strawberry',
        'CustardApple', 'Watermelon', 'Raspberry', 'Pear', 'Avocado', 
        'DragonFruit', 'Guava', 'Grape', 'Papaya', 'Peach', 'Pomegranate',
        'Rambutan', 'Mango', 'Pineapple', 'Lychee']

veggies=['Carrot', 'Tomato', 'Potato', 'Onion', 'BitterGourd',
         'Broccoli', 'Cauliflower', 'Tapioca', 'Chillies', 'Beetroot',
         'Spinach', 'Capsicum', 'Mushroom', 'Corn', 'Cabbage',
         'Garlic', 'Ginger', 'Bringal', 'Pumkin', 'Radish']

lang=['Hindi', 'English', 'Tamil', 'Malay', 'Malayalam', 'Telugu',
      'Kannada', 'Marathi', 'Gujarati', 'Marwadi', 'French',
      'Spanish', 'Bengali', 'Arabic', 'Urdu', 'Korean', 'Italian',
      'Russian', 'Chinese', 'Japanese', 'German', 'Portuguese']

#To generate random words from the selected list
rand_fruits=random.choice(fruits)
rand_veggies=random.choice(veggies)
rand_lang=random.choice(lang)

print("--------------------")
print("Let's play HANGMAN!!")
print("--------------------")

#To display the letters missing letters in the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_ '
    return display

#Main function for the game
def hangman():
    
    user_name=input("Enter your name:  ")

    print(user_name, "please select a category")
    print("1. Fruits")
    print("2. Vegetables")
    print("3. Languages")
    
    category_option=int(input())

    print("***Remember you have 6 attempts to guess the word right****")

    if (category_option==1):
        word=rand_fruits.lower()
    elif (category_option==2):
        word=rand_veggies.lower()
    else:
        word=rand_lang.lower()

    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        #To add the letter enetered by user into the list
        guessed_letters.append(guess)

        if guess not in word:
            print("Wrong guess!")
            attempts -= 1

        if '_' not in display_word(word, guessed_letters):
            print("\nYOU WON!!!", user_name)
            print("\nYou guessed the word:", word)        
            break

    if attempts == 0:
        print("\nYou LOST!!!") 
        print("\nThe word was:", word)

if __name__ == "__main__":
    
    start_time = time.time()
    for i in range(10000000):
        pass
    end_time = time.time()
    tot_time = end_time - start_time  #To Calculate the total time

#Calling the function to start the game
    hangman()
    print("Time taken to finish the game:", tot_time, "seconds")
