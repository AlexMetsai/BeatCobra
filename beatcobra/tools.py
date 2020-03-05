import json

def return_key_frequency(key='C4', A4=440):
    # Return the frequency of the provided note/piano key.
    # https://en.wikipedia.org/wiki/Piano_key_frequencies
    
    # Pseudocode:
    # split string by characters (check)
    # if string contains more than 2 characters -> error invalid musical note (check)
    # find musical note order
    # find which note is given (e.g. the 4th La)
    # multiply note order with number of note
    # pass key number to formula
    # return frequency
    
    # Load note order.
    with open("note_order.json") as json_file:
        order = json.load(json_file)
    musical_note_order = order['major_note_order']
    
    # Split input string into single characters and check for errors.
    note_letter = list(key)[0]
    note_number = int(list(key)[1])
    if (len(list(key)) != 2) or (key_letter not in musical_note_order) or (note_number not in range(1,13)):
        print('Error in musical notation. Returning None.')
        return None
    
    # Calculate the key's number.  
    # For example, A4 will be: 
    # N = musical_note_order['A'] + 12 * note_number - 9 = 10 + 12 * 4 - 9 = 49
    # C4 (middle C) will be:
    # N = 1 + 12 * 4 - 9
    key_number = musical_note_order[note_letter] + 12 * note_number - 9
    
    # Calculate key frequency.
    # f(n) = (12th-root(2))^(n-49) * A4 (Hz)
    f = (2**(1.0/12))**(key_number-49) * A4
    return f

if __name__ == '__main__':
    pass
