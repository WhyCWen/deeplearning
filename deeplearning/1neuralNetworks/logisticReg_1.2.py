
"""
• Build the general architecture of a learning algorithm, including:
– Initializing parameters
– Calculating the cost function and its gradient
– Using an optimization algorithm (gradient descent)
• Gather all three functions above into a main model function, in the right order.

Packages:
First, let’s run the cell below to import all the packages that you will need during this
assignment.
• numpy is the fundamental package for scientific computing with Python.
• h5py is a common package to interact with a dataset that is stored on an H5 file.
• matplotlib is a famous library to plot graphs in Python.
• PIL are used here to test your model with your own picture at the end
"""

import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from  PIL import Image
from  scipy import  ndimage
from  lr_utils import load_dataset

# Loading the data (cat/non-cat)
train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()