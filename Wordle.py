########################################
# Name: Baily Livengood
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
# milestone 3
    
    def random_word():
        word = ""
        while len(word) != 5:
            word = random.choice(ENGLISH_WORDS)
            print(word)
        return word
    correct = random_word()
    #random_word()
    #    print(correct)
    row = 0
    # The main function to play the Wordle game.
    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        
        my_letters = ""
        for i in range(0,5): 
            letter = gw.get_square_letter(row, i) 
            my_letters += letter  
        guess = my_letters.lower()
        print(f"Guess: {guess}")
        
        if guess in ENGLISH_WORDS:
            gw.show_message("True")
            color_guess(guess)

        else:
            gw.show_message("Not in word list")

    
        
        
        def word_from_row(row: int) -> str:
            word = ""
            for col in range(5):
                word += gw.get_square_letter(row, col)
            return word.lower() 


    
        
    def color_guess(guess: str):
        letters_left = correct
        for i in range (len(guess)):
            if guess[i] == correct[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
             #   letters_left = letters_left[:i] + "_" + letters_left[i+1:]
                letters_left = letters_left.replace(guess[i],"_",1)
                print(letters_left)
        
        for i in range (len(guess)):
            if gw.get_square_color(row, i) != CORRECT_COLOR:
                if guess[i] in correct and guess[i] in letters_left:
                    gw.set_square_color(row, i, PRESENT_COLOR)
                #    letters_left = letters_left[:i] + "_" + letters_left[i+1:]
                    letters_left = letters_left.replace(guess[i],"_",1)
                    print(letters_left)
                else:
                    gw.set_square_color(row, i, MISSING_COLOR)
    def spaces_to_underscores(s:str) -> str:
            new = ""
            for index in range(len(s)):
                if s[index] in " ":
                    new += "_"
                else:
                    new += s[index]            
                return new 

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)



# Startup boilerplate
if __name__ == "__main__":
    wordle()
