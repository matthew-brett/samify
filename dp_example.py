""" Script to show dephasing in action
"""

# Install with pip install scikit-image
import skimage

from dephase import dephase, rescale

# Load original image
img = skimage.io.imread('omega.png', as_gray=True)

# Dephase, mostly
dp_img = dephase(img, 0.75)

# WARNING - this will change image intensity levels
# Worth rethinking what that intensity scaling should be.
rescaled = rescale(dp_img)

# Write out dephased version
skimage.io.imsave('dp_omega.png', rescaled)
