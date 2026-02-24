# I ran out of ideas and just wanted to get something done
# This is what I managed to find to follow
# Might get started on Pygame next? Or perhaps something to get used to classes once again?

import random

CHARACTERS = ["A", "B", "C", "D", "E", "F"]
TRIES = 8
CODE_LENGTH = 3

def generate_code() -> list[str]:
    code: list[str] = list()

    for _ in range(CODE_LENGTH):
        code.append(random.choice(CHARACTERS))
    
    return code

def guess_code():
    while True:
        player_guess = input("Guess -> ").upper().split(" ")

        if len(player_guess) != CODE_LENGTH:
            print(f"Wrong code length -- it must be {CODE_LENGTH} characters long!")
            continue
        
        for character in player_guess:
            if character not in CHARACTERS:
                print(f"Invalid character: {character}.")
                break
        else:
            break
    return player_guess

def check_code(guess: list[str], answer: list[str]):
    character_counts: dict = {}
    characters_in_correct_position: int = 0
    characters_NOT_in_correct_position: int = 0

    for character in answer:

        # Could have been a try/except
        if character not in character_counts:
            character_counts[character] = 0
        character_counts[character] += 1
    
    for guessed_character, answer_character in zip(guess, answer):
        if guessed_character == answer_character:
            characters_in_correct_position += 1

            # Necessary to avoid double-counting
            character_counts[guessed_character] -= 1

    for guessed_character, answer_character in zip(guess, answer):
        if guessed_character in character_counts and character_counts[guessed_character] > 0 and guessed_character != answer_character:
            characters_NOT_in_correct_position += 1
            character_counts[guessed_character] -= 1

    return characters_in_correct_position, characters_NOT_in_correct_position

def main():
    print(f"Guess the code! You'll have {TRIES} attempts to reveal the hidden code, which is {CODE_LENGTH} characters long.")
    print("Valid characters:", *CHARACTERS)
    answer = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct, incorrect = check_code(guess, answer)

        if correct == CODE_LENGTH:
            print(f"You guessed the code in {attempts}.")
            break

        print(f"[Attempt {attempts}/{TRIES}] Correct positions: {correct} || Incorrect positions: {incorrect}")
    
    else:
        print("RIP. Code was: ", *answer)

if __name__ == "__main__":
    main()