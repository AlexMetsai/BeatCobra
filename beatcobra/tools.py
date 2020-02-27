
musical_note_order = {'C':  1, 
                      'C#': 2, 
                      'D':  3, 
                      'D#': 4, 
                      'E':  5, 
                      'F':  6, 
                      'F#': 7, 
                      'G':  8, 
                      'G#': 9,
                      'A':  10, 
                      'A#': 11, 
                      'B':  12}

proper_musical_note_order = {'A':  1, 
                             'A#': 2, 
                             'B':  3, 
                             'C':  4, 
                             'C#': 5, 
                             'D':  6, 
                             'D#': 7, 
                             'E':  8, 
                             'F':  9, 
                             'F#': 10, 
                             'G':  11, 
                             'G#': 12}

def return_key_frequency(key='C4', A4=440):
    # Things that need to be implemented for now are:
    # 1. Map notes to keys, e.g. A4 = 49th key, etc.
    # 2. Compute the frequency of its key.
    # The second can be easily achived by the following equation:
    # f(n) = (12th-root(2))^(n-49) * 440Hz
    # https://en.wikipedia.org/wiki/Piano_key_frequencies
    
    # Pseudocode:
    # split string by characters (check)
    # if string contains more than 2 characters -> error invalid musical note (check)
    # find musical note order
    # find which note is given (e.g. the 4th La)
    # multiply note order with number of note
    # pass key number to formula
    # return frequency
    
    # Split input string into single characters.
    note_letter = list(key)[0]
    note_number = list(key)[1]
    if (len(list(key)) != 2) or (key_letter not in musical_note_order):
        print('Error in musical notation. Returning None.')
        return None
    
    # Calculate the key number.  
    # For example, A4 will be: 
    # N = musical_note_order['A'] + 12 * note_number = 1 + 12 * 4 = 49
    key_number = musical_note_oder[note_letter] + 12*int(note_number)
    # the above calculation is wrong, find a way to fix it
    
    pass


if __name__ == '__main__':
    pass
