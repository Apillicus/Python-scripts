
import sys
"""CSCI 1106 Assignment 2: Simple Ciphers

Author: Christopher Thompson

A command-line program which can encipher files using
simple ROT letter substitution ciphers or decipher the same
by exhaustive search."""


WORDLIST_FILEPATH = "some_words.txt"

def main():
    if len(sys.argv) == 1:
        print("Usage:")
        print("simple_ciphers.py encode (input filepath) [optional rot val] [optional rot shift]")
        print("simple_ciphers.py decode (input filepath)")
    else:
        mode = sys.argv[1]
        input_filepath = sys.argv[2]
        fin = open(input_filepath,"r")
        input_text = fin.read()
        fin.close()
        
        if mode == "encode":
            rot_val = 3
            if len(sys.argv) > 3:
                rot_val = int(sys.argv[3])
            rot_shift = 0
            if len(sys.argv) > 4:
                rot_shift = int(sys.argv[4])
            print(cipher(input_text,rot_val,rot_shift))
        elif mode == "decode":
            print(decipher(input_text))

def rotate_character(the_character,rot_val):
    #the_character (+rot_val) -> encoded_character
    #rot_val (0-25) (int mod 26)
    #the_character -> all_uppercase (the_character) 
    #the_character -> int(char())
    #int (-65,97) (+rot_val) -> new_int
    #new_int -> range (0-25) mod base 26 operation
    #mod_int (+65 or 97) -> encoded_int
    #encoded_int -> encoded_char
    #return(encoded_char)
    the_character = ord(the_character)
    #print(the_character)
    char_shift = 65
    
    if the_character in range(65,91):
        char_shift = 65
        the_character = the_character - char_shift
        the_character = the_character + rot_val
        the_character = the_character % 26
        the_character = the_character + char_shift
        #print(the_character)
        
    elif the_character in range(97,123):
        char_shift = 97
        the_character = the_character - char_shift
        the_character = the_character + rot_val
        the_character = the_character % 26
        the_character = the_character + char_shift
        #print(the_character)
    else:
        return chr(the_character)
    
    # the above changes the character into an int value between 0-25
    # current ord to chr
    
    return chr(the_character)
    

def cipher(input_text,rot_val,rot_shift):
    # TODO: Implement function
    #print(rot_val, ',' ,rot_shift)
    # input_text is a long string
    # encode (or decode) characters from input text using the rot_value
    output_text = ''
    encoded_letter = ''
    for x in range(0,len(input_text)):
        encoded_letter = rotate_character(input_text[x], rot_val)
        if encoded_letter.isalpha():
            output_text = output_text + encoded_letter
            rot_val += rot_shift
            rot_val = rot_val % 26     
        else:
            output_text = output_text + encoded_letter
    #print(output_text)
    return output_text    
    

    # the_list_of_strings -> list_of_words
    # list_of_words -> print(encode loop for each character)
    
def read_wordlist(filepath):
    # open file, get lines, convert words, add to list, return list
    
    list_of_words = []
    
    with open(filepath) as f: #closes file after completion
        for line in f:
    # get line in file
            list_of_words.extend(line.split())

    # for words in list_of_words:
    # print(words)
            
    # get line in each file
    return list_of_words
            
    # add line to a list of lines print(line.strip())
    # return word_list

def grade_message(plaintext,known_words):
    # TODO: Implement function

    # from plaintext, find matches from known_words list
    # exclude bad matches, return a numer of matches
    
    list_matches = 0

    for word in plaintext.split():
        for words in known_words:
            if word.upper() == words.upper():
                list_matches += 1
            else:
                pass
    return list_matches
    
def decipher(ciphertext):
    # TODO: Implement function
    dictionary = read_wordlist(WORDLIST_FILEPATH)
    cipher_list = []
    highest_grade = 0
    highest_graded_plaintext = ''
    # brute force the value of encoded message (check x amount of consecutive words)
    for rot in range (-26,0):
        for shift in range (-26,0):
            cipher_list.append(cipher(ciphertext,rot,shift))
        
        #print(rot)
    # check decoded word for match in some_words.txt file
    for plaintext in cipher_list:
        #print(grade_message(plaintext,dictionary))
        if grade_message(plaintext,dictionary) > highest_grade:
            highest_graded_plaintext = plaintext
            highest_grade = grade_message(plaintext,dictionary)
    return highest_graded_plaintext 
        
       
    
    # eat a file (remove whitespace) -> list__strings
    # list_of_strings (or remove whitespace) -> list_of_strings
    # use read_wordlist -> get list_of_words

    
    # the_list_of_strings -> list_of_words
    # list_of_words -> print(encode loop for each character)
    #pass

if __name__ == "__main__":
    main()
    
