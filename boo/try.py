"""Run in console as:
   data-rosstat-boo-2013>python -m boo.try
"""

from . import config
print (config.VALID_YEARS)

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)