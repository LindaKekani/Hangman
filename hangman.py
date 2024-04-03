import random


def choose_category():
    # Define categories and associated words
    print("\nWelcome to Hangman")
    print("\nChoose a category: ")
    categories = {
        1: {
            "name": "animals",
            "words": ["elephant", "giraffe", "lion", "zebra", "monkey"],
        },
        2: {
            "name": "fruits",
            "words": ["apple", "banana", "orange", "grape", "peach", "mango"],
        },
        3: {
            "name": "countries",
            "words": [
                "chad",
                "gambia",
                "united states",
                "morocco",
                "canada",
                "australia",
                "japan",
                "ghana",
            ],
        },
    }

    # User select category

    print("Categories:")
    for num, category in categories.items():
        print(f"{num}. {category['name']}")

    selected_category_num = int(input("Enter the category number: "))

    # Validate the selected category
    if selected_category_num in categories:
        selected_category = categories[selected_category_num]["name"]
        print("The selected category is: ", selected_category)
        return selected_category, random.choice(
            categories[selected_category_num]["words"]
        )
    else:
        print("Invalid category. Please choose again")
    return choose_category()


# Display the possition of the guessed letter in the word
def display_word(word, guessed_letters):
    display = " "
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "- "
    return display.strip()


# Get the chosen category and category word
def hangman():
    print("WeLcOmE to HaNgMan!!")
    category, word = choose_category()
    guessed_letters = []
    attempts = 7  # attempts allowed

    while attempts > 0:
        print("\nAttempts left: ", attempts)
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter 1 letter.")
            continue

        # Check for guessed letters
        if guess in guessed_letters:
            print("You've already guessed that letter. Try another one")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess!")
            attempts -= 1

        if set(guessed_letters) >= set(word):
            print("Congratulations! You've guessed the word", word)
            break

        if attempts == 0:
            print("Sorry, you lost. The word was: ", word)


if __name__ == "__main__":
    print("Script is starting....")
    hangman()
    input("Press Enter to exit....")
