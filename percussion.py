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
