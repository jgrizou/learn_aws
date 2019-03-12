import numpy as np

import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def lambda_handler(event, context):
    print(event)
    print(context)
    print(HERE_PATH)
    print(np.random.rand())
    return True
