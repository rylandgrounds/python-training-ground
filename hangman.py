import random

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    user_letter = input('Guess a Letter').upper()
    if user_letter in alphabet: - used_letters:
    
    user_input = input('Pick a letter and pray!')
    print(user_input) 
    