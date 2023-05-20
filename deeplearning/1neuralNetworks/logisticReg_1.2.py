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
from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset

# Loading the data (cat/non-cat)
train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()


# GRADED FUNCTION: sigmoid
def sigmoid(z):
    """
    Compute the sigmoid of z
    Arguments:
    z -- A scalar or numpy array of any size.
    Return:
    s -- sigmoid(z)
    """
    ### START CODE HERE ### (
    s = 1/(1 + np.exp(z))

    return s


def initialize_with_zeros(dim):
    """
    This function creates a vector of zeros of shape (dim, 1) for w and
    initializes b to 0. ,
    Argument:
    dim -- size of the w vector we want (or number of parameters in this case) ,
    输入的图图片扁平化的 维度,(把像素转化为 一维的长度 image.width *image.height * 3 )
    Returns:
    w -- initialized vector of shape (dim, 1)
    b -- initialized scalar (corresponds to the bias)
    """
    ### START CODE HERE ### (
    w = np.zeros((dim, 1))
    b = 0
    ### END CODE HERE ###
    assert(w.shape == (dim, 1))
    assert(isinstance(b, float) or isinstance(b, int))

    return w, b
