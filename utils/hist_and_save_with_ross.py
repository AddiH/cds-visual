import cv2
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.join(".."))

'''
Takes an image and prints the RGB histogram of the img to screen, then it saves the histogram.
'''

def ross_hist(filename):
    # make path
    in_path = os.path.join("..", "data", "img", filename)
    # load img
    image = cv2.imread(in_path)
    # split channels
    channels = cv2.split(image)
    # names of colours
    colors = ("b", "g", "r")
    # create plot
    plt.figure()
    # add title
    plt.title("Histogram")
    # Add xlabel
    plt.xlabel("Bins")
    # Add ylabel
    plt.ylabel("# of Pixels")

    # for every tuple of channel, colour
    for (channel, color) in zip(channels, colors):
        # Create a histogram
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        # Plot histogram
        plt.plot(hist, color=color)
        # Set limits of x-axis
        plt.xlim([0, 256])
    # Save path
    hist_filename = f'histogram_of_{filename}'
    out_path = os.path.join("..", "data", "img", hist_filename)
    # Save img
    plt.savefig(out_path) # THIS HAS TO HAPPEN BEFORE PLT.SHOW()
    # Show plot
    plt.show()