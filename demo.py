# Make a simple demo with current features of BeatCobra.
# Add option for playing audio (once or in loop) or for saving
# as wav/mp3 files.

import wavio
import numpy as np
from percussion import *
from tone import *

# For a 24 bit file, wav.sampwidth must be equal to 3.
SAMPWIDTH = 3


def proto_loop(sample, loop_num):
    '''
    A prototype for a looping functionality. 
    Used in the demos for now, in the future a more advanced method may be 
    needed to be inserted into the core modules.
    '''
    return(np.tile(sample, loop_num))


def snare_kick_kick(beat_repeats=30):
    '''
    Simple demo with a kick/snare beat.
    '''
    
    # Create sample generator objects.
    snare = Snare(duration=0.5)
    kick = KickDrum(duration=0.5)
    
    # Generate samples.
    snare_sample = snare.generate(decay_factor=15)
    kick_sample = kick.generate()
    
    # Merge samples to create a beat.
    beat = np.concatenate((snare_sample, kick_sample, kick_sample), axis=0)
    
    # Loop the beat
    beat = proto_loop(beat, 10)
    
    # Write output to file.
    wavio.write('demo_beat1.wav',beat, snare.rate, sampwidth=SAMPWIDTH)

def major_scale(root_note=440):
    '''
    Simple demo playing the major scale, given the root note.
    '''
    #TODO
    # !TEST!
    pass

if __name__=='__main__':
    
    print('You may have have to adjust the volume depending on your device.\n' +
           'MIND YOUR EARS IF WEARING HEADPHONES!')
    
    snare_kick_kick()
