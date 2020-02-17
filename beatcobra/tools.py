
def return_key_frequency(key='C4', A4=440):
    # Things that need to be implemented for now are:
    # 1. Map notes to keys, e.g. A4 = 49th key, etc.
    # 2. Compute the frequency of its key.
    # The second can be easily achived by the following equation:
    # f(n) = (12th-root(2))^(n-49) * 440Hz
    # https://en.wikipedia.org/wiki/Piano_key_frequencies
    
    # Pseudocode:
    # split string by characters
    # if string contains more than 2 characters -> error invalid musical note
    # find musical note order
    # find which note is given (e.g. the 4th La)
    # multiply note order with number of note
    # pass key number to formula
    # return frequency
    
    musical_note_order = {'A':  1, 
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
    
    pass


if __name__ == '__main__':
    pass
