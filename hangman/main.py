import re

# Getting the answer
answer = "What's up, Doc?"

answer = answer.upper()

# Game Setup
num_of_incorrect_guesses = 5

answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

# Game Logic
current_incorrect_guesses = 0

while current_answer_character < num_of_incorrect_guesses or False not in answer_guessed:
    print(f"Number of incorrect guesses left: {num_of_incorrect_guesses - current_incorrect_guesses}")
    # Display current status