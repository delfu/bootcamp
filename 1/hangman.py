# Problem: the game is currently case-sensitive. A != a
import getpass

# Split the keyword into characters and put them into an array
def split(keyword):
    return [char for char in keyword]

# Identify the number of guesses allowed
def minimum(answer):
    if len(answer) < 5:
        return 5
    else:
        return len(answer) + 2

# Check if the guessed letter matches something in the array, if so, replace the empty space in box
def check_answer(guess):
    for index, letter in enumerate(answer):
        if letter == guess:
            box[index] = guess

# Ask P1 to input a string for P2 to guess
keyword = getpass.getpass("Player 1: Please enter the word you want Player 2 to guess: ")
answer = split(keyword)
print ("Player 2: There are ",len(answer)," characters you need to guess")

# Create a box to showcase P2 the empty places
box = []
while len(box) < len(answer):
    box.append("_")
print (box)

# Loop for the main game
number_of_guesses_left = int(minimum(answer))
while number_of_guesses_left > 0:
    print ("You have ",number_of_guesses_left," chance left to guess. Please guess a character:")
    guess = input()
    check_answer(guess)
    print (box)
    if answer == box:
        print ("Player 2 wins! The answer is: ", " ".join(answer))
        quit()
    else:
        number_of_guesses_left = number_of_guesses_left - 1
else:
    print ("You ran out of guesses!  Player 1 wins! The answer is: ", " ".join(answer))
