# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
A Python package for the quantitative analysis of the interaction of energetic photons with matter (x-rays and gamma-rays). 
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:
    import os
    import json

from roentgen.material import *