# ADD LICENSE AND BRIEF INFO/TODO LIST!!

import numpy as np
import wavio
from scipy import signal


class ToneGenerator:
    '''
    Parent class for creating combined waveforms.
    Duration in seconds (s).
    '''
    def __init__(self, duration=3, rate=22050, harmonics_num=3):
        self.T = duration
        self.rate = rate
        self.harmonics_num = harmonics_num
        # create the time intervals
        self.t = np.linspace(0, self.T, int(self.T*rate), endpoint=False)
  
    def generate(self, f):
        '''
        The combined signal is generated by basic waveform with the
        fundamental frequency f, and a number of harmonic waveforms,
        with frequencies that are multiples of f (2f, 3f, 4f etc.)
        '''
        x = self.waveform(f)
        for i in range(1, self.harmonics_num+1):
            # Each consecutive harmonic has less energy than the previous one.
            x += np.power(0.5,i)*self.waveform((i+1)*f)
      
        return(x)


class SineGenerator(ToneGenerator):
    def __init__(self, duration=3, rate=22050, harmonics_num=3):
        super().__init__(duration, rate, harmonics_num)
    
    def waveform(self, f):
        wave = np.sin(2*np.pi*f*self.t)
        return(wave)


class SquareGenerator(ToneGenerator):
    def __init__(self, duration=3, rate=22050, harmonics_num=3):
        super().__init__(duration, rate, harmonics_num)
    
    def waveform(self, f):
        wave = signal.square(2*np.pi*f*self.t)
        return(wave)

class SawGenerator(ToneGenerator):
    def __init__(self, duration=3, rate=22050, harmonics_num=3):
        super().__init__(duration, rate, harmonics_num)

    def waveform(self, f):
        wave = signal.sawtooth(2*np.pi*f*self.t)
        return(wave)

if __name__=='__main__':
    # This module is ment to be imported, but show some examples.
    # Would it be best to save or play the generated waveforms?
    pass
