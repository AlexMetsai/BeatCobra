'''
Copyright (C) 2020 Alexandros I. Metsai
alexmetsai@gmail.com

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 3
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import numpy as np
import wavio
from scipy import signal
from beatcobra.tone import *


class PercussionGenerator:
    '''
    Parent class for creating percussion sounds.
    Duration in seconds (s).
    '''
    def __init__(self, duration=3, rate=22050, decay_factor=10):
        self.T = duration
        self.rate = rate
        self.decay_factor = decay_factor
        self.t = np.linspace(0, self.T, int(self.T*rate), endpoint=False)
  
    def decay_function(self, decay_factor=10):
        # Exponential decay.
        # In the future, add more options for the type of decay.
        x = np.exp(-decay_factor*self.t)
        return x


class Snare(PercussionGenerator):
    '''
    A simple snare-like sound can be generated
    by a rapidly decaying noise.
    '''
    def __init__(self, duration=3, rate=22050, decay_factor=10):
        super().__init__(duration, rate, decay_factor)
    
    def noise(self, noise_color):
        if noise_color == 'white':
            return(np.random.random(self.t.shape))
        else:
            print("Error: noise color", noise_color, "not supported.")
            exit(-1)
    
    def generate(self, decay_factor=10, noise_color='white'):
        noise = self.noise(noise_color)
        decay = self.decay_function(decay_factor)
        wave = noise * decay
        return wave


class KickDrum(PercussionGenerator, SineGenerator):
    '''
    A simple kick drum sound can be generated
    by a decaying low frequency wave.
    '''
    def __init__(self, duration=3, rate=22050, decay_factor=10):
        super().__init__(duration, rate, decay_factor)
    
    def generate(self, decay_factor=10, f=70):
        x = self.waveform(f)
        decay = self.decay_function(decay_factor)
        wave = x * decay
        return wave


if __name__=='__main__':
    # This module is meant to be imported, but show some examples.
    # Would it be best to save or play the generated waveforms?
    pass
