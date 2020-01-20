# ADD LICENSE AND BRIEF INFO/TODO LIST!!

import numpy as np
import wavio
from scipy import signal


class PercussionGenerator:
    '''
    Parent class for creating percussion sounds.
    Duration in seconds (s).
    '''
    def __init__(self, duration=3, rate=22050, decay_factor=10):
        self.T = duration
        self.rate = rate
        self.decay_factor = decay_factor
        self.t = np.linspace(0, self.T, self.T*rate, endpoint=False)
  
    def decay_function(self, decay_factor=10):
        # Exponential decay.
        # In the future, add more options for the type of decay.
        x = np.exp(-decay_factor*self.t)
        return(x)


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
        return(wave)
