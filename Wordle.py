########################################
# Name: Baily Livengood
# Collaborators (if any): Tutors
# GenAI Transcript (if any): a small amount from chatgpt
# Estimated time spent (hr): 8+
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random
def wordle():
    def random_word():
        word = ""
        while len(word) != 5:
            word = random.choice(ENGLISH_WORDS)
            print(word)
        return word
    correct = random_word()
    
    # The main function to play the Wordle game.
    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        row = gw.get_current_row()
        if row == N_ROWS: # ends game if failed
            gw.show_message("GAME OVER. WORD = " + correct.upper())
            return
        row = gw.get_current_row()
        my_letters = ""
        for i in range(0,5): # turns your guess into a string + prints
            letter = gw.get_square_letter(row, i) 
            my_letters += letter  
        guess = my_letters.lower()
        print(f"Guess: {guess}")
        
        if guess in ENGLISH_WORDS: # various messages
            if guess == correct:
                gw.show_message("YOU WIN!")
                color_guess(guess)
                return
            if guess not in ENGLISH_WORDS:
                gw.show_message("NOT IN WORD LIST")
            else:
                gw.show_message("GOOD GUESS!")
                color_guess(guess)
                gw.set_current_row(row + 1)

    
        
    def color_guess(guess: str): # colors squares
        row = gw.get_current_row()
        letters_left = correct
        for i in range (len(guess)):
            if guess[i] == correct[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
                letters_left = letters_left.replace(guess[i],"_",1)
                print(letters_left)
        
        for i in range (len(guess)):
            if gw.get_square_color(row, i) != CORRECT_COLOR:
                if guess[i] in correct and guess[i] in letters_left:
                    gw.set_square_color(row, i, PRESENT_COLOR)
                    letters_left = letters_left.replace(guess[i],"_",1)
                    print(letters_left)
                else:
                    gw.set_square_color(row, i, MISSING_COLOR)
        
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)



# Startup boilerplate
if __name__ == "__main__":
    wordle()
