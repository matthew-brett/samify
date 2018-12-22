""" Make a letter, save as a PNG
"""

from os.path import join as pjoin, dirname

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = dirname(__file__)

omega = u'\u03A9'

plt.text(0.5, 0.5, omega, fontsize=300, horizontalalignment='center',
         verticalalignment='center')
plt.axis('off')
plt.savefig(pjoin(HERE, 'omega.png'))
