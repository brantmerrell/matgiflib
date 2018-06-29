"""
Gif.py
David Merrell
2018-06-28

This module defines the Gif class.
Gif objects correspond to whole GIF files;
i.e., for each GIF you want to make, a Gif object
must be constructed and acted upon.
"""

import matplotlib.pyplot as plt
import subprocess as sp
import math
import os

class Gif:
    """ 
    Each instance of this class represents a GIF file. 
    A Gif object has methods for building individual frames
    and then composing them into a GIF file.

    The operating principle is this: each frame of the GIF corresponds to 
    a matplotlib Figure object. This Gif class just keeps things tidy 
    while you're making a GIF.
    """


    def __init__(self, filename, width, height, 
                 max_frames=1000, stride=1,
                 frame_suff=".png", **kwargs):
        """ 
        Constructor.

        :param filename: a filename/path for the GIF we're making
        :param width: the width of the GIF, in inches
        :param height: the height of the GIF, in inches

        Possible keyword arguments:
        :param max_frames: the maximum number of frames the GIF may contain.
        :param stride: an integer. Every stride-th frame is created; 
                       the others are skipped. Initialized at 1 (i.e., all frames
                       are created).
        :param frame_suff: the kind of image file we want our frames to be
                           rendered as. Default is .png.

        Other than these, the keyword arguments available to Matplotlib 
        Figure objects are appropriate for this constructor.
        """

        # Set basic, necessary attributes
        self.filename = filename
        self.width = width
        self.height = height
        self.max_frames = max_frames

        # Store the keyword arguments for later, 
        # when we construct frames
        self.kwargs = kwargs 

        # This is the name of a temporary directory where we'll
        # keep intermediate stuff (e.g. frame images)
        self.tmp_dir = "__mgl_tmp__"
        if not os.path.exists(self.tmp_dir):
            res = sp.call(["mkdir", self.tmp_dir])
            if res != 0:
                print("Error: unable to make temporary directory at {}".format(self.tmp_dir))
                raise OSError 
        else: # If the temporary directory already exists, make sure it's empty
            sp.call("rm {}".format(os.path.join(self.tmp_dir,"*")), shell=True)

        # Set some other attributes that allow this class
        # to do its job

        self.file_basename = os.path.basename(self.filename)

        self.tmp_prefix = os.path.join(self.tmp_dir,self.file_basename.split('.')[0])
        self.tmp_suffix = frame_suff 
        self.frame_count = 0   # keep track of the number of frames
        self.in_scope = False  # are we currently making a frame?
        self.current_frame = None        # This will store the figure we are currently building

        return


    def start_frame(self):
        """
        Indicates that we are beginning a new frame for the GIF.
        A new Figure object is created, using specifications provided to the
        Gif's constructor.

        Note that you are constrained to make one frame at a time---for every
        start_frame, there must be a end_frame without another start_frame
        in between.

        :return: fig, a Matplotlib figure object
        """

        # Check whether we're already making a frame. 
        if self.in_scope:
            print("The Gif object for {} has encountered 'start_frame' twice\
                   without an intervening 'end_frame'".format(self.filename))
            raise SyntaxError

        # Construct a new figure
        fig = plt.figure(figsize=(self.width,self.height), **(self.kwargs))
        self.current_frame = fig

        # Set the "in_scope" member True
        self.in_scope = True

        return self.current_frame


    def end_frame(self, **kwargs):
        """
        Render, save, and close this frame.

        Keyword arguments: all of those available to the 
        figure.savefig(...) method.

        :return: nothing
        """
        if not self.in_scope: 
            print("The Gif object for {} has encountered 'end_frame' twice\
                   without an intervening 'start_frame'".format(self.filename))
            raise SyntaxError


        # Save the frame to the temporary directory
        count_width = str(int(math.log10(self.max_frames) + 1))
        label = "{:0>"+count_width+"d}"
        label = label.format(self.frame_count)
        file_path = "{}_{}{}".format(self.tmp_prefix, label, self.tmp_suffix)
        self.current_frame.savefig(file_path,**kwargs)

        # Close the figure
        plt.close(self.current_frame)
        
        # Update some relevant attributes
        self.current_frame = None
        self.frame_count += 1
        self.in_scope = False

        return


    def close(self):
        """
        Call this when all the desired frames have been created.
        It creates the GIF and cleans up all temporary files
        """

        sp.call(["convert", "{}_*".format(self.tmp_prefix),
                            self.filename])

        sp.call("rm {}_*".format(self.tmp_prefix), shell=True)
        sp.call(["rmdir", self.tmp_dir])


