"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from scipy.linalg import toeplitz
from scipy.fftpack import fft, ifft
from gnuradio import gr



class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, gain=1.0, threshold = 0.0, filterTaps=[]):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Abdallah Convolution',   # will show up in GRC
            in_sig=[np.float32 ],
            out_sig=[np.complex64, np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.gain = gain
        self.threshold = threshold 
        self.filterTaps= filterTaps

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        #print (self.filterTaps)
        #output_items[0] = my_convolve(self.filterTaps, input_items[0])
        output_items[0] = np.convolve(input_items[0],self.filterTaps)
        output_items[1][:] = input_items[0] * self.gain 
     #  output_items[0][:] = input_items[0] * self.example_param
        return len(output_items[0])
        
	

def convMatrix(h,p):
    """
    Construct the convolution matrix of size (N+p-1)x p from the input matrix h of size N.
    Parameters:
        h : numpy vector of length N
        p : scalar value
    Returns:
        H : convolution matrix of size (N+p-1)xp
    """
    col=np.hstack((h,np.zeros(p-1)))
    row=np.hstack((h[0],np.zeros(p-1)))
    
    
    H=toeplitz(col,row)
    return H
    
def my_convolve(h,x):
    """
    Convolve two sequences h and x of arbitrary lengths: y=h*x
    Parameters:
        h,x : numpy vectors
    Returns:
        y : convolution of h and x
    """
    H=convMatrix(h,len(x)) #see convMatrix function
    y=H @ x.transpose() # equivalent to np.convolve(h,x) function
    return y    
    
 