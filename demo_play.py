# A simple demo with current features of BeatCobra.
# Save generated audio as as wav/mp3 files.
import time
import sys
from beatcobra.percussion import snare, kick
from beatcobra.tone import SquareGenerator, SawGenerator
from beatcobra.tools import return_key_frequency

def major_scale(A4=440, waveform='square', mode='fixed'):
    '''
    Simple demo playing the major scale, given the root note.
    '''
    # You can use fixed frequencies, or calculate the corresponding 
    # ones for each note/tone.
    if mode=='fixed':
        C_major = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
    elif mode=="dynamic":
        # A tool for calculating a note's frequency is now implemented.
        # Include this functionality here.
        pass
    else:
        print('Mode not supported')
        sys.exit()
    
    if waveform=='square':
        generator = SquareGenerator(duration=1)
    elif waveform=='saw':
        generator = SawGenerator(duration=1)
    else:
        print('Waveform generator not supported.')
        sys.exit()
    
    scale = []
    for frequency in C_major:
        scale = np.concatenate((scale, generator.generate(frequency)), axis=0)
    # TODO
    # play audio


if __name__=='__main__':
    
    print("You may have have to adjust the volume depending on your device.")
    print("The demo will begin in 5 seconds.")
    print("MIND YOUR EARS IF WEARING HEADPHONES!")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    print("MIND YOUR EARS IF WEARING HEADPHONES!")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    
    # play audio
    print("Demo of the C major scale using a square waveform.")
    major_scale(waveform='square')
    
