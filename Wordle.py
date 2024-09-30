########################################
# Name: Milestone 1
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    
    # The main function to play the Wordle game.
    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        my_letters = ""
        row = 0
        for i in range(0,5): 
            letter = gw.get_square_letter(row, i) 
            my_letters += letter  # create a word from each of the letters
        guess = my_letters.lower() # make word lowercase
        print(f"Guess: {guess}") # print and debug (from chatgpt)
        
        if guess in ENGLISH_WORDS:
            gw.show_message("True")
        else:
            gw.show_message("Not in word list")

    
        def word_from_row(row:int) -> str: # unfinished function
            gw.get_square_letter(row, 0)
            gw.get_square_letter(row, 1)
            gw.get_square_letter(row, 2)
            gw.get_square_letter(row, 3)
            gw.get_square_letter(row, 4)
            return


    
        
    #def color_guess(): # started on next milestone because I was annoyed
    #      letters_left = guess
    #        for i in range len(guess):
     #       if guess[i] == correct [i]:
      #          gw.set_square_color(i, col, green)
       #         remove guess
    #def spaces_to_underscores(s:str) -> str:
     #   new = ""
      #  for index in range(len(s)):
    #        if s[index] in " ":
    #            new += "_"
    #        else:
    #            new += s[index]            
    #    return new 

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)



# Startup boilerplate
if __name__ == "__main__":
    wordle()
