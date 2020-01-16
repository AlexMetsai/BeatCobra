# ADD LICENSE AND BRIEF INFO/TODO LIST!!

import numpy as np
import wavio
from scipy import signal

class PercussionGenerator:
  '''
  Parent class for creating percussion sounds.
  Duration in seconds (s).
  '''
  def __init__(self, duration=3, rate=22050):
    self.T = duration
    self.rate = rate
    self.decay_factor = decay_factor
