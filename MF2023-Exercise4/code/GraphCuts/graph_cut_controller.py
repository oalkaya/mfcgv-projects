import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
from scipy.sparse import coo_matrix
from tkinter import *
from PIL import Image

from graph_cut import GraphCut
from graph_cut_gui import GraphCutGui


class GraphCutController:

    def __init__(self, args):
        self.__init_view(args.autoload)

    def __init_view(self, autoload=None):
        root = Tk()
        root.geometry("700x500")
        self._view = GraphCutGui(self, root)

        if autoload is not None:
            self._view.autoload(autoload)

        root.mainloop()

    # TODO: TASK 2.1
    def __get_color_histogram(self, image, seed, hist_res):
        """
	Compute a color histograms based on selected points from an image
	
	:param image: color image
	:param seed: Nx2 matrix containing the the position of pixels which will be
	            used to compute the color histogram
	:param histRes: resolution of the histogram
	:return hist: color histogram
	"""
        # Check order later
        pixels = image[seed[:,1], seed[:,0], :]
        hist, _ = np.histogramdd(pixels, hist_res)
        hist_filtered = ndimage.gaussian_filter(hist, 0.1)
        hist_normalized = hist_filtered / np.linalg.norm(hist_filtered)
        return hist_normalized


    # TODO: TASK 2.2
    # Hint: Set K very high using numpy's inf parameter
    def __get_unaries(self, image, lambda_param, hist_fg, hist_bg, seed_fg, seed_bg):
        """
        :param image: color image as a numpy array
        :param lambda_param: lamdba as set by the user
        :param hist_fg: foreground color histogram
        :param hist_bg: background color histogram
        :param seed_fg: pixels marked as foreground by the user
        :param seed_bg: pixels marked as background by the user
        :return: unaries : Nx2 numpy array containing the unary cost for every pixels in I (N = number of pixels in I)
        """
        # Define K
        K = np.inf
        
        # Create unaries based on image dimensions
        _ , width, _ = image.shape

        # # Flatten the image
        flattened_image = image.reshape(-1,3) 

        # Calculate the Rp costs
        def calc_Rp_per_row(row):
            # Going from pixel range 0-255 to 0-31 (shorthand for floor_divide is //)
            row = row // 8

            # Histogram gives the Pr(Ip | O) or Pr(Ip | B) respectively
            Rp_fg = -np.log(hist_fg[tuple(row)])
            Rp_bg = -np.log(hist_bg[tuple(row)])
            return np.array([lambda_param*Rp_fg, lambda_param*Rp_bg])

        unaries = np.apply_along_axis(calc_Rp_per_row, axis=1, arr=flattened_image)

        # Fill up Ks and 0s based on seeds
        fg_K_indices = seed_fg[:,1] * width + seed_fg[:,0]
        bg_K_indices = seed_bg[:,1] * width + seed_bg[:,0]
  
        # Edges to source
        np.put(unaries[:,0], fg_K_indices, K)
        np.put(unaries[:,0], bg_K_indices, 0.0)

        # Edges to sink
        np.put(unaries[:,1], fg_K_indices, 0)
        np.put(unaries[:,1], bg_K_indices, K)

        



        

    # TODO: TASK 2.3
    # Hint: Use coo_matrix from the scipy.sparse library to initialize large matrices
    # The coo_matrix has the following syntax for initialization: coo_matrix((data, (row, col)), shape=(width, height))
    def __get_pairwise(self, image):
        """
        Get pairwise terms for each pairs of pixels on image
        :param image: color image as a numpy array
        :return: pairwise : sparse square matrix containing the pairwise costs for image
        """
        # go from 3d to 1d for intensity
        # append to coo, for 8-neigbourhood (ie diags included)
        
    # TODO TASK 2.4 get segmented image to the view
    def __get_segmented_image(self, image, labels, background=None):
        """
        Return a segmented image, as well as an image with new background 
        :param image: color image as a numpy array
        :param label: labels a numpy array
        :param background: color image as a numpy array
        :return image_segmented: image as a numpy array with red foreground, blue background
        :return image_with_background: image as a numpy array with changed background if any (None if not)
        """


    def segment_image(self, image, seed_fg, seed_bg, lambda_value, background=None):
        image_array = np.asarray(image)
        background_array = None
        if background:
            background_array = np.asarray(background)
        seed_fg = np.array(seed_fg)
        seed_bg = np.array(seed_bg)
        height, width = np.shape(image_array)[0:2]
        num_pixels = height * width

        # TODO: TASK 2.1 - get the color histogram for the unaries
        hist_res = 32
        cost_fg = self.__get_color_histogram(image_array, seed_fg, hist_res)
        cost_bg = self.__get_color_histogram(image_array, seed_bg, hist_res)

        # TODO: TASK 2.2-2.3 - set the unaries and the pairwise terms
        unaries = self.__get_unaries(image_array, lambda_value, cost_fg, cost_bg, seed_fg, seed_bg)
        pairwise = self.__get_pairwise(image_array)

        # TODO: TASK 2.4 - perform graph cut
        # Your code here

        # Task 2.1 clone

        # TODO TASK 2.4 get segmented image to the view
        segmented_image, segmented_image_with_background = self.__get_segmented_image(image_array, labels,
                                                                                      background_array)
        # transform image array to an rgb image
        segmented_image = Image.fromarray(segmented_image, 'RGB')
        self._view.set_canvas_image(segmented_image)
        if segmented_image_with_background is not None:
            segmented_image_with_background = Image.fromarray(segmented_image_with_background, 'RGB')
            plt.imshow(segmented_image_with_background)
            plt.show()
