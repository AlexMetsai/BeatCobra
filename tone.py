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
    self.t = np.linspace(0, self.T, self.T*rate, endpoint=False)
  
  def generate(self, f):
    
    x = self.waveform(f)
