

import os

path = os.path.dirname(os.path.realpath(__file__))
dirs = os.listdir( path )
for file in dirs:
    print("S:" + file)